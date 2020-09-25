from flask import Flask, request, jsonify
import MysqlConnect as connect
import GenerateResponse as res
import Error as err

app = Flask(__name__)


@app.route("/fetch", methods=["get", "post"])
def fetch():
    conn = connect.ConnectMySql()
    print(f"Connection status : {conn}")

    if conn is False:
        return err.ReturnConnectionError()
    else:
        try:
            cur = conn.cursor()
            print(f"Cursor object : {cur}")
            query = "select * from Pizza_det"
            cur.execute(query)
            msg = "Data fetched succesfully"
            return jsonify(
                {"fulfillmentMessages": [{"text": {"text": ["hello world"]}}]}
            )
        except Exception as e:
            print(e)
            return err.ReturnFetchError()
        finally:
            conn.close()


@app.route("/insert", methods=["post"])
def insertData():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=3000)

