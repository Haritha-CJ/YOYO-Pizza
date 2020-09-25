from flask import jsonify


def response(data, msg):
    data = {}
    data_list = []
    try:
        for i in data:
            temp = {}
            temp["reg_no"] = i[0]
            temp["name"] = i[1]
            temp["address"] = i[2]
            data_list.append(temp)
            data["data"] = data_list

        data["msg"] = msg
        print(f"Respone data : {data}")
        return jsonify(data)
    except IndexError as e:
        print(e)
        return str(e)

