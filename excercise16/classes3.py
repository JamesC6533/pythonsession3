class Employee:
    name = ""
    age = 0
    payroll = 0
    techId = ""
    email = ""
    pay = []

    def __init__(self, name, age, payroll, techId, email, pay):
        self.name = name
        self.age = age
        self.payroll = payroll
        self.techId = techId
        self.email = email
        self.pay = pay

