class NotesApplication(object):
    def __init__(self, author, notes):
        '''
            Initialize the NotesApplication class with two instance properties.
        '''
        if author == None or notes == None:
            raise TypeError('NotesApplication constructor expects two arguments. None given')
        elif type(notes) != list:
            raise TypeError('The second parameter passed to NotesApplication constructor should be a list')
        else:
            self.author = author
            self.notes = notes
        
    def create(self, new_content):
        '''
            Method takes in a single argument as a note and adds
            it to the notes property of the class
        '''
        if new_content == None:
            raise TypeError('Method expects string argunment. None given')
        elif new_content.strip() == '':
            raise TypeError('Method expects a non-empty string as an argument. Empty string given')
        else:
            self.notes.append(new_content)
        
    def list(self):
        '''
            Loop through all entries in the notes property returning each entry 
            using a pre-specified format: Note ID, note content, and note author
            all on separate lines
        '''
        for k, v in enumerate(self.notes):
            line  = str(k) + "\n"
            line += v + "\n"
            line += "By " + self.author + "\n\n"
            print(line)
            
    def search(self, search_text):
        '''
            Search for a particular string in all the entries in the note list.
            Return all the note entries that contain the particular string using
            a pre-specified format
        '''
        for k,v in enumerate(self.notes):
            if v.find(search_text) != -1:
                result  = "Showing results for '" + search_text + "'\n"
                result += "Note ID: " + str(k) + "\n"
                result += v + "\n"
                result += "By " + self.author + "\n"
                print(v)
    
    def get(self, note_id):
        '''
            Look up a note in the notes propety using a user-supplied ID
            that matches the index location of the particular note in the
            note list property
        '''
        if note_id >= len(self.notes):
            # IndexError
            raise TypeError('Note ID is not in the list of notes')
        else:
            return self.notes[note_id]
                
    def delete(self, note_id):
        '''    
            Given an ID that identifies a particular note in the notes
            list property, delete that note from the list
        '''
        self.notes.pop(note_id)
        
    def edit(self, note_id, new_content):
        '''
            Given an ID that identifies a particular note in the note list
            property and content as another parameter, change the content
            currently residing at the location referenced by the note_id argument
            to one passed in as "new_content" argument
        '''
        self.notes[note_id] = new_content

#luke_notes = ['bootcamp days at andela', 'managed passed the andela interviews']            
#np = NotesApplication('Luke', luke_notes)
#np.create('pushing stuff to my remote repositroy in github')
#np.create('andela tech talent acceleration program')
#print(np.list())
#print()
#print(np.search('andela'))
#np.edit(2, 'not so cool stuff')
#print(np.list())
  
        