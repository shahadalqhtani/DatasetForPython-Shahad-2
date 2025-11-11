bash
pip install flask
import yaml
from flask import Flask, request, Response

app = Flask(__name__)

# Dummy function to simulate fetching a price based on product code
def get_price_for_product_code(product_code):
    # In a real application, this would query a database or an external API.
    prices = {
        "A123": 10.00,
        "B456": 15.00,
        "C789": 20.00,
    }
    return prices.get(product_code, None)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    # Get the YAML payload from the query parameter
    yaml_payload = request.args.get('payload')

    if not yaml_payload:
        return Response("Error: Payload is required.", status=400)

    try:
        # Load the YAML payload into a dictionary
        payload = yaml.safe_load(yaml_payload)

        # Extract product code and quantity from the payload
        product_code = payload.get('product_code')
        quantity = payload.get('quantity', 1)  # Default to 1 if not provided

        if not product_code:
            return Response("Error: Product code is required.", status=400)

        # Get the price for the product code
        price = get_price_for_product_code(product_code)

        if price is None:
            return Response("Error: Invalid product code.", status=400)

        # Calculate total price
        total_price = price * quantity

        # Return the result in YAML format
        response_payload = {
            "total_price": total_price,
            "product_code": product_code,
            "quantity": quantity,
            "unit_price": price
        }

        return Response(yaml.dump(response_payload), content_type='text/yaml')

    except yaml.YAMLError as exc:
        return Response(f"Error parsing YAML: {exc}", status=400)

if __name__ == '__main__':
    app.run(debug=True)