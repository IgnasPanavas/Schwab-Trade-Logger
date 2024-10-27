from datetime import datetime, timedelta
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/historical/account-balance')
def get_account_balance_values():

    # Generate example dates for the past week
    today = datetime.now()
    dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)][::-1]  # Reverse to have ascending order

    # Example account balance data for each date
    account_balances = [1000, 1050, 1025, 1100, 1150, 1125, 1200]

    # Data structure for Chart.js
    data = {
        "labels": dates,  # Dates as x-axis labels
        "data": account_balances,  # Account balances as y-axis data points
    }

    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True, port=5000)