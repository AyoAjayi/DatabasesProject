from application import app
# from flask.ext.mysql import MySQL

# mysql = MySQL()



 
if __name__ == "__main__":
    # MySQL configurations
    # app.config['MYSQL_DATABASE_USER'] = 'jay'
    # app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
    # app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    # app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    # mysql.init_app(app)

    # conn = mysql.connect()
    # cursor = conn.cursor()
    app.run(debug=True)