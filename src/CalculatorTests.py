import unittest
import csv
from Calculator import Calculator
from CsvReader import CsvReader, ClassFactory
from pprint import pprint
from decimal import Decimal
import math


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    #    def test_instantiate_calculator(self):
    #        self.assertIsInstance(self.calculator, Calculator)


    def test_square(self):
        test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.division(row['Value 1'], row['Value 2']), Decimal(row['Result']))
            self.assertEqual(self.calculator.result, Decimal(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            
    def test_addition(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
