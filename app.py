from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Your existing code for solving linear equations

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Process the form data and run your equations solver code
        # Pass the results to the HTML page
        pass
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
