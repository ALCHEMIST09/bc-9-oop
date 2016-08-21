import unittest
import inspect
from notes import NotesApplication

class NotesApplicationTest(unittest.TestCase):
    '''
        Test Class for Notes Application
    '''
    
    def test_create_notes_object(self):
        '''
            Test note_object can be instantiated from NotesApplication
        '''
        author = 'Bootcamper'
        notes = ['Now I know how to write various kinds of unit tests', 'I have made Git to part of my process while creating any application']
        noteApp = NotesApplication(author, notes)
    
    def test_note_object_is_instance_of_notes_application_class(self):
        '''
            Test if a note taking object can be instantiated from NoteApplication
        '''
        author_name = 'Default Author'
        notes_from_author = ['week two of bootcamp']
        noteApp = NotesApplication(author_name, notes_from_author)
        self.assertIsInstance(noteApp, NotesApplication, msg='Object not an instance of NoteApplication Class')        
    
    def test_constructor_passed_empty_args(self):
        '''
            Test for case where both constructor arguments are empty strings
        '''
        with self.assertRaises(TypeError):
            noteApp = NotesApplication()
            
    def test_constructor_not_passed_author_name(self):
        '''
            Test constructor was not given an author name
        '''
        author = ''
        notes_list = ['version control for everyone']
        noteApp = NotesApplication(author, notes_list)
        self.assertEqual(noteApp.author, '', msg='Constructor missing name of author. Name of author required as first argument')        
        
        
    def test_notes_list_param_not_a_list(self):
        '''
            Test notes parameter is of type list
        '''
        author = 'Default Author'
        notes_list = ['this is note a list, it is called a tuple', 'this data structure is index from zero']
        noteApp = NotesApplication(author, notes_list)
        self.assertEqual(type(noteApp.notes), list, msg='Second parameter of NotesApplication should be a list.')
        with self.assertRaises(TypeError):
            author = 'Another Author'
            notes_list = ''
            noteApp = NotesApplication(author, notes_list)   
    
    def test_constructor_missing_one_argument(self):
        '''
            Test second parameter passed to constructor not a list
        '''
        with self.assertRaises(TypeError):
            author = 'New Author'
            noteApp = NotesApplication(author)
            
    def test_author_argument_is_string(self):
        '''
            Test to determine if author name is a string
        '''
        author = 'Teaching Assistant'
        notes_list = ['Bootcamp Cohort IX at Nairobi', 'Aspiring Andelas taken through intensive training']
        noteApp = NotesApplication(author, notes_list)
        self.assertEqual(type(noteApp.author), str, msg="Construct expects its first argument to be a string")
        
    def test_create_method_called_without_argument(self):
        '''
            Test create method of NotesApplication class called without an argument
        '''
        with self.assertRaises(TypeError):
            noteApp = NotesApplication('Luke', ['Getting closer to mastering the coding art', 'Code Complete'])
            noteApp.create()
    
    def test_create_method_called_with_one_argument(self):
        '''
            Test create method is called with only one argument
        '''
        with self.assertRaises(TypeError):
            noteApp = NotesApplication('Luke', ['Getting closer to mastering the coding art', 'Code Complete'])
            noteApp.create('')
            
    def test_not_id_exists(self):
        '''
            Test ID used to reference a particular story is within the notes_list
        '''
        with self.assertRaises(TypeError):
            noteApp = NotesApplication('Luke', ['Getting closer to mastering the coding art', 'Code Complete'])
            noteApp.get(10)
            
    
            
    
if __name__ == '__main__':
    unittest.main()
        

    
    