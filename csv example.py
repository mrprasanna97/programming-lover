import csv

with open("books.csv","w", newline="")as f:
  writer=csv.writer(f)
  writer.writerow(["title","author","year"])
  writer.writerow(["money and power","sunil sasthiri",1998])
  writer.writerow(["power of politics","zig ziglar",2003])
  writer.writerow(["welcome to python","sakthi kumar",2008])
with open("books.csv","r")as f:
  reader=csv.DictReader(f)
  for row in reader:
    if row["year"]<"2000":
     print(row["title"].upper()," BY ",row["author"].upper(),(row["year"]))

    