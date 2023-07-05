from flask import Flask, request, jsonify

app = Flask(__name__)

# route() here is a decorator (html) that tells Flask what URL should TRIGGER the function.
# in this case, going to the /test route will trigger the test() function.
# methods here specigies which HTTP methods are allowed. The default is GET only.
@app.route('/test', methods=['POST', 'GET'])

def test():
    if request.method == 'POST':
        return jsonify({'msg': 'POST method'})
    else:
        return jsonify({'msg': 'GET method'})

# for logging purposes only; it does not show on the website
@app.before_request
def before():
    print("This is executed BEFORE each request.")

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name
    
# ensures that the app only runs when it is executed in the main file and not when it is imported
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9988)