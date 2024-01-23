# PROJECT IS UNDER DEVELOPMENT

# Jira Automations

Automate routine tasks in Jira!

## Examples of usage Jira Automations as a desktop tool

### Creation preconfigured Jira dashboard

- Run `pip install jira-automations`;
- Rename [auth_data.template.py](bin/auth_data.template.py) into `auth_data.py` and write Jira authentication data to the file;
- Rename [create_preconfigured_dashboard_configuration.template.py](bin/create_preconfigured_dashboard_configuration.template.py) into `create_preconfigured_dashboard_configuration.py` and write dashboard configuration to the file;
- Run [create_preconfigured_dashboard.py](bin/create_preconfigured_dashboard.py)

## Examples of usage Jira Automations as a package

- TODO

## TODO (ideas)

- Convert functions create_smth into methods of class Jira (and move authorisation into constructor);
- Integrate some logger instead of using print;
- Convert settings into yaml files;