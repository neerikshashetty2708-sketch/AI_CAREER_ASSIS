import requests
from bs4 import BeautifulSoup

def get_mock_jobs():
    return [
        {
            "title": "Python Developer",
            "company": "TCS",
            "location": "Bangalore",
            "experience": "0-2 years",
            "salary": "4 LPA"
        },
        {
            "title": "Data Analyst",
            "company": "Infosys",
            "location": "Hyderabad",
            "experience": "1-3 years",
            "salary": "5 LPA"
        },
        {
            "title": "Backend Developer",
            "company": "Wipro",
            "location": "Pune",
            "experience": "2-4 years",
            "salary": "6 LPA"
        }
    ]