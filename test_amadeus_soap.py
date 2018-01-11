#!/usr/bin/env python

import base64
from constants import *
import zeep

if __name__ == "__main__":

    client = zeep.Client(wsdl=WSDL1)

    # authenticate
    resp = client.service.Security_Authenticate(
            userIdentifier={
                "originIdentification": {
                    "sourceOffice": SOURCEOFFICE
                    },
                "originatorTypeCode": "U",
                "originator": USERNAME
                },
            passwordInfo={
                "dataLength": str(len(PASSWORD)),
                "dataType": "E",
                "binaryData": base64.b64encode(PASSWORD)
                },
            dutyCode={
                "dutyCodeDetails" : {
                    "referenceQualifier": "DUT",
                    "referenceIdentifier": "SU"
                    }
                }
            )
    session = resp["header"]["session"]
    headers = {"session": session}

    # JBU 1012: JetBlue Chicago to Boston
    print client.service.Air_FlightInfo(generalFlightInfo={
            "companyDetails": {
                "marketingCompany": "B6" # IATA airline code
                },
            "flightIdentification": {
                "flightNumber": "1012"
                },
            "flightDate": {
                "departureDate": "110118" # ddmmyy
                },
            "boardPointDetails": {
                "trueLocationId": "ORD"
                },
            "offPointDetails": {
                "trueLocationId": "BOS"
                }
            }, _soapheaders=headers)

    client.service.Security_SignOut(_soapheaders=headers)
