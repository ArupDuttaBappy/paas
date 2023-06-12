from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    numbers = [1,2,12,13,33]
    numbers.sort()
    return "2nd largest number from the given list is "+ str(numbers[1])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
