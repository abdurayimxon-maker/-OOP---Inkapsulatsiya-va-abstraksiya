class Employee:
    def __init__(self, name: str, employee_id: str, hourly_rate: float = 15.0) -> None:
        self.name = name
        self.employee_id = employee_id
        self.__working_hours = []
        self.hourly_rate = hourly_rate

    def log_hours(self, hour: int) -> bool:
        if 0 <= hour <= 24:
            self.__working_hours.append(hour)
            return True
        else:
            return False

    def total_hours(self) -> int:
        return sum(self.__working_hours)

    def calculate_salary(self) -> float:
        return self.total_hours() * self.hourly_rate

    def reset_hours(self) -> None:
        self.__working_hours = []


employee = Employee("Javlon", "E101", hourly_rate=20.0)

print(employee.log_hours(8))    
print(employee.log_hours(9))   
print(employee.log_hours(10))   
print(employee.log_hours(25))   

print(employee.total_hours())        
print(employee.calculate_salary())  

employee.reset_hours()
print(employee.total_hours())     
print(employee.calculate_salary())   