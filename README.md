# 📊 Social Network Ad Conversion Prediction (Django + ML)

A Machine Learning powered web application that predicts whether a user will purchase a product after seeing a social media advertisement.

The model is trained using **scikit-learn** and deployed using a **Django web application** with a clean user interface.
Users can enter details like age and salary, and the system predicts if the ad will convert into a purchase.

---

## 🚀 Live Demo

🔗 [https://ml-project-college.onrender.com](https://ml-project-college.onrender.com)

---

## 🧠 Machine Learning Model

* Algorithm: Logistic Regression
* Library: Scikit-Learn
* Output: Probability (0–1)
* Decision Rule:

  * **≥ 0.5 → YES (Will Buy)**
  * **< 0.5 → NO (Will Not Buy)**

The trained model and scaler are saved using pickle:

```
model.pkl
scaler.pkl
```

---

## 🛠 Tech Stack

**Backend**

* Python
* Django
* Gunicorn

**Machine Learning**

* NumPy
* Pandas
* Scikit-Learn
* Pickle

**Frontend**

* HTML
* CSS
* Bootstrap

**Deployment**

* Render

---

## 📂 Project Structure

```
COLLEGE-ML-PROJECT
│
├── predictor/
│   ├── views.py
│   ├── urls.py
|   ├── model.pkl
|   ├── scaler.pkl
│
├── Social_Network_Ad_Conversion_Prediction/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── templates/
│   └── predict.html
│
├── requirements.txt
├── start.sh
├── build.sh
└── manage.py
```

---

## ⚙️ How It Works

1. User enters Age & Estimated Salary
2. Django receives input
3. Data is scaled using saved scaler
4. Model predicts probability
5. If probability ≥ 0.8 → YES else NO
6. Result displayed on webpage

---

## 💻 Run Locally

Clone repo:

```
git clone https://github.com/your-username/your-repo-name.git
cd COLLEGE-ML-PROJECT
```

Create virtual environment:

```
python -m venv env
env\\Scripts\\activate   (Windows)
source env/bin/activate (Mac/Linux)
```

Install dependencies:

```
pip install -r requirements.txt
```

Run server:

```
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📌 Features

* Real-time ML prediction
* Clean form-based UI
* Django backend integration
* Model persistence using pickle
* Production deployment using Gunicorn + Render

---

## 🎯 Future Improvements

* Add more features for prediction
* Improve UI design
* Add user authentication
* Store prediction history in database

---

## 👨‍💻 Author

**Atanu Maity**

AI & Backend Developer (Aspiring)
