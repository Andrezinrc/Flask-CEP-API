from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = {}

    if request.method == "POST":
        cep = request.form.get("cep")
        api_url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(api_url)
            data = response.json()
        except Exception as e:
            print(f"Nao foi possivel acessar a API: {e}")

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()
