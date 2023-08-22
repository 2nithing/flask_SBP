from flask import Flask, render_template, request
import predict_sbp


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
        age = request.form['age']
        SBP = predict_sbp.prediction(int(age))
        return render_template('index.html',age=age, SBP=SBP)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)