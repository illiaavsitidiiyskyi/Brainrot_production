from scrt.core.risk_engine import calculate_risk, update_status

def process_resident(resident):
    resident.risk_score = calculate_risk(resident)
    update_status(resident)


def calculate_risk(resident):
    score = 0
    
    score += resident.debt * 2
    
    score += len(resident.incidents) * 5
    return score

def update_status(resident):
    if resident.risk_score > 20:
        resident.status = "blocked"
    elif resident.risk_score > 10:
        resident.status = "monitoring"
    else:
        resident.status = "normal"
