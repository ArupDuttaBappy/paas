from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    
    X = [[1,2,3],
        [3,2,1],
        [1,2,3]]
    
    Y = [[4,5,6],
        [6,5,4],
        [4,6,5]]
    
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    for i in range(len(X)):
     for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
    return result

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
