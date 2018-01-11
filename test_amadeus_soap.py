#!/usr/bin/env python

import base64
from constants import *
import zeep

if __name__ == "__main__":

    client = zeep.Client(wsdl=WSDL1)

    # authenticate
    resp = client.service.Security_Authenticate(userIdentifier={
            "originatorTypeCode": "U",
            "originator": ""
            },
            passwordInfo={
                "dataLength": str(len(PASSWORD)),
                "dataType": "E",
                "binaryData": base64.b64encode(PASSWORD)
                }
            )
    print resp
        
    # JBU 1012: JetBlue Chicago to Boston
    print client.service.Air_FlightInfo(generalFlightInfo={
            "companyDetails": {
                "marketingCompany": "JBU"
                },
            "flightIdentification": {
                "flightNumber": "1012"
                },
            "flightDate": {
                "departureDate": "011118"
                },
            "boardPointDetails": {
                "trueLocationId": "ORD"
                },
            "offPointDetails": {
                "trueLocationId": "BOS"
                }
            })

    client.service.Security_SignOut()
