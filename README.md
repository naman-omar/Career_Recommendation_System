# Career Recommendation System 🎯

A machine learning-based Career Recommendation System that helps students or individuals identify suitable career paths based on their interests and skillsets. This project uses the Random Forest algorithm with hyperparameter tuning to enhance prediction accuracy.

## 🚀 Features

- Predicts the most suitable career option based on user inputs.
- Built using the Random Forest algorithm.
- Hyperparameter tuning for improved model accuracy.
- Web interface and Android APK available for user interaction.
- Classification report and accuracy score generated for performance evaluation.

## 📊 Model Details

- **Algorithm Used:** Random Forest Classifier
- **Technique:** Hyperparameter tuning (GridSearchCV)
- **Accuracy:** 92.1%
- **Evaluation Metrics:** Classification Report (Precision, Recall, F1-score)

## 🛠️ Tech Stack

- Python
- scikit-learn
- Pandas, NumPy
- Kotlin (for Android App)
- Google Colab (for model development)

## 🔗 Important Links

- **GitHub Repository:** [Career_Recommendation_System](https://github.com/naman-omar/Career_Recommendation_System)
- **Android APK:** [Download APK](https://drive.google.com/file/d/1Qk5dKeFY2bpgAik_Uai30ird8rXb4z5i/view?usp=sharing)

## 🔍 How It Works

1. User provides scores and interests through a form.
2. The model predicts the most suitable career based on the trained data.
3. Hyperparameters like `n_estimators`, `max_depth`, and `min_samples_split` were tuned using GridSearchCV.
4. The final model gives accurate career recommendations with minimal overfitting.

## App.py file description 
1. This Flask API loads a machine learning model and encoders from a pickle file to recommend careers based on user input.
2. It accepts POST requests at the /predict endpoint with inputs like age, skills, interests, and education.
3. The inputs are preprocessed (TF-IDF + encoded features), fed into the model, and the predicted career is returned as a JSON response.

## 




