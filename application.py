from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello YES SKYNIX World!"

def printer(text):
    return text

print("function completed")

if __name__ == "__main__":
    app.run()
