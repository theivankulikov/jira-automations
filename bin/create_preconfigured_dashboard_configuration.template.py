DASHBOARD_NAME = "dashboard name"
LABEL_NAME = "label for filtering items"

jql_left_side = [
    ["Bugs in Dev", 'project = projectname AND issuetype in (Bug) AND status in ("Dev") AND (labels = ' + LABEL_NAME + ')']
]

jql_right_side = [
    ["Bugs in QA", 'project = projectname AND issuetype in (Bug) AND status in ("QA") AND (labels = ' + LABEL_NAME + ')']
]