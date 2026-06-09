# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json
import os  # ← 추가

app = Flask("JobScraper")

def load_jobs():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # ← 추가
    path = os.path.join(base_dir, "jobs.json")             # ← 추가
    with open("jobs.json", "r") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE
@app.route("/")
def home():
    return render_template("home.html")
 
 
@app.route("/search")
def search():
    keyword = request.args.get("keyword", "").strip()
    jobs = load_jobs()
 
    if keyword:
        results = [
            job for job in jobs
            if keyword.lower() in job["title"].lower()
            or keyword.lower() in job["description"].lower()
            or keyword.lower() in job["company_name"].lower()
        ]
    else:
        results = []
 
    return render_template("search.html", keyword=keyword, jobs=results)
 

# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ← 수정
    app.run(host="0.0.0.0", port=port) #app.run()

# /BLUEPRINT
