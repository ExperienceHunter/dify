# 🚀 App Creator

**App Creator** is a tool that allows users to quickly build and publish apps using **DSL (Domain-Specific Language) templates**.  
Instead of manually writing complex configurations, users only need to provide a **query** describing what they want, and App Creator automatically modifies the underlying DSL to generate a working app.  

This makes it easy to:
- Create AI-powered apps without coding from scratch  
- Customize workflows, system prompts, and UI logic  
- Publish and start using apps instantly  

---

## 📌 Workflow Overview

This diagram illustrates the **end-to-end flow** of creating and publishing a custom app using DSL templates.

1. **Choose App Category**  
   The user begins by selecting a category (e.g., AI-Powered Apps, Form Apps, etc.).  
   This determines the type of DSL template that will be retrieved.  

2. **Provide Query**  
   The user specifies their requirements or desired changes for the app.  
   This query guides how the DSL template will be modified.  

3. **Fetch DSL Template**  
   The system retrieves a base DSL template corresponding to the chosen app category.  

4. **Modify DSL**  
   The DSL template is updated based on the user’s query.  
   Example: changing the chatbot’s system prompt, title, or workflow behavior.  

5. **Import DSL**  
   The modified DSL is imported back into the system.  
   At this stage, the app definition is recognized and ready for deployment.  

6. **Publish App**  
   The app is deployed and becomes available for use.  

7. **Use App**  
   The user can now interact with their custom app.  
   Optionally, the flow can restart if the user wants to build or adjust another app.  

---

📷 *Diagram: High-level workflow of building and publishing an app with DSL templates.*
