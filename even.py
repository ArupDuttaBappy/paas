from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    arr = []
    for i in range(2,22,1):
        if (i%2) == 0:
            arr.append(i)
    return a

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    
