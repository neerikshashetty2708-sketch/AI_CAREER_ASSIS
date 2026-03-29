def match_jobs(resume_text, jobs):
    matched = []

    for job in jobs:
        score = 0

        if job["title"].lower() in resume_text.lower():
            score += 50

        if job["location"].lower() in resume_text.lower():
            score += 20

        matched.append({**job, "score": score})

    return sorted(matched, key=lambda x: x["score"], reverse=True)