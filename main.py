import mysql.connector as ms

conn = ms.connect(host='localhost', user='root', password='enter_your_mysql_pass_here', database='hospital')
cursor = conn.cursor()

def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      name VARCHAR(255),
                      age INT,
                      gender VARCHAR(50),
                      diagnosis VARCHAR(255),
                      doctor_assigned VARCHAR(255))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      name VARCHAR(255),
                      specialization VARCHAR(255),
                      contact INT)''')

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    diagnosis = input("Enter diagnosis: ")
    doctor_assigned = input("Enter assigned doctor: ")
    query = "INSERT INTO patients (name, age, gender, diagnosis, doctor_assigned) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, gender, diagnosis, doctor_assigned)
    cursor.execute(query, values)
    conn.commit()

def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    contact = int(input("Enter contact number: "))
    query = "INSERT INTO doctors (name, specialization, contact) VALUES (%s, %s, %s)"
    values = (name, specialization, contact)
    cursor.execute(query, values)
    conn.commit()

def view_patients():
    cursor.execute("SELECT * FROM patients")
    for row in cursor.fetchall():
        print(row)

def view_doctors():
    cursor.execute("SELECT * FROM doctors")
    for row in cursor.fetchall():
        print(row)

def main():
    create_tables()
    while True:
        print("\n1. Add Patient\n2. Add Doctor\n3. View Patients\n4. View Doctors\n5. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_patient()
        elif choice == 2:
            add_doctor()
        elif choice == 3:
            view_patients()
        elif choice == 4:
            view_doctors()
        elif choice == 5:
            break

main()
conn.close()
