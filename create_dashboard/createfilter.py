# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-filters/

import requests
from requests.auth import HTTPBasicAuth
import json

import authdata
import settings


def createfilter(jql_name, jql_body):
    created_filter = "Filter is not created"

# Authentification
    auth = HTTPBasicAuth(authdata.email, authdata.api_token)


# Searching filter with name jql_name

    print("Searching filter.")

    headers = {
        "Accept": "application/json",
    }

    params = {
        'filterName' : '"' + settings.dashboard_name + ' ' + jql_name + '"'
    }

    response = requests.get(
        settings.jira_url + "/rest/api/3/filter/search",
        params=params,
        headers=headers,
        auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    


# Removing filter with name jql_name
    print("Removing filter.")
    if len(json.loads(response.text)['values']) >0:
        filter_for_deletion = json.loads(response.text)['values'][0]['self']
    
        response = requests.request(
            "DELETE",
            filter_for_deletion,
            auth=auth
        )
      
        print("Filter deletion status: " + str(response.status_code))
    else:
        print("Filter not found. Nothing to delete.")


# Creating filter with name jql_name
    
    print("Creating filter.")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "description": "For " + settings.dashboard_name + " dashboard",
        "jql": jql_body,
        "name": settings.dashboard_name + " " + jql_name,
        "sharePermissions": [{"type": "authenticated"}]
    } )

    response = requests.request(
        "POST",
        settings.jira_url + "/rest/api/3/filter",
        data=payload,
        headers=headers,
        auth=auth
    )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    if len(json.loads(response.text)['self']) >0:
        created_filter = json.loads(response.text)['self']
        print("Filter is created.")


    return created_filter