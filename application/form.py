from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd

data = pd.read_csv("/Users/michiko/Developer/CS315/DatabasesProject/csv/countries.csv")    #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
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
                            ('2', 'Which region has the highest/lowest population?'),
                            ('3', 'What is the relationship between a country/region’s population and GDP?'),
                            ('4', 'What is the GDP per capita within a region?'),
                            ('5', 'What is the average life expectancy rate of a region over time?'),
                            ('6', 'What is the life expectancy rate of a country over time?'),
                            ('7', 'What countries within a region have the highest life expectancy rate and how does it compare to the rest of the region?'),
                            ('8', 'What countries GDP has increased/decreased the most across 20 years?'),
                            ('9', 'Which countries population has increased/decreased the most across 20 years?'),
                            ('10', 'What is the GDP per capita of a country over time?'),
                            ('11', 'What is the average life expectancy rate in a region and how does it compare to GDP over time?')
                            ])
                            
    country = SelectField('Type', validators = [DataRequired()],
                        choices = country_data)
    region = SelectField('Type', validators = [DataRequired()],
                        choices = region_data)
    submit = SubmitField("Generate Report")
