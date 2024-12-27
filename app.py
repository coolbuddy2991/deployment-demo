from flask import Flask, render_template, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

SWAGGER_URL="/docs"
API_URL="/static/swagger.json"
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Deployment Demo"
    }
)

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    
    return "This is about page"

@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "Okay"})

@app.get("/health")
def health():
    return jsonify({"status": "AllGood"}),200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)