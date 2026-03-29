# import streamlit as st
# from scraper import get_mock_jobs

# st.set_page_config(page_title="AI Career Assistant", layout="wide")

# st.title("💼 AI Career Assistant - Job Finder")

# # INPUT BOX
# query = st.text_input("Enter job role (e.g. Python Developer, Data Analyst)")

# location_filter = st.selectbox(
#     "Filter by Location",
#     ["All", "Bangalore", "Hyderabad", "Pune"]
# )

# # LOAD DATA
# jobs = get_mock_jobs()

# # FILTER LOGIC
# if location_filter != "All":
#     jobs = [job for job in jobs if job["location"] == location_filter]

# # SEARCH SIMULATION
# if query:
#     jobs = [job for job in jobs if query.lower() in job["title"].lower()]

# # DISPLAY RESULTS
# st.subheader("📌 Job Listings")

# for job in jobs:
#     st.markdown(f"""
#     ### {job['title']}
#     - 🏢 Company: {job['company']}
#     - 📍 Location: {job['location']}
#     - 🎓 Experience: {job['experience']}
#     - 💰 Salary: {job['salary']}
#     ---
#     """)
#     st.sidebar.info("AI-powered job search assistant for Indian job seekers")

from ai_helper import career_advice
import streamlit as st
from scraper import get_mock_jobs
from resume_parser1 import extract_resume_text

st.title("💼 AI Career Assistant")

# 1. JOB DATA
jobs = get_mock_jobs()

# 2. USER INPUT
query = st.text_input("Enter job role")

# 3. FILTER JOBS
if query:
    jobs = [job for job in jobs if query.lower() in job["title"].lower()]

# 4. ⭐ ADD RESUME UPLOAD HERE (BEST PLACE)
st.subheader("📄 Upload Resume")

uploaded_file = st.file_uploader("Upload Resume (PDF)")

if uploaded_file:
    text = extract_resume_text(uploaded_file)
    st.text_area("Resume Text", text, height=200)

# 5. SHOW JOBS
st.subheader("📌 Job Listings")

for job in jobs:
    st.write(job)
st.subheader("🤖 AI Career Advice")

user_input = st.text_input("Ask Career Assistant")

if user_input:
    result = career_advice(user_input)
    st.success(result)