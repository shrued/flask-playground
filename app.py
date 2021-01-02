from flask import Flask
app = Flask(__name__)

@app.route("/")
def jeoy():
  return 'How you doin'

@app.route("/<name>")
def name(name):
  return 'Hey ' + name

if __name__ == "__main__":
  app.run(debug=True)