from flask import Flask, abort, jsonify, request

fakedb = {}

app = Flask(__name__)

@app.route('/users/<name>')
def get_user_by_name(name):
    user_data = fakedb.get(name)
    if not user_data:
        abort(404)
    response = jsonify(**user_data)
    app.logger.debug('get user for %s returns data:\n%s', name, response.data)
    return response

@app.route('/_pact/provider_states', methods=['POST'])
def provider_states():
    return jsonify({'result': request.json['state']})

def setup_user_a():
    fakedb['UserA'] = {'name': "UserA"}

if __name__ == '__main__':
    setup_user_a()
    app.run(debug=True, host="0.0.0.0", port=50010)
