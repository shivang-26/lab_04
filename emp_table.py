class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"


def sort_employees(employees, sort_key):
    if sort_key == 1:
        return sorted(employees, key=lambda x: x.age)
    elif sort_key == 2:
        return sorted(employees, key=lambda x: x.name)
    elif sort_key == 3:
        return sorted(employees, key=lambda x: x.salary)
    else:
        raise ValueError("Invalid sorting parameter")

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Choose a sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    
    try:
        sort_key = int(input("Enter the sorting parameter (1/2/3): "))
        sorted_employees = sort_employees(employees, sort_key)
        
        print("\nEmployee ID\tName\tAge\tSalary")
        for emp in sorted_employees:
            print(emp)
    except ValueError:
        print("Invalid input. Please enter a valid sorting parameter (1/2/3).")

if __name__ == "_main_":
    main()