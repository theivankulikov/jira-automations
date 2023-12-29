from createfilter import createfilter
import jqls

left_filters = []
right_filters = []

for jql in jqls.left_side:
    left_filters.append(createfilter(jql[0], jql[1]))

for jql in jqls.right_side:
    right_filters.append(createfilter(jql[0], jql[1]))



    
#TODO: создать дашборд
    #TODO: права доступа
    #TODO: добавить левые фильтры, правые фильтры