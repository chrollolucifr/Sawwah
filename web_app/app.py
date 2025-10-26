from flask import Flask, render_template, request, jsonify
import requests, base64, io

app = Flask(__name__)

# رابط ngrok الخاص بـ Colab
COLAB_API_BASE = "https://millicent-hypogynous-basally.ngrok-free.dev"

# -------- الصفحات الأساسية -------- #
@app.route("/")
def about():
    return render_template("about.html")

@app.route("/why")
def why():
    return render_template("why.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/data")
def data():
    return render_template("data.html")


# -------- الربط مع Colab Model -------- #
@app.route("/ask", methods=["POST"])
def ask_text():
    data = request.get_json()
    user_text = data.get("text", "")
    if not user_text:
        return jsonify({"error": "No text provided"}), 400

    try:
        resp = requests.post(f"{COLAB_API_BASE}/ask", json={"text": user_text}, timeout=60)
        data = resp.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/voice", methods=["POST"])
def voice():
    audio_file = request.files.get("audio_file")
    if not audio_file:
        return jsonify({"error": "No audio file uploaded"}), 400

    files = {"audio": (audio_file.filename, audio_file.stream, audio_file.mimetype)}
    try:
        resp = requests.post(f"{COLAB_API_BASE}/voice", files=files, timeout=120)
        data = resp.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

