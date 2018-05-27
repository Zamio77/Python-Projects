"""
Makes use of the employee classes to create an object
of those files.
"""

import employee


def main():
    emp = input("Please enter the employee's name. ")
    emp_num = input("Please enter the employee's number. ")
    shift = int(input("Please enter the employee's shift. 1 = day, 2 = night "))
    pay = float(input("Please enter the employee's hourly rate. "))

    worker = employee.ProductionWorker(emp, emp_num, shift, pay)

    print("Here is the information you have enter.")
    print(f"Employee name: {worker.get_employee_name()}")
    print(f"Employee number: {worker.get_employee_num()}")
    print(f"Employee shift: {worker.get_shift_num()}")
    print(f"Employee hourly rate: ${worker.get_hourly_pay_rate()}")

main()
