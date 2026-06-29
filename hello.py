from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Jenkins +   + modify github src + run + Ngrok + Docker + Flask 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
