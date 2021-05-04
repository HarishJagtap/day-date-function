import unittest
import solution

class TestFunction(unittest.TestCase):
    def test_date_converter(self):
        self.assertEqual('Mon', solution.date_to_day(3, 5, 2021))
        self.assertEqual('Tue', solution.date_to_day(24, 10, 2000))
        self.assertEqual('Wed', solution.date_to_day(10, 2, 1700))
        self.assertEqual('Thu', solution.date_to_day(11, 2, 2100))
        self.assertEqual('Fri', solution.date_to_day(3, 7, 1970))
        self.assertEqual('Sat', solution.date_to_day(19, 3, 2005))
        self.assertEqual('Sun', solution.date_to_day(26, 12, 1830))

    def test_solution(self):
        input1 = {'2020-01-01': 4, '2020-01-02': 4, '2020-01-03': 6, 
            '2020-01-04': 8, '2020-01-05': 2, '2020-01-06': -6, '2020-01-07': 2, 
            '2020-01-08': -2}

        input2 = {'2020-01-01': 6, '2020-01-04': 12, '2020-01-05': 14, 
            '2020-01-06': 2, '2020-01-07': 4}

        output1 = {'Mon': -6, 'Tue': 2, 'Wed': 2, 'Thu': 4, 
            'Fri': 6, 'Sat': 8, 'Sun': 2}

        output2 = {'Mon': 2, 'Tue': 4, 'Wed': 6, 'Thu': 8, 
            'Fri': 10, 'Sat': 12, 'Sun': 14}

        solution_output1 = solution.solution(input1)
        solution_output2 = solution.solution(input2)

        for k, v in output1.items():
            self.assertEqual(v, solution_output1[k])
        
        for k, v in output2.items():
            self.assertEqual(v, solution_output2[k])

if __name__ == '__main__':
    unittest.main()