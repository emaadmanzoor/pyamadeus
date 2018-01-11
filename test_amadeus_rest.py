#!/usr/bin/env python

from amadeus import Flights
from constants import *
import sys

if __name__ == "__main__":
    if len(API_KEY) == 0:
        raise Exception("Obtain an API key from sandbox.amadeus.com and store it in constants.py")
        sys.exit()


    print "Flight search:"
    flights = Flights(API_KEY)
    resp = flights.inspiration_search(
        origin='BKK',
        departure_date="2018-03-25--2018-03-30",
        max_price=200)
    print resp
