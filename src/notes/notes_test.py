import unittest
from notes import NotesApplication

class NotesApplicationTest(unittest.TestCase):
    '''
        Test Class for Notes Application
    '''
    
    def test_note_object_can_be_created(self):
        '''
            Test if a note taking object can be instantiated from NoteApplication
        '''
        author_name = 'Default Author'
        notes_from_author = []
        noteApp = NotesApplication(author_name, notes_from_author)
        self.assertIsInstance(noteApp, NotesApplication, msg='Object not an instance of NoteApplication Class')        
    
    def test_no_constructor_passed_empty_args(self):
        '''
            Test for case where both constructor arguments are empty strings
        '''
        noteApp = NotesApplication('', '')
        self.assertEqual(noteApp.author, 'Default Author', msg='NotesApplication constructor expects two arguments. Empty Values Passed')
        
    def test_no_constructor_arg_passed(self):
        '''
            Test case for initializing NoteApplication constructor without any argument
        '''
        noteApp = NotesApplication()
        self.assertNotIsInstance(noteApp, NotesApplication, msg='NotesApplication constructor expects two arguments. None passed')
        
    def test_invalid_args_for_constructor(self):
        author_name = 'Name'
        author_notes = []
        noteApp = NotesApplication(author_name, author_notes)
        self.assertEqual(type(noteApp.author), str, msg='NotesApplication constructor expects the first argument to be a string')
        self.assertEqual(type(noteApp), list, msg='NotesApplication constructor expects second argument to be list')
        
    
    
if __name__ == '__main__':
    unittest.main()
        

    
    