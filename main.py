from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/x")
def x():
  return render_template("index.html")

@app.route("/y")
def y():
  return render_template("y.html")

@app.route("/z")
def z():
  return render_template("z.html")

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = random.randint(2000,9000))