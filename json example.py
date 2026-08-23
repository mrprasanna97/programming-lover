import json
student={"name":"prasanna","age":19,"course":"cse"}
with open("student.json","w")as f:
    json.dump(student,f)
with open("student.json","r")as f:
    b=json.load(f)

print(b["name"])