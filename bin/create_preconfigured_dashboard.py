import jira_automations

import auth_data
import create_preconfigured_dashboard_configuration as db_config

left_filters = []
right_filters = []

for jql in db_config.jql_left_side:
    left_filters.append(jira_automations.create_filter(auth_data.JIRA_URL, auth_data.LOGIN, auth_data.LOGIN_TOKEN, jql[0], jql[1]))

for jql in db_config.jql_right_side:
    right_filters.append(jira_automations.create_filter(auth_data.JIRA_URL, auth_data.LOGIN, auth_data.LOGIN_TOKEN, jql[0], jql[1]))