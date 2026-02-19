from scrt.core.models import Resident

r1 = Resident("Артем Кабаневский")
r2 = Resident("Кривой Назар")
r3 = Resident("Иллюша Попович")
r4 = Resident("Данил Колбасенко")

r1.add_incident("Suspicious activity", 5)
r1.add_debt(500)

print("Имя:", r1.name)
print("Долг:", r1.debt)
print("Риск:", r1.risk_score)
print("Статус:", r1.status)
print("Инциденты:", r1.incidents)
