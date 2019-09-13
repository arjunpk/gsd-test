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
#### check
Check whether an object is an instance of Car
input - any object
output - A Boolean value representing if the object is an instance of Car

#### check_with_exception
Similar to check method. Raises an exception if object is not instance of Car
input - any object

#### remove_claim_at_index
Removes a claim from the claim history at a particular index. Results in an exception if the index is invalid
input - an integer index

#### sort_car_list
This function was coded to address requirement 5. This function takes a list of cars and sorts it based on the selected key
inputs
 - cars - A list of cars
 - key - property of the car on which the list has to be sorted. A Value Error occurs if an invalid key is provided. Available properties are
	 1. year
	 2. make
	 3. model
	 4. purchase_value
	 5. vin
	 6. license_plate_state
	 7. license_plate_number
- inplace - a boolean value indicating whether the list should be sorted in place. defaults to False
- reverse - a boolean value indicating whether the list should be sorted i descending order

outputs
 - list of cars sorted based on key. none if the list is being sorted inplace 
