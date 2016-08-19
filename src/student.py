from datetime import date

state = {'KE':'Kenya', 'NG':'Nigeria', 'TZ':'Tanzania', 'UG':'UGANDA'}

class Student(object):
    
    # Create Class property to keep track of the last
    # student ID generated
    last_stud_id = 0
    todays_attendance = []
    
    def __init__(self, fname, lname, cc='KE'):
        '''Generate Sequential ID'''
        self.id = self.generate_id()
        self.first_name = fname
        self.last_name  = lname
        self.country    = state[cc]
        
    def generate_id(self):
        '''
            This method is called during class instantiation
            to generate the student ID
        '''
        Student.last_stud_id += 1
        stud_id = Student.last_stud_id
        return stud_id
     
    def attend_class(self, **kwargs):
        '''
            default values:
                location  = 'Hogwarts'
                date      = current_date
                teacher   = 'Alex'
        '''
        location = kwargs.get('location', 'Hogwarts')
        which_day = kwargs.get('date', date.today())
        teacher  = kwargs.get('teacher', 'Alex')
        
        result  = self.first_name + ' attended a class taught by ' + teacher + ' at '
        result += location + ' on ' + str(which_day)
        fullname = ''
        if str(which_day) == str(date.today()):
            fullname = self.first_name + ' ' + self.last_name
            Student.todays_attendance.append(fullname)
        return result
    
    @staticmethod
    def get_attendance_list():
        '''
            Method should generate a list of people who attended class in that day
        '''
        todays_class = Student.todays_attendance
        result = "\n".join(todays_class)
        return result
    
    @staticmethod
    def my_method():
        print('This is a static method')
    
    
        
    
    
        


        
    
        
    