from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/chat')
def chat():
    return render_template('chat.html')

@main.route('/predict')
def predict():
    return render_template('prediction.html')

@main.route('/treatment')
def treatment():
    return render_template('treatment.html')
