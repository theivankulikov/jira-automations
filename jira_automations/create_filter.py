# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-filters/

import requests
from requests.auth import HTTPBasicAuth
import json


def create_filter(jira_url, login, token, jql_name, jql_body):
    # Authentification
    auth = HTTPBasicAuth(login, token)

    # Searching filter
    print("Searching filter.")

    headers = {"Accept": "application/json"}

    params = {"filterName": '"' + jql_name + '"'}

    response = requests.get(
        jira_url + "/rest/api/3/filter/search",
        params=params,
        headers=headers,
        auth=auth,
    )

    print(
        json.dumps(
            json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
        )
    )

    if len(json.loads(response.text)["values"]) > 0:
        # Updating filter
        print("Updating filter.")

        filter_for_deletion = json.loads(response.text)["values"][0]["self"]
        response = requests.request("DELETE", filter_for_deletion, auth=auth)
        print("Filter deletion status: " + str(response.status_code))
    else:
        # Creating filter
        print("Creating filter.")

        headers = {"Accept": "application/json", "Content-Type": "application/json"}

        payload = json.dumps(
            {
                "description": "Created by Jira Automations",
                "jql": jql_body,
                "name": jql_name,
                "sharePermissions": [{"type": "authenticated"}],
            }
        )

        response = requests.request(
            "POST",
            jira_url + "/rest/api/3/filter",
            data=payload,
            headers=headers,
            auth=auth,
        )
        print(
            json.dumps(
                json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
            )
        )

    return created_filter
