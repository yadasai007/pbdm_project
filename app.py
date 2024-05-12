from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import random
app = Flask(__name__)

# Load your trained modelp
model = load_model('my_model.keras')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=="GET":
        return render_template("predict.html")
    if request.method=="POST":
        # Get data from request
        search_input = request.form['search']
        search_input=float(search_input)/172788
        # Create input array for prediction
        data = np.array([[search_input]+[round(random.uniform(0, 1), 6)]*29])  # Repeat the input 30 times to match the expected input shape
        
        # Perform inference with your model
        prediction = model.predict(data)

        prediction=round(prediction[0][0],2)        
        print(prediction)
        # Return prediction as JSON
        if prediction==0.0:
            return jsonify({'prediction': "Transaction at this time is not Fraud"})
        else:
            return jsonify({'prediction': "Transaction at this time Fraud"})

if __name__ == '__main__':
    app.run(debug=True)
