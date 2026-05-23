skills_list = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "data analysis",
    "data visualization",
    "communication",
    "pandas",
    "numpy",
    "statistics",
    "deep learning",
    "nlp",
    "html",
    "css",
    "javascript"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))