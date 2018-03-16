from flask import Flask, render_template, request
from instagram import Instagram

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index(url=None, error=None, media=None):

    if request.method == 'POST':
        try:
            data = Instagram(request.form["url"])
            media = data.get_download_url()
        except Exception as e:
            error = e

    return render_template("index.html", method=request.method, url=url, error=error, media=media)


if __name__ == "__main__":
    app.run()
