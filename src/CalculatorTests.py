import unittest
from Calculator import Calculator
from CsvReader import CsvReader, ClassFactory
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            pprint(test_data)

#    def test_subtraction(self):
#        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
#        for row in test_data:
#            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
#            self.assertEqual(self.calculator.result, int(row['Result']))



if __name__ == '__main__':
    unittest.main()
