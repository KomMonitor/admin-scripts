# Kommonitor Admin Script

This Python script interacts with the Data Management API to determine which organizational units have specific permissions for spatial units related to each indicator. The container generates a CSV file containing the indicator, spatial unit, and associated permissions.This script simplifies the process of analyzing permissions across different organizational units and indicators within the Kommonitor system.

## Prerequisites

- Docker
- Docker Compose
- Clone the repo:[Admin-scripts](https://github.com/KomMonitor/admin-scripts.git)
- cd to repo
  
### Setup
#### 1. build docker image
Run ``docker build -t kommonitor/admin_script:dev . ``
#### 2. create an .env file

Ensure your `.env` file is correctly configured. Example:

```
KOMMONITOR_URL=http://localhost
KEYCLOAK_REALM=kommonitor-demo
KEYCLOAK_AUTH_ENDPOINT=http://localhost/keycloak/
ADMIN_SCRIPT_SECRETS=secrets
GRANT_TYPE=client_credentials
CLIENT_ID=kommonitor-admin-scripts
DATA_MANGEMENT=data-management
```



#### 3. run the script 
Run ``docker run --env-file admin_script.env -v path/to/result:/app/result kommonitor/admin_script:dev permissions.py`` 

