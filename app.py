import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, jsonify
from scipy.sparse import hstack

# Load model and preprocessing tools
with open('model_v2.pkl', 'rb') as f:
    data = pickle.load(f)
    model = data['model']
    tfidf = data['tfidf']
    education_encoder = data['education_encoder']
    career_encoder = data['career_encoder']

app = Flask(__name__)

@app.route('/')
def home():
    return "Career Recommendation System API is live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs
        age = int(request.form.get('age'))
        skills = request.form.get('skills')  # e.g. "Python;Machine Learning"
        interests = request.form.get('interests')  # e.g. "AI;Data Science"
        education = request.form.get('education')  # e.g. "Bachelor's"

        # Preprocess input
        text = skills.replace(';', ' ') + ' ' + interests.replace(';', ' ')
        text_tfidf = tfidf.transform([text])
        edu_encoded = education_encoder.transform([education])[0]
        numeric_features = np.array([[age, edu_encoded]])
        input_features = hstack([text_tfidf, numeric_features])

        # Predict
        pred_class = model.predict(input_features)[0]
        career = career_encoder.inverse_transform([pred_class])[0]

        return jsonify({'recommended_career': career})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
