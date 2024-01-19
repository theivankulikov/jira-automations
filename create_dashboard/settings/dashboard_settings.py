dashboard_name = "dashboard name"
label_name = "label for filtering items"

jql_left_side = [
    ["Bugs in Dev", 'project = projectname AND issuetype in (Bug) AND status in ("Dev") AND (labels = ' + label_name + ')']
]

jql_right_side = [
    ["Bugs in QA", 'project = projectname AND issuetype in (Bug) AND status in ("QA") AND (labels = ' + label_name + ')']
]