from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# HTML sayfaları
@app.route("/")
def index():
    return render_template("nabi-kimdir.html")

@app.route("/nabi-kimdir")
def nabi():
    return render_template("nabi-kimdir.html")

# Sitemap route'u
@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), "sitemap.xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
