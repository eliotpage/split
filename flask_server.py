from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = "map_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_shapes")
def get_shapes():
    return jsonify(load_data())

@app.route("/add_shape", methods=["POST"])
def add_shape():
    data = load_data()
    new_shape = request.json
    data.append(new_shape)
    save_data(data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
