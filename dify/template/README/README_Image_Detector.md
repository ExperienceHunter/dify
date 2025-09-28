# 🖼️ Image Detector Template

This template demonstrates how to create a **custom image detection app** using **App Creator** and DSL templates.  
By describing the type of image detector you want, App Creator automatically builds and publishes it for you.

---
## ⚙️ Requirements

Before using this template, make sure the **image annotation service** is running.  
Also, ensure the file `image_annotation_flask.py` is available and ready to execute.

```bash
python image_annotation_flask.py
---

## 📌 Steps to Create Your Image Detector

### 1. Start App Creator
- Open **App Creator**.  
- In **Choose App Category**:  
  - For **AI_Powered_Apps**, select **Image Detector**.  
  - For the rest of the categories, choose **None**.  
- In the **Query** field, type what kind of image detector you want (e.g., *"detect animals in photos"*, *"identify cars in traffic images"*, *"highlight damaged areas on products"*).  

📷 *Example UI*  
![Step 1](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/Images/ImageDetector_Image_1.png)

---

### 2. Execute Workflow
- Click on **Execute**.  
- If the workflow runs successfully, it will generate a **URL** for your newly created image detector app.  
- Click the link to open the app.  

📷 *Example Output*  
![Step 2](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/Images/ImageDetector_Image_2.png)

---

### 3. Use Your Image Detector
- Upload or provide an image to the app.  
- The app will return both the **execution result** and an **annotated image** with detected objects highlighted.  

📷 *Execution Result*  
![Step 3a](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/Images/ImageDetector_Image_3.png)

📷 *Annotated Output (Detected Image)*  
![Step 3b](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/Images/ImageDetector_Image_4.png)

---

## ✅ Features
- Fully customizable detection logic via **query input**  
- Supports visual object detection for a variety of use cases  
- Built with **DSL templates** for flexibility  
- Instant publishing and ready-to-use app  

---

## 📂 Next Steps
- Modify the query to experiment with different detection tasks.  
- Explore other templates like [🤖 Chatbot](../chatbot/README.md).  
