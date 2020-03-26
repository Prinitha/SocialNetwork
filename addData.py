from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def func():
    # if request.method == "GET":
    #     pass
    # if request.method == "POST":
    #     id = request.get("id")
    #     name = request.get("name")
    #     content = request.get("content")
    #
    #
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
