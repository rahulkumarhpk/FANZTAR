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
|   |-- test_order_controller.py    # Unit test cases for the order controller/API endpoint.
|-- requirements.txt                # The requirements
|-- README.md                       # The documentation Your Current location


# To clone the repository in your local run the following command

git clone https://github.com/rahulkumarhpk/FANZTAR.git

# Pre-requisites for running the application

1. Python
2. pip
3. POSTMAN


# For installing dependencies paste the command below in terminal

pip install -r requirements.txt

# To run the application run the following command

python app.py

Or

python(ver) app.py e.g python3 app.py

# To run the test cases run the following command

pytest .\tests\test_order_controller.py
