# Take home Test
*Python Version = 3.5.6*

This repository has 2 python files.
1. solution.py - This file contains the Data Structures designed to address the requirements
2. example.py - This file provides examples/helper functions to demonstrate the usage of the Data Structures and methods in solution.py

# solution.py

## Car

This class holds details of a single Car
### Fields
- id - An auto generated unique id
- year - The year the car was manufactured
- make - The Make of the car
- model - The model of the car
- purchase_value - The purchase value of the car in dollars
- license_plate_state - The US state where this car is registered
- license_plate_number - The license plate number of the car
- claim_history - A list which holds the claims for this car Each element of this list has to be an object of the base class Claims

### Methods
#### check_car
input - any object
output - A Boolean value representing if the object is an instance of Car
