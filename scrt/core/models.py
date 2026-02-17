class Resident:
    def __init__(self, name):
        self.name = name
        self.debt = 0
        self.incidents = []
        self.status = "normal"
        self.risk_score = 0

    def add_incident(self, incident):
        self.incidents.append(incident)

