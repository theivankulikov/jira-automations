# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-filters/

import requests
from requests.auth import HTTPBasicAuth
import json


def create_filter(jira_url, login, token, jql_name, jql_body):
    # Authentification
    auth = HTTPBasicAuth(login, token)

    # Searching filter
    print("Searching filter...")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

    params = {"filterName": '"' + jql_name + '"'}

    response = requests.get(
        jira_url + "/rest/api/3/filter/search",
        params=params,
        headers=headers,
        auth=auth,
    )

    print("Status code: " + str(response.status_code))
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


    if len(json.loads(response.text)["values"]) > 0:
        # Updating filter
        print("Filter with provided name is found. Updating filter...")

        filter_for_updating = json.loads(response.text)["values"][0]["self"]
        #response = requests.request("DELETE", filter_for_updating, auth=auth)

        payload = json.dumps( {
                "description": "Updated by Jira Automations",
                "jql": jql_body,
                "name": jql_name
            } )

        response = requests.request(
            "PUT",
            filter_for_updating,
            data=payload,
            headers=headers,
            auth=auth
            )

        print("Status code: " + str(response.status_code))
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

        if 200 <= response.status_code <= 299:
            print("Filter is updated: " + json.loads(response.text)["viewUrl"])
            return json.loads(response.text)["viewUrl"]
        else:
            print("Error: filter is NOT updated.")
            return -1

    else:
        # Creating filter
        print("Filter with provided name is NOT found. Creating filter...")

        payload = json.dumps( {
                "description": "Created by Jira Automations",
                "jql": jql_body,
                "name": jql_name,
                "sharePermissions": [{"type": "authenticated"}],
            } )

        response = requests.request(
            "POST",
            jira_url + "/rest/api/3/filter",
            data=payload,
            headers=headers,
            auth=auth,
        )

        print("Status code: " + str(response.status_code))
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

        if 200 <= response.status_code <= 299:
            print("Filter is created: " + json.loads(response.text)["viewUrl"])
            return json.loads(response.text)["viewUrl"]
        else:
            print("Error: filter is NOT created.")
            return -1
