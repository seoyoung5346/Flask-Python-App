# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")

import os

def load_jobs():
    # main.py 파일 기준으로 절대 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "jobs.json")
    with open(file_path, "r", encoding="utf-8") as f:
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
    app.run()

# /BLUEPRINT
