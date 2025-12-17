from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to home page"

@app.route("/product")
def products():
    return "this is product page"

if __name__ == "__main__":
    app.run(debug=True)
