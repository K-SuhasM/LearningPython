import requests as re
import json
choice=input("Enter what news do you want ")
url=f"https://newsapi.org/v2/everything?q={choice}&from=2026-06-25&sortBy=publishedAt&apiKey=a46d034499384cb484761944904022a9"

r=re.get(url)
news=json.loads(r.text)
for i in news["articles"]:
    print(i["title"])
    print(i["description"], end="\n")
    print("-------------------------------------------------------------------------------------------")