class Resident:
    def __init__(self, name):
        self.name = name
        self.debt = 0
        self.incidents = []
        self.status = "normal"
        self.risk_score = 0

    def add_incident(self, description, severity):
        incident = {
            "description": description,
            "severity": severity
        }

        self.incidents.append(incident)
        self.risk_score += severity
        self.update_status()

    def add_debt(self, amount):
        self.debt += amount

    def update_status(self):
        if self.risk_score >= 10:
            self.status = "blocked"
        elif self.risk_score >= 5:
            self.status = "monitoring"
        else:
            self.status = "normal"