from functools import wraps
import json
from flask import Blueprint, request, jsonify
from parts_pricing.parts_pricing import parts_data, price_data
import random

order_app = Blueprint("order_app", __name__)


# Custom decorator for order validation
def validate_order(func):
    """Custom decorator for order validation"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            components_list = request.args.get("components")
            components_list = json.loads(components_list)

            if len(components_list) > 5:
                return (
                    jsonify(
                        {
                            "error": "Invalid order. You are trying to order more components."
                        }
                    ),
                    400,
                )
            elif len(components_list) < 5:
                return (
                    jsonify(
                        {
                            "error": "Invalid order. You have ordered less components than required."
                        }
                    ),
                    400,
                )
            category_counts = {"Screen": 0, "Camera": 0, "Port": 0, "OS": 0, "Body": 0}

            for component in components_list:
                part = parts_data.get(component, "")
                if part != "":
                    for category in category_counts.keys():
                        if category in part:
                            category_counts[category] += 1

            if all(count == 1 for count in category_counts.values()):
                return func(*args, **kwargs)
            else:
                return (
                    jsonify(
                        {"error": "Invalid order. Each category should have one part."}
                    ),
                    400,
                )

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return wrapper


@order_app.route("/orders", methods=["POST"])
@validate_order
def create_order():
    """API to create a new order"""
    try:
        components = request.args.get("components")
        components_list = json.loads(components)
        total_price = 0
        ordered_parts = []

        for component in components_list:
            price = price_data.get(component, 0)
            part = parts_data.get(component, "")

            if price > 0 and part != "":
                total_price += price
                ordered_parts.append(part)

        # Creating orderids
        order_id = random.randint(1000, 99999)

        response_data = {
            "order_id": order_id,
            "total": total_price,
            "parts": ordered_parts,
        }

        return jsonify(response_data), 201

    except Exception as e:
        # returning if any error occurs
        return jsonify({"error": str(e)}), 400
