# 🏆 CoachBot AI – Adaptive Youth Performance Intelligence System  

**Course:** Artificial Intelligence  
**Project Type:** Generative AI Web Application  
**Model Used:** GPT-4o-mini (OpenAI)  
**Framework:** Streamlit  

**Student Name:** Dwij Vala  
**Candidate Registration Number:** 2505369  

---

## App Link
https://coach-bot-dwij.streamlit.app/

---
## 📌 Project Overview  

CoachBot AI is a Generative AI-powered web application designed to provide personalized fitness coaching, tactical advice, injury-aware training modifications, and nutrition guidance for youth athletes.  

The system simulates a certified elite youth performance coach using AI and generates structured, safe, and goal-oriented training programs.

The application adapts outputs based on:

- Sport and position  
- Experience level  
- Injury history  
- Pain level  
- Risk tolerance  
- Training mode  
- Performance goals  

This project demonstrates practical application of Generative AI in sports development and youth performance optimization.

---

## 🌍 Problem Definition  

Many young athletes lack access to professional coaching, structured training plans, and injury-aware conditioning systems.  

Common issues include:

- Overtraining  
- Poor recovery  
- Increased injury risk  
- Improper nutrition planning  
- Lack of tactical awareness  

CoachBot AI addresses these challenges by generating personalized weekly training plans, tactical advice, and nutrition strategies while prioritizing safety and structured development.

---

## 🔬 Research & Conceptual Foundation  

The project was influenced by research in:

- Youth athletic development models  
- Periodization and load management principles  
- Injury prevention frameworks  
- Sports nutrition planning  
- AI-based personalized recommendation systems  

Key insights implemented:

- Training must adapt to injury severity  
- Structured weekly plans improve performance consistency  
- Nutrition should align with athletic goals  
- Mental preparation enhances match performance  
- AI prompts must enforce structured output formatting  

---

## 🤖 AI Model Used  

**Model:** GPT-4o-mini (OpenAI)  
**Accessed via:** OpenAI Python SDK  

The model was selected because it:

- Provides structured and coherent outputs  
- Supports temperature-based creativity control  
- Handles complex multi-section generation  
- Produces consistent formatting for parsing  

---

## 🎯 Prompt Engineering Strategy  

The system uses structured prompting that includes:

- Defined AI persona ("Certified Elite Youth Performance Coach")  
- Athlete profile embedding  
- Mode-based training adjustment  
- Injury-aware constraints  
- Strict output format enforcement  

The model is instructed to return structured sections:

```
=== WEEKLY PLAN ===
Monday:
Tuesday:
Wednesday:
Thursday:
Friday:
Saturday:
Sunday:

=== POSITION DRILLS ===
=== TACTICAL ADVICE ===
=== NUTRITION PLAN ===
=== RECOVERY PROTOCOL ===
=== MENTAL PREPARATION ===
=== SAFETY NOTES ===
```

This ensures consistency and allows parsing for data visualization.

---

## 🧠 Core Features Implemented  

### 1️⃣ Athlete Intelligence Module  
- Age, height, weight (BMI calculation)  
- Sport & position  
- Experience level  
- Injury history  
- Pain level slider  
- Risk tolerance selector  

### 2️⃣ Smart Training Modes  
- Normal Training  
- Tournament Preparation  
- Injury Recovery  
- Off-Season Mode  

### 3️⃣ AI Control Features  
- Temperature slider (creativity control)  
- Coach style selection (Structured / Motivational)  

### 4️⃣ Performance Analytics  
- BMI calculation  
- Injury risk scoring  
- Estimated calorie requirement  
- Macronutrient distribution chart  

### 5️⃣ Output Management  
- Structured weekly plan parsing  
- Full AI output display  
- PDF export functionality  

### 6️⃣ Safety Layer  
- Injury-based modifications  
- Overtraining warnings  
- Professional disclaimer  

---

## 🔧 Hyperparameter Tuning  

Temperature testing was conducted at:

- **0.3 – 0.4:** Conservative, structured outputs  
- **0.5 – 0.6:** Balanced personalization  
- **0.7+:** Creative tactical advice  

Optimal balance was found between 0.4 and 0.6 for structured training outputs.

---

## 🧪 Model Validation  

Testing included:

- Multiple sport types  
- Injury-heavy profiles  
- Beginner vs Competitive athletes  
- Different training modes  
- Output structure validation  

The model output was refined to ensure:

- Clear segmentation  
- Injury-aware advice  
- Structured weekly planning  
- Safe and realistic recommendations  

---

## 🚀 Deployment Instructions  

### Local Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the application:

```
streamlit run coach-bot-app.py
```

---

## 📦 Repository Structure  

```
coach-bot-app.py
requirements.txt
README.md
.gitignore
---

## 🌐 Live Streamlit Application  

The CoachBot AI application is deployed on Streamlit Cloud and can be accessed using the link below:

🔗 **Live App:**  
https://coach-bot-dwij.streamlit.app/

> Note: If the app takes a few seconds to load, please wait while the server wakes up.


---

## 🎥 Video Demonstration  

A full demonstration of the application has been recorded showing:

- Athlete profile input process  
- AI generation workflow  
- Weekly plan parsing  
- Analytics dashboard  
- PDF export feature  
- Temperature adjustment demonstration  

📌 Video Link:  
https://drive.google.com/file/d/1jcmv8ANNd_3bO5M3kWKfmLwSVliBCoAQ/view?usp=sharing

---

## ⚠ Disclaimer  

CoachBot AI provides AI-generated guidance for educational purposes only. Athletes should consult certified coaches or medical professionals before implementing training changes.
