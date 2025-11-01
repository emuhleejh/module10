import json
import requests
from flask import Flask

# API endpoint URLs and access keys
WMATA_API_KEY = "9ad449fc0b3840f0a6bf3979ea3894c0"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# Get incidents by machine type (elevators/escalators)
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
 
  # Format function input correctly for incident unit_type filtering
  if unit_type == "escalators":
    unit_type = "ESCALATOR"

  elif unit_type == "elevators":
    unit_type = "ELEVATOR"

  # Empty list of incidents
  incidents = []

  # GET request to WMATA Incidents API
  response = requests.get(INCIDENTS_URL, headers=headers)

  # Format return from WMATA API as JSON
  returned_incidents = response.json()
  returned_incidents_list = returned_incidents["ElevatorIncidents"]

  # Loop through incidents from API response
  for incident in returned_incidents_list:

    # Create empty dictionary for station info
    incident_dict = {}

    # Only proceed if incident UnitType matches parameter called by function
    if incident["UnitType"] == unit_type:

      # Add key-value pairs to incident_dict
      incident_dict["StationCode"] = incident["StationCode"]      
      incident_dict["StationName"] = incident["StationName"] 
      incident_dict["UnitName"] = incident["UnitName"] 
      incident_dict["UnitType"] = incident["UnitType"] 

      # Add incident dictionary to incidents list
      incidents.append(incident_dict)

  # Convert list of incidents to JSON string
  all_incidents = json.dumps(incidents)

  return all_incidents

if __name__ == '__main__':
    app.run(debug=True)