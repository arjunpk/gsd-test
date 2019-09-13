import uuid
import json

class Car(object):
    """
    Required params
    :param VIN : VIN(Vehicle Identification Number) of the car

    Optional params
    :param id : Auto generated Unique id
    :param year : Year of the car
    :param make : Make of the car
    :param model : Model of the car
    :param purchase_value : Purchase value of the car in dollars
    :param license_plate_state : State where the car is registered
    :param license_plate_number : License Plate Number of the car
    :param claim_history : List of claims for this car. Each element
        of this list has to be an object of base class Claims

    :method remove_claim_at_index : Remove the claim at a particular
        index from the claim history
        input - index (int)
    :method check_car : checks if the object is an instance of Car
        input - object
        output - boolean
    :method check_car_with_exception : checks if object is an
        instance of Car and raises an exception if not
        input - object
    """
    def __init__(self, vin):
        self.id = uuid.uuid4()
        self.year = None
        self.make = None
        self.model = None
        self.purchase_value = None
        self.vin = vin
        self.license_plate_state = None
        self.license_plate_number = None
        self.__claim_history = []

    @staticmethod
    def check(car):
        if not isinstance(car, Car): return False
        return True

    @staticmethod
    def check_with_exception(car):
        if not Car.check(car):
            raise ValueError('Car object expected')

    @property
    def claim_history(self):
        return self.__claim_history

    @claim_history.setter
    def claim_history(self, claims):
        if isinstance(claim, list):
            for claim in claims:
                self.__insert_claim(claim)
        else: self.__insert_claim(claims)

    def remove_claim_at_index(self, index):
        del(self.__claim_history[index])

    def __insert_claim(self, claim):
        if not issubclass(claim, Claims):
            raise ValueError('Claim object expected')
        self.__claim_history.append(claim)

    def __str__(self):
        return json.dumps({'ID': str(self.id),
            'Year': self.year,
            'Make' : self.make,
            'Model' : self.model,
            'Purchase Value' : self.purchase_value,
            'Vin' : self.vin,
            'License Plate State' : self.license_plate_state,
            'License Plate Number' : self.license_plate_number,
            'Claim History' : self.claim_history}, default=str)

    def __repr__(self):
        return json.dumps(self.__dict__, default=str)

    @staticmethod
    def sort_car_list(cars, key, inplace=False, reverse=False):
        switcher={ 'year' : lambda x: x.year,
            'make': lambda x: x.make,
            'model': lambda x: x.model,
            'purchase_value': lambda x: x.purchase_value,
            'license_plate_state': lambda x: x.license_plate_state,
            'license_plate_number': lambda x: x.license_plate_number,
            'vin': lambda x: x.vin }
        func = switcher.get(key,
            lambda x: (_ for _ in ()).throw(ValueError('Invalid Key')))
        if inplace: cars.sort(key=func, reverse=reverse)
        else: return sorted(cars, key=func, reverse=reverse)

class Claims(object):
    """
    Abstract base class for claim history
    """
    def __init__(self):
        self.company = None

    @staticmethod
    def check(claim):
        if not issubclass(claim, Claims):
            raise ValueError('Claim object expected')

    def __repr__(self):
        return json.dumps(self.__dict__, default=str)

    def __str__(self):
        self.__repr__()

class Fleet(object):
    """
    :param count : Total Number of Cars in this Fleet
    :param count_by_year : A Dictionary containg count of cars by Year
        Access individual counts as follows -
        <Fleet object>.count_by_year[<year>]
    :param total_purchase_price : Total purchase price of all the cars
        in this fleet in dollars

    :method agg : Creates Agregated metrics for a list of cars
        input - list of Car objects
        output - Fleet objects
    """
    def __init__(self, count=0, count_by_year={}, total_purchase_price=0):
        self.count = count
        self.count_by_year = count_by_year
        self.total_purchase_price = total_purchase_price

    def __str__(self):
        return json.dumps({'Total Count' : self.count,
            'Count by Year' : self.count_by_year,
            'Total Purchase Price' : self.total_purchase_price})

    def __repr__(self):
        return json.dumps(self.__dict__, default=str)

    @classmethod
    def agg(cls,cars):
        if not isinstance(cars, list):
            raise ValueError('List object expected')
        count, count_by_year, total_purchase_price = 0, {}, 0
        for car in cars:
            Car.check_with_exception(car)
            count += 1
            count_by_year[car.year] = count_by_year.get(car.year, 0) + 1
            total_purchase_price += car.purchase_value
        return cls(count, count_by_year, total_purchase_price)

class VINIndex(object):
    """
    Creates an Index of Car objects using VIN numbers

    :method get_car_by_vin : fetch a Car object by VIN number
        input - VIN number
        output - Car object
    :method add_car : Add cars to the index
        input - Car object OR list of Car objects
    """
    def init(self):
        self.__index = {}

    def get_car_by_vin(self, vin):
        return self.__index[vin]

    def add_car(self, cars):
        if isinstance(cars, list):
            for car in cars:
                self.__add_car(car)
        else: self.__add_car(cars)

    def __add_car(self, car):
        Car.check_with_exception(cars)
        self.__index[car.vin] = car

    def __repr__(self):
        return json.dumps(self.__dict__, default=str)

    def __str__(self):
        self.__repr__()
