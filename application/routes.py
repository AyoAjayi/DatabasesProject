from application import app
from flask import render_template
from application.form import MyForm
import mysql.connector



@app.route("/", methods=['GET', 'POST'])
def myapp():
    mydb = mysql.connector.connect(host="localhost", user="root", password="DA25wn!*", database="final_project")
    form = MyForm()
    if form.validate_on_submit():
        mycursor = mydb.cursor()
        country = form.country.data
        region = form.region.data
        print(form.query.data)
        if form.query.data == "1":
            args = (0, 0)
            result = mycursor.callproc('current_country_pop', args)
            print (result[0])
            query = "SELECT country_name, population FROM Country INNER JOIN Population ON Population.country=Country.country_code WHERE year = '2019'"
            mycursor.execute(query)
            for i in mycursor:
                print(i)
        elif form.query.data == "2":
            mycursor.callproc("current_region_population")
        elif form.query.data == "3":
            mycursor.callproc('')
        elif form.query.data == "4":
            mycursor.callproc("current_region_population")
        elif form.query.data == "5":
            mycursor.callproc("current_region_population")
        elif form.query.data == "6":
            mycursor.callproc("current_region_population")
        else:
            mycursor.callproc("current_region_population")
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