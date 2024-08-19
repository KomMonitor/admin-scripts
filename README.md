# Kommonitor Admin Script

This Python script interacts with the Data Management API to determine which organizational units have specific permissions for spatial units related to each indicator. The container generates a CSV file containing the indicator, spatial unit, and associated permissions.This script simplifies the process of analyzing permissions across different organizational units and indicators within the Kommonitor system.

## Prerequisites

- Docker
- Docker Compose

## Setup
### 1. create an .env file

Ensure your `.env` file is correctly configured. Example:

KOMMONITOR_URL=http://localhost
KEYCLOAK_REALM=kommonitor-demo
KEYCLOAK_AUTH_ENDPOINT=http://localhost/keycloak/
ADMIN_SCRIPT_SECRETS=secrets
GRANT_TYPE=client_credentials
CLIENT_ID=kommonitor-admin-scripts
DATA_MANGEMENT=data-management


### 2. Start Docker Compose
Clone the repo:[Admin-scripts](https://github.com/KomMonitor/admin-scripts.git)
Run **docker compose up** 

