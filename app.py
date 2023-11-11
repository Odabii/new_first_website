from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder= "template")


@app.route ("/")
def Hello_world():
  return render_template ("home.html")

@app.route ("/staffs")
def staffs_officiele():
  return jsonify (render_template ("pos.html"))

if __name__ == "__main__":
  app.run (host= "0.0.0.0", debug = True)