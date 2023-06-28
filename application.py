from flask.helpers import flash
from web import result
from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('komoditas.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    if 'b' == 'sawah' or 'Sawah':
        data3 = 0
    else:
        data3 = 2
    arr = np.array([[data1, data3]])
    pred = model.predict(arr)
    
    return render_template('index1.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
