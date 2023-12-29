import settings

left_side = [
    ["AM Bugs - iOS - for Dev", 'project = AM AND issuetype in (Bug, Gap) AND status not in ("READY FOR QA ON BRANCH", "QA ON BRANCH IN PROGRESS", "Ready for QA", ReadyForQA, "QA In Progress", Done, Rejected) AND component in (iOS, "iOS(Driver)") AND (assignee not in(5b3a0f0be263df2dc32f75f3, 557058:c6b6bb16-4bd0-44aa-8f28-e343a258f7b6) or assignee is EMPTY) AND (labels = ' + settings.label_name + ')']
]

right_side = [
    ["AM Bugs - Android - for Dev", 'project = AM AND issuetype in (Bug, Gap) AND status not in ("READY FOR QA ON BRANCH", "QA ON BRANCH IN PROGRESS", "Ready for QA", ReadyForQA, "QA In Progress", Done, Rejected) AND component in (Android, "Android(Driver)") AND (assignee not in(5b3a0f0be263df2dc32f75f3, 557058:c6b6bb16-4bd0-44aa-8f28-e343a258f7b6) or assignee is EMPTY) AND (labels = ' + settings.label_name + ')']
]