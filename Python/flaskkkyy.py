from flask import Flask

# 1. Create the app
app = Flask(__name__)

# 2. Define the route (The URL)
# This means: When someone goes to the homepage ('/')...
@app.route('/')
def home():
    # 3. Run this function and send the text back to the browser
    return "Yo, this is my website!"

# 4. Run the app
if __name__ == '__main__':
    app.run(debug=True)