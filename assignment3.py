from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Database connection
DATABASE_URL = "postgresql://postgres:password@localhost/StudentInfoSystem"
# create_engine creates an engine which interprets the database api functions as well as behaviours
engine = create_engine(DATABASE_URL)
# a base class for declarative class definitions
Base = declarative_base()

# Define the table schema
class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    enrollment_date = Column(Date)

# Function to get all students
def getAllStudents():
    # A session establishes connection with the database where you are able to query the database
    # We query the database through the session to get the entire student table then return it for printing
    Session = sessionmaker(bind=engine)
    session = Session()
    students = session.query(Student).all()
    session.close()
    return students

# Function to add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    # We add a new student to the database by inputting the above parameters
    # With session, we query using ADD then commits it
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        new_student = Student(first_name=first_name, last_name=last_name, email=email, enrollment_date=enrollment_date)
        session.add(new_student)
        session.commit()
        print("Student added successfully!")
    except IntegrityError:
        session.rollback()
        print("Error: Email already exists.")
    finally:
        session.close()

# Function to update student email
def updateStudentEmail(student_id, new_email):
    # We check the table and filter by the id, then we change the email
    Session = sessionmaker(bind=engine)
    session = Session()
    student = session.query(Student).filter_by(student_id=student_id).first()
    if student:
        student.email = new_email
        session.commit()
        print("Student email updated successfully!")
    else:
        print("Error: Student not found.")
    session.close()

# Function to delete a student
def deleteStudent(student_id):
    # We check the table and filter by the id, then we delete the student if the id exists
    Session = sessionmaker(bind=engine)
    session = Session()
    student = session.query(Student).filter_by(student_id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
    else:
        print("Error: Student not found.")
    session.close()

# Function to display menu
def displayMenu():
    print("1. Get All Students")
    print("2. Add Student")
    print("3. Update Student Email")
    print("4. Delete Student")
    print("5. Exit")

# Main function
def main():
    while True:
        displayMenu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("All Students:")
            for student in getAllStudents():
                print(student.student_id, student.first_name, student.last_name, student.email, student.enrollment_date)
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == '3':
            student_id = input("Enter student ID: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            deleteStudent(student_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
