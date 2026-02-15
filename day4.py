m = int(input("enter size"))
scores = []
for i in range(m):
    n = int(input("enter scores :"))
    scores = scores + [n]
valid_scores = 0
ignored_scores = 0
removed_due_to_personalization = 0
d = 1
print("registration digit :", d)
low_risk = []
medium_risk = []
high_risk = []
critical_risk = []
for i in range(m):
    if scores[i] < 0:
        ignored_scores += 1
    elif scores[i] >= 0 and scores[i] <= 30:
        valid_scores += 1
        low_risk = low_risk + [scores[i]]
    elif scores[i] > 30 and scores[i] <= 60:
        valid_scores += 1
        medium_risk = medium_risk + [scores[i]]
    elif scores[i] > 60 and scores[i] <= 100:
        valid_scores += 1
        high_risk = high_risk + [scores[i]]
    else:
        valid_scores += 1
        critical_risk = critical_risk + [scores[i]]
print("low risk :", low_risk)
print("medium risk :", medium_risk)
print("high risk :", high_risk)
print("critical risk :", critical_risk)
if d % 2 == 0:
    removed_due_to_personalization += len(low_risk)
    low_risk = []
else:
    removed_due_to_personalization += len(critical_risk)
    critical_risk = []
print("after personalization filtering:")
print("low risk :", low_risk)
print("medium risk :", medium_risk)
print("high risk :", high_risk)
print("critical risk :", critical_risk)
print("total valid entries :", valid_scores)
print("total ignored entries :", ignored_scores)
print("total removed due to personalization :", removed_due_to_personalization)

