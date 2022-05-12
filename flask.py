from asyncio import tasks
from flask import Flask, jsonify,request

app = Flask(__name__)
tasks = [
    {
        "id":1,
        "contact":u"9987644456",
        "name":u"Raju",
        "done":False
    },
    {
        "id":2,
        "contact":u"9876543222",
        "name":u"Rahul",
        "done":False
    }
]


@app.route("/add-data",methods = ["POST"])

def addtask():
    if not request.json:

       return jsonify({
             "status":"error",
             "messgae":"please provide the data"
    },400)
    task = {
        "id":tasks[-1]["id"]+1,
        "name":request.json["title"],
        "contact":request.json.get("description",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added succesfully"
    })
@app.route("/get-data")
def get_data():
    return jsonify({
        "data":tasks
    })

if __name__ == "__main__":
    app.run()