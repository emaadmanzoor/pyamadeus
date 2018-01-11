#!/usr/bin/env python

import base64
from constants import *
import datetime
import pprint
import xmltodict
import zeep
#import log # uncomment to print debugging logs

pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":

    client = zeep.Client(wsdl=OAG_WSDL, strict=False)

    # set up header and login details
    header = {"Host": "status.oag.com",
              "Content-Type": "text/xml; charset=utf-8",
              "SoapAction": ""}
    client.transport.session.headers = header
    logindetails = {"username": OAG_USERNAME, "password": OAG_PASSWORD}

    with client.options(raw_response=True):
        resp = client.service.getFlights({
            "flightsQueryWSVO": {
                "fromDate": datetime.datetime.strptime("2011-01-10", "%Y-%m-%d"),
                "plusMinusaDay": True,
                "airlineCode": "BA",
                "depAptCode": "LHR",
                "arrAptCode": "DEL"
                },
            "loginDetailsVO": logindetails
            })

        resp_dict = xmltodict.parse(resp.content)
        flights = resp_dict["S:Envelope"]["S:Body"]["ns2:getFlightsResponse"]["return"]
        for flight in flights:
            print "Details for flight ID:", flight["id"]
            for k, v in flight.iteritems():
                print "\t", k, v
