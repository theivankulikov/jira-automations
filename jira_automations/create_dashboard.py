# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-dashboards/

import requests
from requests.auth import HTTPBasicAuth
import json


def create_dashboard(db_name):
    created_dashboard = "Dasboard is not created"


# Authentification
    auth = HTTPBasicAuth(authdata.email, authdata.api_token)


# Searching dashboard with name settings.dashboard_name
    
    print("Searching dashboard.")

    headers = {
        "Accept": "application/json",
    }

    params = {
        'filterName' : db_name
    }

    response = requests.get(
        authdata.jira_url + "/rest/api/3/dashboard/search",
        params=params,
        headers=headers,
        auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


# Clearing the dashboard
    if len(json.loads(response.text)['values']) >0:
        print("Dashboard have been found. Clearing dashboard.")

        print("Dashboard is cleared.")
    else:
        print("Dashboard not found. Creation of newone is started.")
        
        print("Dashboard is created.")


    return created_dashboard