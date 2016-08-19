import unittest

from my_sum import my_sum

class MySumTests(unittest.TestCase):
    '''
        Takes two numbers (x and Y) and returns the sum
    '''
    
    def setUp(self):
        # setting up
        self.numbers = [10, 5, 5, 7, 10, 15]
        
    def test_sum_of_numbers(self):
        '''
            Test sum of digits / numbers
        '''
        result = my_sum(5, 10)
        self.assertEqual(result, 15,)
        self.assertEqual(my_sum(10, 15), 25)
        
    def test_non_numbers(self):
        '''
            Assert throwing of exception when it's a non number
        '''
        with self.assertRaises(ValueError):
            my_sum('a', 'b')
        
    def test_sum_of_negative_nums(self):
        '''
            Test adding negative numbers: -4 + 5 = 1
        '''
        self.assertEquals(my_sum(-4, 5), 1)
        self.assertEquals(my_sum(-6, -4), -10)
        
    def test_no_argument_given(self):
        '''
            Test if one or both arguments missing
        '''
        with self.assertRaises(TypeError):
            my_sum()
        
if __name__ == '__main__':
    unittest.main()
    

        
            
        

