from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return 'How you doin'

if __name__ == "__main__":
  app.run()