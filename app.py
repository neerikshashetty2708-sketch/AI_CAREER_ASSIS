import streamlit as st
from scraper import get_mock_jobs

st.set_page_config(page_title="AI Career Assistant", layout="wide")

st.title("💼 AI Career Assistant - Job Finder")

# INPUT BOX
query = st.text_input("Enter job role (e.g. Python Developer, Data Analyst)")

location_filter = st.selectbox(
    "Filter by Location",
    ["All", "Bangalore", "Hyderabad", "Pune"]
)

# LOAD DATA
jobs = get_mock_jobs()

# FILTER LOGIC
if location_filter != "All":
    jobs = [job for job in jobs if job["location"] == location_filter]

# SEARCH SIMULATION
if query:
    jobs = [job for job in jobs if query.lower() in job["title"].lower()]

# DISPLAY RESULTS
st.subheader("📌 Job Listings")

for job in jobs:
    st.markdown(f"""
    ### {job['title']}
    - 🏢 Company: {job['company']}
    - 📍 Location: {job['location']}
    - 🎓 Experience: {job['experience']}
    - 💰 Salary: {job['salary']}
    ---
    """)