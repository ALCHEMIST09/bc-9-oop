class NotesApplication(object):
    def __init__(self, author, notes=[]):
        self.author = author
        self.notes = notes
        
    def create(self, new_content):
        self.notes.append(new_content)
        
    def list(self):
        for k, v in enumerate(self.notes):
            line  = str(k) + "\n"
            line += v + "\n"
            line += "By " + self.author + "\n\n"
            print(line)
            
    def search(self, search_text):
        for k,v in enumerate(self.notes):
            if v.find(search_text) != -1:
                result  = "Showing results for '" + search_text + "'\n"
                result += "Note ID: " + str(k) + "\n"
                result += v + "\n"
                result += "By " + self.author + "\n"
                print(v)
    
    def get(self, note_id):
        return self.notes[note_id]
                
    def delete(self, note_id):
        self.notes.pop(note_id)
        
    def edit(self, note_id, new_content):
        self.notes[note_id] = new_content

luke_notes = ['bootcamp days at andela', 'managed passed the andela interviews']            
np = NotesApplication('Luke', luke_notes)
np.create('pushing stuff to my remote repositroy in github')
np.create('andela tech talent acceleration program')
print(np.list())
print()
print(np.search('andela'))
np.edit(2, 'not so cool stuff')
print(np.list())
  
        