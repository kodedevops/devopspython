from flask import Blueprint, Flask, jsonify

app = Flask(__name__)
first_bp = Blueprint('firstbp', __name__, url_prefix='/python-service/first')

@first_bp.route("/")
def hello_default():
    return jsonify(message="Hello Wold")


@first_bp.route("/hello")
def hello_world():
    return jsonify(message="Hello Wold")


@first_bp.route("/list")
def hello_list():
    fruits = ['apple', 'banana', 'cherry', 'orange']
    return jsonify(fruits)


@first_bp.route("/map")
def hello_map():
    map = {'id': 1, "username": 'jai', "email": "jai@email.com"}
    return jsonify(map)



@first_bp.route("/health", methods=['GET'])
def health_check():
    return jsonify(message="OK")

# Register the blueprint in the app
app.register_blueprint(first_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
