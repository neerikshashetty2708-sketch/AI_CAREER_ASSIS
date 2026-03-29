def career_advice(text):
    if "python" in text.lower():
        return "You should apply for Python Developer roles"
    elif "data" in text.lower():
        return "You should explore Data Analyst roles"
    else:
        return "Improve skills in programming + projects"