from application import app
from flask import render_template
@app.route("/")
def myapp():
    return render_template('index.html', title = 'index')

if __name__ == "__main__":
    app.run(debug=True)
