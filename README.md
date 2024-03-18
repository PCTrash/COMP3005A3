# COMP3005A3

Link to Video: https://youtu.be/CV2pNrTLRBs

Steps to Run the Program

1. Create the Database in pgAdmin 4
2. Right-click the database that you just made and click "Query Tool"
3. Create the table with this command:
   
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

5. Add the initial data into the database with this command:

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

6. Make sure python is installed, as well as "sqlalchemy" and "psycopg2".
7. The commands to download sqlalchemy in windows cmd are "pip install sqlalchemy", to install psycopg2 use "pip install psycopg2".
8. Open the assignment3.py file in an editor like VSCode.
9. Under the DATABASE_URL section, input the necessary parameters to connect to the database, your username, password, and the database name.
10. Run the code and follow the menu on screen to make changes to the database.
11. To verify any of the changes were made go to pgAdmin 4 and use the query: "SELECT * FROM students" this will show the table
