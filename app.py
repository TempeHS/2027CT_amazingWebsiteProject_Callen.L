from flask import Flask, render_template 

app = Flask(__name__)

# Homepage for flask
@app.route("/")
def homepage():
  return render_template('index.html')

# Allows directly running of flask program with python3 app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
