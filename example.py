###############################################################################
# Date: 13 September 2019                                                     #
# Author: Arjun Kishore                                                       #
# This file contains examples and helper methods for classes defined in       #
# solutions.py                                                                #
###############################################################################
from solution import *

import random
import string

#helper method to generate random string
def randomString(n=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))

# helper method to generate a list of cars
def generate_cars(n=15):
    car_list = []
    make_model = [['Ford','F150',65000],['Tesla','Model X', 70000],
        ['Volvo','XC40',48000], ['BMW','M3',120000],['Honda','Civic', 22000],
        ['Toyota','Corolla',28000], ['Hyundai','Sonata',21000]]
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL',
        'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA',
        'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
        'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',
        'VA', 'WA', 'WV', 'WI', 'WY', 'PR']

    for i in range(n):
        # Creating a Car object
        car = Car(randomString(9))
        car.year = random.randint(1970, 2020)
        car.make, car.model, car.purchase_value = \
            make_model[random.randint(0, len(make_model)-1)]
        car.license_plate_state = states[random.randint(0, len(states)-1)]
        car.license_plate_number = randomString(7)
        car_list.append(car)
    return car_list

# Aggregate a list of cars
def create_fleet(n=100):
    return Fleet.agg(generate_cars(n))

#Create an index of cars
def create_index(n=100):
    idx = VINIndex()
    idx.add_car(generate_cars(n))
    return idx

# Sort list by year
def sorter_example_by_year(n=50):
    return Car.sort_car_list(generate_cars(n),'year')

# Sort list by state inplace
def sorter_example_by_state(n=50):
    cars = generate_cars(n)
    Car.sort_car_list(cars,'license_plate_state', True)
    return cars


class ProgressiveClaim(Claims):
    def __init__(self, year):
        super().__init__('Progressive')
        self.claim_year = year

#create car with a claim
def create_car_with_claim():
    car = Car(randomString(9))
    car.claim_history = ProgressiveClaim(2010)
    return car
