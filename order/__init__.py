from flask import Flask
from order.order_controller import order_app

app = Flask(__name__)

app.register_blueprint(order_app)

if __name__ == "__main__":
    app.run(debug=True)
