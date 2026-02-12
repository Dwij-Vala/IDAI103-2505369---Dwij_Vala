import streamlit as st
from openai import OpenAI
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import re
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# =====================================
# CONFIG
# =====================================

st.set_page_config(page_title="CoachBot AI", layout="wide")

# 🔴 PASTE YOUR NEW OPENAI KEY BELOW
API_KEY = "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"

client = OpenAI(api_key=API_KEY)

# =====================================
# UTILITY FUNCTIONS
# =====================================

def calculate_bmi(height_cm, weight_kg):
    if height_cm <= 0:
        return 0
    return round(weight_kg / ((height_cm / 100) ** 2), 2)

def calculate_injury_risk(pain, injuries, tolerance):
    score = pain * 6 + len(injuries) * 12
    if tolerance == "Conservative":
        score += 15
    elif tolerance == "Aggressive":
        score -= 10
    return max(0, min(100, score))

def estimate_calories(weight, goal):
    base = weight * 30
    if goal == "Stamina":
        base *= 1.3
    elif goal == "Strength":
        base *= 1.2
    return int(base)

def generate_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    elements = []
    styles = getSampleStyleSheet()
    elements.append(Paragraph("CoachBot AI Training Plan", styles["Heading1"]))
    elements.append(Spacer(1, 0.4 * inch))
    elements.append(Paragraph(text.replace("\n", "<br/>"), styles["Normal"]))
    doc.build(elements)
    buffer.seek(0)
    return buffer

def parse_weekly_plan(text):
    pattern = r"=== WEEKLY PLAN ===(.*?)==="
    match = re.search(pattern, text, re.DOTALL)

    if not match:
        return pd.DataFrame()

    content = match.group(1)
    rows = []

    for line in content.split("\n"):
        if ":" in line:
            day, plan = line.split(":", 1)
            rows.append({"Day": day.strip(), "Plan": plan.strip()})

    return pd.DataFrame(rows)

def build_prompt(profile, mode, style):

    persona = "You are a certified elite youth performance coach."
    if style == "Motivational":
        persona += " Speak in an inspiring and energetic tone."
    else:
        persona += " Speak in a structured and safety-focused tone."

    return f"""
{persona}

Athlete Profile:
Name: {profile['name']}
Age: {profile['age']}
Sport: {profile['sport']}
Position: {profile['position']}
Experience: {profile['experience']}
Goal: {profile['goal']}
Injuries: {profile['injuries']}
Pain Level: {profile['pain']}
Training Mode: {mode}

Return structured sections:

=== WEEKLY PLAN ===
Monday:
Tuesday:
Wednesday:
Thursday:
Friday:
Saturday:
Sunday:

=== POSITION DRILLS ===
Provide 3-5 sport-specific drills.

=== TACTICAL ADVICE ===
Provide structured guidance.

=== NUTRITION PLAN ===
Include calorie guidance and macronutrients.

=== RECOVERY PROTOCOL ===
Include warm-up and cooldown.

=== MENTAL PREPARATION ===
Include mindset advice.

=== SAFETY NOTES ===
Include injury prevention advice.
"""

# =====================================
# UI
# =====================================

st.title("CoachBot AI – Elite Youth Performance System")

left, right = st.columns([1, 2])

with left:
    st.header("Athlete Profile")

    name = st.text_input("Athlete Name", "Athlete")
    age = st.number_input("Age", 10, 25, 15)
    height = st.number_input("Height (cm)", 120, 220, 170)
    weight = st.number_input("Weight (kg)", 30, 150, 65)

    sport = st.selectbox("Sport", ["Football", "Cricket", "Basketball", "Athletics", "Tennis"])
    position = st.text_input("Position")
    experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Competitive"])
    goal = st.selectbox("Primary Goal", ["Stamina", "Strength", "Agility", "Recovery"])

    injuries = st.multiselect("Injury History", ["Knee", "Ankle", "Shoulder", "Back", "Hamstring"])
    pain = st.slider("Pain Level", 0, 10, 0)
    tolerance = st.selectbox("Risk Tolerance", ["Conservative", "Balanced", "Aggressive"])

    mode = st.selectbox("Training Mode",
                        ["Normal Training", "Tournament Prep", "Injury Recovery", "Off-Season"])

    temperature = st.slider("Creativity Level", 0.1, 1.0, 0.4)
    style = st.selectbox("Coach Style", ["Structured", "Motivational"])

    generate = st.button("Generate Plan")

with right:

    if generate:

        bmi = calculate_bmi(height, weight)
        risk = calculate_injury_risk(pain, injuries, tolerance)
        calories = estimate_calories(weight, goal)

        profile = {
            "name": name,
            "age": age,
            "sport": sport,
            "position": position,
            "experience": experience,
            "goal": goal,
            "injuries": injuries,
            "pain": pain
        }

        with st.spinner("Generating AI Plan..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a certified elite youth performance coach."},
                    {"role": "user", "content": build_prompt(profile, mode, style)}
                ],
                temperature=temperature
            )

        output = response.choices[0].message.content

        tabs = st.tabs(["Weekly Plan", "Analytics", "Full Output"])

        with tabs[0]:
            df = parse_weekly_plan(output)
            if not df.empty:
                st.dataframe(df)
            else:
                st.write(output)

        with tabs[1]:
            st.metric("BMI", bmi)
            st.metric("Injury Risk Score", risk)
            st.metric("Estimated Calories", calories)

            fig, ax = plt.subplots()
            ax.pie([50, 30, 20], labels=["Carbs", "Protein", "Fats"], autopct='%1.1f%%')
            st.pyplot(fig)

        with tabs[2]:
            st.write(output)

        pdf = generate_pdf(output)
        st.download_button("Download PDF", pdf, "coachbot_plan.pdf")

        st.info("CoachBot AI provides guidance only. Consult professionals before implementing training changes.")
