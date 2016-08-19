from datetime import date
from student import Student

# Create at least 10 stidents

s1 = Student('Luke', 'M')
s2 = Student('Jojo', 'M')
s3 = Student('Emmanual', 'M')
s4 = Student('Msee Mjanja', 'K')
s5 = Student('Code', 'Warrior')
s6 = Student('Kimani', 'N')
s7 = Student('Stephen', 'N')
s8 = Student('BootKampa Mpoa', 'M')
s9 = Student('Msee Wa-mavybes', 'W')
s10 = Student('LateKama', 'O')

print(s1.id)
print(s2.id)
print(s3.id)

# Make at least 5 students attend class
today = str(date.today())
print(s1.attend_class(location='Crazies', date='2016-08-01', teacher='Anto'))
print(s2.attend_class())
print(s4.attend_class(location='Wizards', date=today, teacher='Chris'))
print(s8.attend_class(location='Hackers', date='2016-08-16', teacher='John.M'))
print(s9.attend_class(location='Painters', date=today, teacher='Me-Myself'))
    

# You should be able to print the list of students who attend class on a particular day
print()
print(Student.get_attendance_list())
print()

d = {'ke':'kenya', 'ug':'uganda', 'tz':'tanzania'}
print(d.get('sa'))

print(d['ke'])


