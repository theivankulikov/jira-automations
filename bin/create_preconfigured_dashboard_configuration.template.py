DASHBOARD_NAME = "dashboard name"
LABEL_NAME = "label for filtering items"

JQL_LEFT_SIDE = [
    ["Bugs in Dev", 'project = projectname AND issuetype in (Bug) AND status in ("Dev") AND (labels = ' + LABEL_NAME + ')']
]

JQL_RIGHT_SIDE = [
    ["Bugs in QA", 'project = projectname AND issuetype in (Bug) AND status in ("QA") AND (labels = ' + LABEL_NAME + ')']
]