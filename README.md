#Scripts to automate routine manager tasks in Jira
Before you start using sctripts:
- Rename auth_data.template.py to auth_data.py and edit it. Add credentials to Jira;

##Create dashboard
The script creates a Jira dashboard using a predefined list of JQLs.
- Rename create_dashboard/settings.template.py to create_dashboard/settings.py;
- Edit settings.py. Provide a name for a dashboard and edit the list of JQLs;
- Execute run.py.