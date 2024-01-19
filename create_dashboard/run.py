from src.createfilter import createfilter
from src.createdashboard import createdashboard

import settings.dashboard_settings as dashboard_settings

left_filters = []
right_filters = []

for jql in dashboard_settings.jql_left_side:
    left_filters.append(createfilter(jql[0], jql[1]))

for jql in dashboard_settings.jql_right_side:
    right_filters.append(createfilter(jql[0], jql[1]))



    
#TODO: создать дашборд
    #TODO: права доступа
    #TODO: добавить левые фильтры, правые фильтры