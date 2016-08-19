import unittest

from super_sum import super_sum

class MySuperSumTest(unittest.TestCase):
    '''
        Takes in any number of numbers or sum of numbers
        and sums them up
    '''
    
    def test_sum_of_args(self):
        '''
            Test sum of numbers passed to the function
            Numbers can be individual integers, or list of numbers
        '''
        self.assertEquals(super_sum(1, 2, 3, 4), 10)
        self.assertEquals(super_sum([1, 2, 3, 4]), 10)
    
    def test_no_arguments_given(self):
        '''
            Test if function called without any argument
        '''
        with self.assertRaises(TypeError):
            super_sum()
            
    def test_non_number_arguments(self):
        '''
            Test for non number arguments
        '''
        with self.assertRaises(TypeError):
            super_sum('a', 'b', 'c')
            
    def test_result_in_iterable(self):
        '''
            Test for any non-number items in the list
            if the function is passed a list of numbers
            as an argument
        '''
        self.assertIn(super_sum(1, 2, 3, 4), [3, 10, 6, 1], msg='Function result not in list')
        
    def test_empty_list_of_arguments(self):
        '''
            Test for an empty list passed as an argument
        '''
        with self.assertRaises(TypeError):
            super_sum([])
    
    
if __name__ == '__main__':
    unittest.main()