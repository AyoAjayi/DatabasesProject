from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd

data = pd.read_csv("/Users/ayo/Desktop/DatabasesProject/csv/countries.csv")    #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
country = data["country_name"]
region = data["region"]
country_data = []
region_data = []
for i in country:
    country_data.append((i, i))

for i in region:
    region_data.append((i,i))

class MyForm(FlaskForm):
    query = SelectField('Type', validators = [DataRequired()],
                        choices = [
                            ('0', 'Select a query you are interested in'),
                            ('1', 'Which countries have the highest/lowest population?'),
                            ('2', 'Which region has the highest/lowest population'),
                            ('3', 'What is the relationship between a country/region’s population and GDP?'),
                            ('4', 'What is the GDP per capita in a country'),
                            ('5', 'What is the life expectancy rate per region?'),
                            ('6', 'What is the life expectancy rate of a country over time?'),
                            ('7', 'What states within a country (United States e.g) have the highest life expectancy rate and how does it compare to the rest of the region? Why is this the case?'),
                            ('8', 'What countries GDP has increased/decreased the most across 10years? Has their population size increased/decreased?'),
                            ('9', 'Which countries population has increased/decreased the most across a time period? Why?'),
                            ('10', 'What gender is the most prevalent in each region')
                            ])
                            
    country = SelectField('Type', validators = [DataRequired()],
                        choices = country_data)
    region = SelectField('Type', validators = [DataRequired()],
                        choices = region_data)
    submit = SubmitField("Generate Report")
