# FANZTAR Mobile Factory App Assignment

This repository contains a Flask application simulating API for creating orders of configurable mobiles.

## Project Structure

FANZTAR/
|-- order/
|   |-- __init__.py                 # An empty file that marks the directory as a package.
|   |-- order_controller.py         # The order controller
|-- data/
|   |-- parts_pricing.py            # The parts and their price information
|-- tests/
|   |-- __init__.py                 # An empty file that marks the directory as a package.
|   |-- test_order_controller.py    # Unit test cases for the order controller to make sure the API is working properly.
|-- requirements.txt                # The requirements
|-- README.md                       # The documentation Your Current location


# For installing dependencies paste the command below in terminal

pip install -r requirements.txt

# To run the application run the following command

python app.py

# To run the test cases run the following command

pytest .\tests\test_order_controller.py