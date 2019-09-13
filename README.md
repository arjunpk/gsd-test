The file solutions.py contains data structures designed to address the requirements. Details on the individual classes can be found in README(detailed).md

1. Requirement 1a : Car - This data structure holds information for a single car. An id field is automatically generated and the VIN number is mandatory field. Instantiate this as follows:
	``` python
	  car = Car('vinnumber')
	```
	- Claim history is stored as a list. This list will only accept objects which are inherited from the base class Claims
2. Requirement 1b: Claims - This is an abstract class which designed to form a base for Claims from different companies. Create a new claims class for each company by extending the Claims class
	```python
	class AllStateClaims(Claims):
		def __init__(self):
			super().__init__(self, 'AllState')
			self.attribute1 = None
	```

3. Requirement 2 and 3: Fleet - This class holds aggregated metrics for Fleet. This class has a classmethod -agg which returns an instance of the fleet class with data aggregated for input list of Cars
	``` python
	 fleet = Fleet.agg(cars_list)
	```
4. Requirement 4: VINIndex - This class holds an index of cars. The index is stored as a dictionary and hence provides O(1) lookups
	- Use the `add_car` method to add a list of cars or an individual car.
	- Use the `get_car_by_vin` method to get an individual car based on a VIN number. This method returns a null if there is no car with a matching VIN in the index
	``` python
	idx = VINIndex()
	# add a list of cars
	idx.add_car(cars_list)
	# add an individual car
	idx.add_car(car)
	# retreive a car by VIN number
	car = idx.get_car_by_vin('vin number') 
