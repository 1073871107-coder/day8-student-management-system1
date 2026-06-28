import json
def save_data(students):
     with open("students.json","wt",encoding="utf-8") as f:
          json.dump(students,f,ensure_ascii=False,indent=4)

def load_data():
    try:
        with open("students.json","rt",encoding="utf-8") as f:
            result=json.load(f)
            return result
    except:return []
    