from flask import Flask, render_template, request 
import pickle
app=Flask(__name__)

@app.route('/') 
def home():
    return render_template('home.html')
@app.route('/predict')
def index() :
    return render_template("index.html")

@app.route('/data_predict', methods=['GET','POST']) 
def predict():
    
    model = pickle.load(open('wineQuality_new.pkl', 'rb'))
 
    data = [[x for x in request.form.values()]]    
    
    pred= model.predict(data)[0]
    print(pred)
    if pred==0:
        prediction="Bad"
    else:
        prediction="Good"
    
    return render_template('pred.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)