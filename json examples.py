import json
student={"name":"prasanna","age":19,"course":"cse"}
with open("student.json","w")as f:
    json.dump(student,f)
with open("student.json","r")as f:
    c=json.load(f)

print(c["course"])