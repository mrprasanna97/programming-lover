import requests

response=requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code==200:
    users=response.json()
    for user in users:
        print(user["name"],user["address"]["city"])
        
else:
    print("failed",response.status_code)



#IT WORK ONLY WHEN THE INTERNET IS ON .....