from application import app
from flask import render_template
from application.form import MyForm
import mysql.connector



@app.route("/", methods=['GET', 'POST'])
def myapp():
    mydb = mysql.connector.connect(host="localhost", user="root", password="cool1234", database="mydb")
    form = MyForm()
    if form.validate_on_submit():
        mycursor = mydb.cursor()
        country = form.country.data
        region = form.region.data
        print(form.query.data)
        if form.query.data == "1":
            mycursor.callproc("current_country_population", (@a, @b))
        elif form.query.data == "2":
            mycursor.callproc("current_region_population", (@a, @b))
        elif form.query.data == "3":
            mycursor.callproc("current_region_population", (@a, @b))
        elif form.query.data == "4":
            mycursor.callproc("current_region_population", (@a, @b))
        elif form.query.data == "5":
            mycursor.callproc("current_region_population", (@a, @b))
        elif form.query.data == "6":
            mycursor.callproc("current_region_population", (@a, @b))
        else
            mycursor.callproc("current_region_population", (@a, @b))
        for i in mycursor:
            print(i)
    return render_template('index.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)


# from application import app, mo
# from flask import render_template
# from flask_wtf import FlaskForm
# from wtforms import SelectField


# @app.route("/", methods=['GET', 'POST'])
# def myapp():
#     form = Form()


#     return render_template('index.html',form=form)

# if __name__ == "__main__":
#     app.run(debug=True)