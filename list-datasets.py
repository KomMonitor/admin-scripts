import json
import csv
import os
import requests
import argparse

kommonitor_url = os.environ.get('KOMMONITOR_URL', 'localhost')
keycloak_realm = os.environ.get('KEYCLOAK_REALM', 'kommonitor')
keycloak_auth_endpoint = os.environ.get('KEYCLOAK_AUTH_ENDPOINT', 'localhost:8080/keycloak/')
admin_script_secrets = os.environ.get('ADMIN_SCRIPT_SECRETS', 'secrets')
grant_type = os.environ.get('GRANT_TYPE', 'client_credentials')
client_id = os.environ.get('CLIENT_ID', 'kommonitor-admin-script')
data_management = os.environ.get('DATA_MANGEMENT','data-management')
output_dir = os.environ.get('OUTPUT_DIR','/app/result')

#getToken
url =  keycloak_auth_endpoint+'/realms/'+keycloak_realm+'/protocol/openid-connect/token'
payload = 'grant_type='+grant_type+'&client_id='+client_id+'&client_secret='+admin_script_secrets
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request('POST', url, headers=headers, data=payload)
token_data = response.json()
token = token_data['access_token']

#getIndicators
url = kommonitor_url+'/data-management/management/indicators'
payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer '+token
}
ind = requests.request('GET', url, headers=headers, data=payload)
indicators = ind.json()
indicator_table = []
for i in indicators:
    indicator_table.append({"id": i['indicatorId'], "name": i['indicatorName']})
#getSpatialUnits
spatial_unit_table = []
for i in indicators:
    for spatial_unit in i['applicableSpatialUnits']:
        spatial_unit_table.append({"id": spatial_unit['spatialUnitId'], "name": spatial_unit['spatialUnitName']})

#getOrganisationUnits
url = kommonitor_url+'/data-management/management/organizationalUnits'
payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer '+token
}
org = requests.request('GET', url, headers=headers, data=payload)
organisations = org.json()
organisations_table = []
for i in organisations:
    organisations_table.append({"id":i['organizationalUnitId'], "name":i['name']})

parser = argparse.ArgumentParser(description='choose which csv file to generate')
parser.add_argument('--resourcetype', choices=['indicators', 'spatial_unit','organisations'])
args = parser.parse_args()

#getFiles
if args.resourcetype == 'indicators':
    with open(f'{output_dir}/indicators.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'name'])
        w.writeheader()
        w.writerows(indicator_table)
if args.resourcetype=='spatial_unit':
    with open(f'{output_dir}/spatial_units.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'name'])
        w.writeheader()
        w.writerows(spatial_unit_table)
if args.resourcetype == 'organisations':
    with open(f'{output_dir}/organisations.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'name'])
        w.writeheader()
        w.writerows(organisations_table)