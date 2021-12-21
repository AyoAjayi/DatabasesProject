from application import app
from flask import render_template
from application.form import MyForm
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
# import pandas as pd
# from scipy import stats
import mysql.connector
from flask import jsonify
import json




@app.route("/", methods=['GET', 'POST'])
def myapp():
    form = MyForm()
    if form.validate_on_submit():
        return success(form)
    #     print("YES")
    return render_template('home.html',form=form)

@app.route("/success", methods=['GET', 'POST'])
def success(form):
    mydb = mysql.connector.connect(host="localhost", user="root", password="cool1234", database="mydb")
    mycursor = mydb.cursor()
    country = form.country.data
    region = form.region.data
    print(form.query.data)
    country_name = []
    population = []
    if form.query.data == "1":
        args = (0, 0)
        result = mycursor.callproc('current_country_population', args)
        highest = result[0]
        lowest = result[1]
        query = "SELECT country_name, population FROM Country INNER JOIN Population ON Population.country=Country.country_code WHERE year = '2019'"
        mycursor.execute(query)
        for i in mycursor:
            country_name.append(i[0])
            population.append(i[1])
        print(country_name)
        return render_template('layout.html', country_name=country_name, population=population, highest=highest, lowest=lowest)
    elif form.query.data == "2":
        args = (0, 0)
        result = mycursor.callproc("current_region_population",args)
        # query = "SELECT region, SUM(population) AS total_population FROM Country INNER JOIN Population WHERE year = '2019' GROUP BY region"
        # mycursor.execute(query)
        # for i in mycursor:
        #     country_name.append(i[0])
        #     population.append(i[1])
        region = []
        population = []
        actualPop = []
        for result in mycursor.stored_results():
            data = result.fetchall()
        print(data)
        for i in range(len(data)):
            region.append(data[i][0])
            population.append(data[i][1])
        for i in population:
            actualPop.append(float(i))
        print(actualPop)
        print(region)
        return render_template('layout_two.html', region=region, actualPop=actualPop)
    elif form.query.data == "3":
        population = []
        gdp = []
        res = []
        country = form.country.data
        #Change the procedure name to the one that we chose in procedure file when you run code
        result = mycursor.callproc('y', (country,))
        for result in mycursor.stored_results():
            data = result.fetchall()
        print(data)
       
        for i in range(len(data)):
            res.append({"x": data[i][1],
                        "y": data[i][2]})
        for i in data:
            population.append(i[1])
        for i in data:
            gdp.append(i[2])
        r = calculateValue(population,gdp)
        return render_template('layout_three.html', res=res, r=r)
    elif form.query.data == "4":
        country = form.country.data
        result = mycursor.callproc('current_within_GDP', (country,))
        for result in mycursor.stored_results():
            data = result.fetchall()
        if len(data) == 2:
            country = data[0][1]
            GDP = data[0][2]
        else:
            country = form.country.data
            GDP = "blank. There is no available GDP for " + country + "."
        print(data)
        return render_template('layout_four.html', country=country, GDP=GDP)
    elif form.query.data == "5":
        mycursor.callproc("current_region_population")
    elif form.query.data == "6":
        year = []
        expectancy = []
       
        country = form.country.data
        result = mycursor.callproc('country_life', (country,))
        for result in mycursor.stored_results():
            data = result.fetchall()
        print(data)
       
        
        for i in range(len(data)):
            year.append(data[i][0])
            expectancy.append(data[i][1])
        print(year)
        print(expectancy)

        
    
        return render_template('layout_five.html',year=year, expectancy=expectancy)




    else:
        return True
    return True


def calculateValue(x,y):
    x = np.array(x).reshape((-1, 1))
    y = np.array(y)

    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_)
    y_pred = model.predict(x)


    # plt.scatter(x,y, color = "red")
    # plt.plot(x, y_pred, color="blue", linewidth=3)
    # plt.title("Population vs GDP")
    # plt.xlabel("Population")
    # plt.ylabel("GDP")
    # plt.show()

    return round(r_sq*100)



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