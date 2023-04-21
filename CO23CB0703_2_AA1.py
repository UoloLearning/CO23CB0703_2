def check_attendance(roll_number):
    # For the purpose of this example, let's just return "Present" for even roll numbers and "Absent" for odd roll numbers.
    if roll_number % 2 == 0:
        print(f"Attendance status for roll number {roll_number}:","Present")
    else:
        print(f"Attendance status for roll number {roll_number}:","Absent")
        
roll_number = int(input("Enter the roll number : "))
check_attendance(roll_number)
