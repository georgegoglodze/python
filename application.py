from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello YES SKYNIX World!"

print("Added print")

if __name__ == "__main__":
    app.run()
