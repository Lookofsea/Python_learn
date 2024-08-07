class Employee:
    def __init__(self,name,id) -> None:
        self.name = name 
        self.id = id

    def print_info(self):
        print(f"name:{self.name} ,id: {self.id},salary:{self.calculate_monthly_pay()}")

    def calculate_monthly_pay(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, name, id) -> None:
        super().__init__(name, id)
        self.month_salary = 5000

    def calculate_monthly_pay(self) -> int:
        return self.month_salary

class PartTimeEmployee(Employee):

    def __init__(self, name, id,work_days) -> None:
        super().__init__(name, id)
        self.day_salary = 300
        self.work_days = work_days

    def set_day_salary(self,day_salary):
        self.day_salary = day_salary

    def calculate_monthly_pay(self) -> int:
        return self.day_salary * self.work_days

tom = FullTimeEmployee("tom","01")
leo = PartTimeEmployee("leo","02",21)

tom.print_info()
leo.print_info()

        