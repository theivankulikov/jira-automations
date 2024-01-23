import jira_automations

from auth_data import *
from create_preconfigured_dashboard_configuration import *

left_filters = []
right_filters = []

for jql in JQL_LEFT_SIDE:
    left_filters.append(jira_automations.create_filter(JIRA_URL, LOGIN, LOGIN_TOKEN, jql[0], jql[1]))


for jql in JQL_RIGHT_SIDE:
    right_filters.append(jira_automations.create_filter(JIRA_URL, LOGIN, LOGIN_TOKEN, jql[0], jql[1]))