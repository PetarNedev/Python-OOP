class Employee:
    new_salary = 0

    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self, amount):
        self.new_salary = self.salary + amount
        return self.new_salary

    def get_annual_salary(self):
        return self.new_salary * 12


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
