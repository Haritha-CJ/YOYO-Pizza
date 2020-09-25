from mysql.connector import connect, errorcode, Error


def ConnectMySql():
    try:
        mydatabase = connect(
            host="localhost", user="root", password="root", database="Yoyo_pizza_details",
        )
        return mydatabase
    except Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return False
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return False
        else:
            print(e)
            return False
