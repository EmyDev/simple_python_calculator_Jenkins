#!/usr/bin/env python3
import unittest
from Calculator import Calculator

class TestCalc(unittest.TestCase):
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.calculator = Calculator(4,2)
    
    def test_add(self):
        self.assertEqual(self.calculator.add(),6)

    def test_minus(self):
        self.assertEqual(self.calculator.subtarction(),2)
    
    def test_multiplication(self):
        self.assertEqual(self.calculator.multplication(),8)

    def test_divition(self):
        self.assertEqual(self.calculator.divition(),2)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()

    

