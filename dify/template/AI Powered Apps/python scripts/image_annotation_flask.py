from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

def annotate_image(image_base64, detection_json):
    try:
        print("[DEBUG] Length of received base64 string:", len(image_base64))

        # Remove data URI prefix
        if image_base64.startswith("data:image"):
            image_base64 = image_base64.split(",", 1)[1]

        # Decode base64 → numpy array → OpenCV image
        image_bytes = base64.b64decode(image_base64)
        print("[DEBUG] Decoded bytes length:", len(image_bytes))

        img_array = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if img is None:
            print("[DEBUG] cv2.imdecode returned None")
            return None, "Failed to decode image from base64."

        h, w, _ = img.shape
        print(f"[DEBUG] Image decoded successfully, shape: {img.shape}")

        # Draw boxes
        for obj in detection_json.get("objects", []):
            name = obj.get("name", "")
            for coord in obj.get("coordinates", []):
                x_min = int(coord[0] * w)
                y_min = int(coord[1] * h)
                x_max = int(coord[2] * w)
                y_max = int(coord[3] * h)
                print(f"[DEBUG] Drawing box for {name}: ({x_min},{y_min})-({x_max},{y_max})")
                cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                cv2.putText(img, name, (x_min, y_min - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Convert back to base64 with data URI prefix
        _, buffer = cv2.imencode('.jpg', img)
        cv2.imwrite("annotated_output.jpg", img)  # <-- saves locally
        img_base64_out = base64.b64encode(buffer).decode('utf-8')
        img_base64_out = f"data:image/jpeg;base64,{img_base64_out}"
        # <-- ADD THIS LINE
        with open("annotated_output_base64.txt", "w") as f:
            f.write(img_base64_out)

        print("[DEBUG] Successfully generated output base64")
        return img_base64_out, None

    except Exception as e:
        print(f"[DEBUG] Exception in annotate_image: {e}")
        return None, f"Unexpected error: {str(e)}"

@app.route('/annotate', methods=['POST'])
def annotate():
    data = request.json
    print("[DEBUG] Received POST data keys:", list(data.keys()) if data else None)

    image_base64 = data.get('image_base64')   # <-- Now expecting base64, not URL
    detection_json = data.get('detection_json', {})

    if not image_base64:
        print("[DEBUG] No image_base64 provided in request")
        return jsonify({"error": "No image_base64 provided"}), 400

    annotated_img, error = annotate_image(image_base64, detection_json)
    if error:
        print(f"[DEBUG] Error in annotation: {error}")
        return jsonify({"error": error}), 400

    return jsonify({"annotated_image": annotated_img})

if __name__ == '__main__':
    print("[DEBUG] Starting Flask server on 0.0.0.0:5010")
    app.run(host='0.0.0.0', port=5010)
