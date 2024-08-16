from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/first/hello")
def hello_world():
    return jsonify(message="Hello Wold")


@app.route("/first/list")
def hello_list():
    fruits = ['apple', 'banana', 'cherry', 'orange']
    return jsonify(fruits)


@app.route("/first/map")
def hello_map():
    map = {'id': 1, "username": 'jai', "email": "jai@email.com"}
    return jsonify(map)



@app.route("/first/health", methods=['GET'])
def health_check():
    return jsonify(message="OK")


if __name__ == '__main__':
    app.run(debug=False)
