#!/usr/bin/env python3

class Calculator:

    def __init__(self,first_arg,second_arg):
        self.num1 = first_arg
        self.num2 = second_arg

    def add(self):
        return self.num1 + self.num2
    
    def subtarction(self):
        return self.num1 - self.num2
    
    def multplication(self):
        return self.num1 * self.num2
    
    def divition(self):
       return self.num1 / self.num2
    
    '''      
    def user_inputs(self):
        self.a = int(input("Enter your first number: "))
        self.operator = input("Select one of these operations: 'add', 'minus','multiply','divide': ")
        self.b = int(input("Enter your second number: "))
    def calculator(self):
        if (self.operator == "add"):
            self.add(self.a,self.b)
        elif (self.operator == "minus"):
            self.subtarction(self.a,self.b)
        elif (self.operator == "multiply"):
            self.multplication(self.a,self.b)
        elif (self.operator == "divide"):
            self.divition(self.a,self.b)
        else:
            print("Please select the right operator")



cal_obj =Calculator()
cal_obj.user_inputs()
cal_obj.calculator()
'''