from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': "Data Analyst",
    'location': "Bangluru",
    'salary':'100000 rs',    
    },
    {
    'id': 2,
    'title': "Data scientist",
    'location': "Mumbai",
    'salary':'150000 rs'    
    },
    {  
    'id': 3,
    'title': "Data Engineer",
    'location': "Bangluru",   
    },
    {
    'id': 4,
    'title': "Backend engineer",
    'location': "remote",
    'salary':'105000 rs'    
    }
  ]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs = JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run('0.0.0.0',debug = True)