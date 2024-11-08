import json
import flask
import streamlit as st
import altair

# Load images (replace with actual image paths or URLs)
# logo = Image.open("path_to_logo.png")
# automation_image = Image.open("path_to_automation_image.png")

# App Header
st.set_page_config(page_title="Auto Anchor", page_icon="🚀", layout="centered")
# st.image(logo, width=100)
st.title("Welcome to Auto Anchor 🚀")
st.subheader("Your DevOps Automation Partner for Streamlit Deployments")

# Intro Section
st.write("**Auto Anchor** makes DevOps seamless by automating the process of deploying Streamlit applications.")
st.write("Simply provide your application folder, and Auto Anchor will generate your `requirements.txt` file and create a `Dockerfile` — all without manual setup.")

# Features Section
st.header("Key Features")
st.write("🔹 **Automated Requirements**: Detects dependencies and builds `requirements.txt` for you.")
st.write("🔹 **Dockerfile Generation**: Quickly creates a Dockerfile tailored to your app’s setup.")
st.write("🔹 **Folder-Driven Automation**: Just give the folder, and Auto Anchor does the rest!")

# Add Images
# st.image(automation_image, caption="Automate Streamlit Deployments with Auto Anchor", use_column_width=True)

# Call-to-Action
st.markdown("## Get Started Today!")
st.write("Start using Auto Anchor to simplify your Streamlit deployments. Experience DevOps without the hassle.")
st.button("Try Auto Anchor Now")



