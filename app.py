import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv  # Import the python-dotenv module

load_dotenv()  # Load the environment variables from .env file

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        code_prompt = request.form["text"]  # Changed from "prompt" to "text"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=code_prompt,
            max_tokens=100,
            temperature=0.2
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", translated_code=result)  # Changed "result" to "translated_code"
