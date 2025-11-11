from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for stocks (simulating a database)
stocks_db = {}

def buy_function(stock_name):
    # Placeholder function to simulate buying stock.
    # Replace this with actual logic when integrating with a real database or service.
    if stock_name in stocks_db:
        stocks_db[stock_name] += 1
    else:
        stocks_db[stock_name] = 1
    return f"Bought {stocks_db[stock_name]} shares of {stock_name}"

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    data = request.get_json()
    stock_name = data['stock_name']
    quantity = int(data['quantity'])

    # Simulate buying the stock by calling the buy_function with the stock name
    result = buy_function(stock_name)

    return jsonify({"status": "success", "message": result})

if __name__ == '__main__':
    app.run(debug=True)