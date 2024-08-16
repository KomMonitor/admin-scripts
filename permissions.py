import json
import csv
import os
import requests

kommonitor_url = os.environ.get('KOMMONITOR_URL', 'localhost')
keycloak_realm = os.environ.get('KEYCLOAK_REALM', 'kommonitor')
keycloak_auth_endpoint = os.environ.get('KEYCLOAK_AUTH_ENDPOINT', 'localhost:8080/keycloak/')
admin_script_secrets = os.environ.get('ADMIN_SCRIPT_SECRETS', 'secrets')
grant_type = os.environ.get('GRANT_TYPE', 'client_credentials')
client_id = os.environ.get('CLIENT_ID', 'kommonitor-admin-script')
data_management = os.environ.get('DATA_MANGEMENT','data-management')
output_dir = os.environ.get('OUTPUT_DIR','./result')

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

#getOrganisationUnits
url = kommonitor_url+'/data-management/management/organizationalUnits'
payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer '+token
}
org = requests.request('GET', url, headers=headers, data=payload)
organisations = org.json()

roleId_permission = {}
for o in organisations:
    for role in o['roles']:
        roleId_permission[role['roleId']] = o['name']+'-'+role['permissionLevel']

my_list = []
for i in indicators:
    indicator = i['indicatorName']
    for spatial_unit in i['applicableSpatialUnits']:
        su_name = spatial_unit['spatialUnitName']
        for role_id in spatial_unit['allowedRoles']:
            permissions = roleId_permission[role_id]
            my_list.append({'indikator': indicator,'raumeinheit': su_name,'freigaben': permissions})

with open(output_dir+'/results.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames= ['indikator','raumeinheit','freigaben'])
    w.writeheader()
    w.writerows(my_list)

