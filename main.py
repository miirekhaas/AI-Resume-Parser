import json
from extract_text import extract_text_from_pdf
from extract_entities import extract_entities

file_path = "data/sample_resume.pdf"
text = extract_text_from_pdf(file_path)
info = extract_entities(text)

# Save to JSON
with open("outputs/resume_parsed.json", "w") as f:
    json.dump(info, f, indent=4)

print("Extracted info saved to outputs/resume_parsed.json")
