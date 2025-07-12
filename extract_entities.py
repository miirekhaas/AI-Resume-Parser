import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)

    education_keywords = ['bachelor', 'master', 'degree', 'b.e', 'btech', 'mtech', 'phd', 'college', 'university']
    education = [line for line in text.split('\n') if any(kw in line.lower() for kw in education_keywords)]

    skills = [token.text for token in doc if token.pos_ == "NOUN" or token.pos_ == "PROPN"]

    return {
        "name": name,
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None,
        "education": education[:3],
        "skills": list(set(skills))
    }
