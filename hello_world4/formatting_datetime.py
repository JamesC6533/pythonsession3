from datetime import datetime as DateTime

gates_bd = DateTime(1955, 10, 28, 22, 0, 0)
print(gates_bd)
print()

print(gates_bd.strftime('Bill was born on %B %d, %Y at %I:%M %p'))
print()

print(gates_bd.strftime('BG: %m/%d/%y'))
print()