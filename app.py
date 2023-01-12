from flask import Flask, jsonify, request

app = Flask(__name__)

Users = []

@app.route('/Users/')
def get_Users():
    return jsonify(Users)


@app.route('/Users/', methods=['POST'])
def add_Users():
    Users.append(request.get_json())
    return 'Post Request Send Successfully -/'


if __name__ == '__main__':
    app.run(debug=True)
