"""
A program to create the employee and the
subclass ProductionWorker.
"""


class Employee:

    def __init__(self, employee_name, employee_num):
        self.employee_name = employee_name
        self.employee_num = employee_num

    def set_employee_name(self, employee_name):
        self.employee_name = employee_name

    def set_employee_num(self, employee_num):
        self.employee_num = employee_num

    def get_employee_name(self):
        return self.employee_name

    def get_employee_num(self):
        return self.employee_num

class ProductionWorker(Employee):

    def __init__(self, employee_name, employee_num, shift_num, hourly_pay_rate):
        Employee.__init__(self, employee_name, employee_num)

        self.shift_num = shift_num
        self.hourly_pay_rate = hourly_pay_rate

    def set_shift_num(self, shift_num):
        self.shift_num = shift_num

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate

    def get_shift_num(self):
        return self.shift_num

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate
