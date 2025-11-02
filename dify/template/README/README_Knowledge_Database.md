
# 🧠 Knowledge Database Template

This template demonstrates how to create a **custom knowledge database app** using **App Creator** and DSL templates.  
By describing the type of knowledge app you want, **App Creator** automatically builds and publishes it for you.

---

## ⚙️ Requirements

Before using this template, make sure your **App Creator environment** is properly set up.  
You will also need access to a **Knowledge Database API** or endpoint to upload and manage files.  
All document processing, embedding, and indexing are handled automatically within the workflow.

---

## 📌 Steps to Create Your Knowledge Database App

### 1. Start App Creator
- Open **App Creator**.  
- In **Choose App Category**:  
  - For **Content_and_Knowledge**, select **Knowledge Database**.  
  - For the rest of the categories, choose **None**.  
- In the **Query** field, type what kind of knowledge app you want (e.g., *"create a knowledge base for company policies"*, *"build a searchable database for research papers"*, *"develop a chatbot that answers using uploaded documents"*).  

💬 *Example UI*  
![Step 1](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/Images/KnowledgeDatabase_Image_1.png)

---

### 2. Execute Workflow
- Click on **Execute**.  
- If the workflow runs successfully, it will generate a **URL** for your newly created knowledge database app.  
- Click the link to open the app.  

💬 *Example Output*  
![Step 2](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/Images/KnowledgeDatabase_Image_2.png)

---

### 3. Upload and Index Documents
- Open your app and upload one document (PDF, TXT, DOCX, CSV, etc.).
- The system automatically:  
  - Extracts text content  
  - Cleans and segments the data  
  - Embeds it into the **Knowledge Database** using your configured embedding model  
- Once processed, your documents become searchable and retrievable for Q&A tasks.
**Note**
- You can only upload one document through the workflow. To upload multiple files, please at least upload the file once through the workflow so that the knowledge database is created. Then you can upload the files manually through the Dify GUI.

💬 *Execution Result*  
![Step 3a](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/Images/KnowledgeDatabase_Image_3.png)

---

### 4. Query Your Knowledge Base
- Enter a question or keyword related to your uploaded documents.  
- The app retrieves the most relevant content and provides an AI-generated answer with supporting context.  

💬 *Example Result:*  
> **Question:** What are the refund policies in the company handbook?  
> **Answer:** The handbook states that refunds are processed within 7 business days for valid claims, with approval from the finance department.
> 
💬 *Execution Result*  
![Step 3a](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/Images/KnowledgeDatabase_Image_4.png)

---

## ✅ Features
- Supports **multiple document uploads** (PDF, TXT, DOCX, CSV)  
- Automatic **text extraction**, **cleaning**, and **embedding**  
- Uses semantic search for **context-aware retrieval**  
- Fully customizable via **DSL templates**  
- Works seamlessly with **chatbot** and **workflow** integrations  

---

## 📂 Next Steps
- Modify the query to experiment with different knowledge-based applications.  
- Integrate this knowledge base with a **chatbot workflow** to answer questions using your uploaded documents.  
- Explore other templates like [💬 Sentiment Analysis](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/README_Sentiment_Analysis.md) or [🖼️ Image Detector](https://github.com/ExperienceHunter/dify/blob/main/dify/template/README/README_Image_Detector.md).
