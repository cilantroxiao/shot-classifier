import json
with open("training_labels_raw.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned = []

for item in data:
    file_name = item["still"].replace("/data/upload/1/", "")
    clean_name = file_name.split("-", 1)[-1]
    cleaned.append({
        "id" : item["id"],
        "file_name" : clean_name,
        "shot_type" : item["shot_type"]
    })

with open("training_labels_clean.json", "w") as f:
    json.dump(cleaned, f, indent=2)
