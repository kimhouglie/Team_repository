def build_report(records, target):
    days=0
    streak=0
    report=0
    chk=0
    total=0
    if 0>len(records)>365:
        return -1,-1,-1;
    for A in records:
        total+=A
        if A>=target:
            streak+=1
            chk+=1
            if report<=chk:
                report=chk
        else :
            chk=0
    return total//len(records), streak, report
records= [60, 90, 0, 45, 120, 75, 0]
print(build_report(records,60))
