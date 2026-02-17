from scrt.core.models import Resident

r1 = Resident("Артем Кабаневский")
r2 = Resident("Кривой Назар")
r3 = Resident("Иллюша Попович")
r4 = Resident("Данил Колбасенко")

r1.add_incident("Late payment")
r1.debt += 500

print(r1.name)
print(r1.debt)
print(r1.incidents)
