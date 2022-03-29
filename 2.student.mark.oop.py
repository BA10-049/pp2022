class Student : 
    #number of student
    def numb_student():
        return int(input("number of student: "))
    #infor about student    
    def accept(self, Name, Rollno, marks ):
        # use  ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, marks )
        ls.append(ob)
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i       
                                  
    def delete(self, rn):
        i = obj.search(rn)  
        del ls[i]
  
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll;
            }
            print(f"entered {i+1} student")
    numb_student = numb_student()
    students =infor_student(numb_student)

class Course :
    #number course 
    def number_course():
        return int(input("Enter number course: "))
    #infor about course    
    def infor_course(number_course):
        courses = []
        for i in range (number_course):
            print(f"Enter course number {i+1} infor: ")
            idCourse = input("idCourse: ")
            nameCourse = input("nameCourse: ")
    number_course = number_course()
    courses = infor_course(number_course)
