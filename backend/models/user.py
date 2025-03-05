from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    budgets = db.relationship('Budget', backref='user', lazy=True)
    expenses = db.relationship('Expense', backref='user', lazy=True)

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Rotas
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    user_id = data.get('user_id')

    user = User.query.get(user_id)
    if not user:
        return jsonify({"response": "Usuário não encontrado."})

    if "quanto gastei" in user_message.lower():
        category = user_message.lower().split("com ")[1].split(" este mês")[0]
        expenses = Expense.query.filter_by(user_id=user_id, category=category).all()
        total = sum(expense.amount for expense in expenses)
        response = f"Este mês, você gastou R$ {total:.2f} com {category}."
    elif "meta de economizar" in user_message.lower():
        budgets = Budget.query.filter_by(user_id=user_id).all()
        total_budget = sum(budget.amount for budget in budgets)
        expenses = Expense.query.filter_by(user_id=user_id).all()
        total_expenses = sum(expense.amount for expense in expenses)
        remaining = total_budget - total_expenses
        response = f"Faltam R$ {remaining:.2f} para atingir sua meta de R$ {total_budget:.2f}."
    else:
        response = "Desculpe, não entendi. Como posso ajudar?"

    return jsonify({"response": response})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)