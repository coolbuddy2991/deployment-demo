from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    
    return "This is about page"

@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "Okay"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)