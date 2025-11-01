from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):
    
    # Ensure both endpoints return a 200 HTTP code
    def test_http_success(self):

        # Load escalator endpoint status code, assert it equals 200 to pass
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        self.assertEqual(200,escalator_response)

        # Load elevator endpoint status code, assert it equals 200 to pass
        elevator_response = app.test_client().get('/incidents/elevators').status_code
        self.assertEqual(200,elevator_response)

################################################################################

    # Ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        # Load and format data from WMATA API
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # For each incident, assert it contains all required fields
        for incident in json_response:
            for field in required_fields:
                self.assertIn(field,incident)

################################################################################

    # Ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):

        # Load and format data from WMATA API
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # For each incident, assert UnitType is ESCALATOR
        for incident in json_response:
            unit_type = incident["UnitType"]
            self.assertEqual(unit_type,"ESCALATOR")

################################################################################

    # Ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        
        # Load and format data from WMATA API
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # For each incident, assert UnitType is ELEVATOR
        for incident in json_response:
            unit_type = incident["UnitType"]
            self.assertEqual(unit_type,"ELEVATOR")

################################################################################

if __name__ == "__main__":
    unittest.main()