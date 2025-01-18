name = input("Enter your name: ")
dob = input("Enter your date of birth (DD-MM-YYYY): ")
address = input("Enter your address: ")
gender = input("Enter gender: ")
phone = input("Enter phone: ")

def NID(name, dob, address, gender, phone):
    print("\n--- NID Details ---")
    print(f"Name: {name}")
    print(f"Date of Birth: {dob}")
    print(f"Address: {address}")
    print(f"Gender: {gender}")
    print(f"Phone Number: {phone}")
NID(name,dob, address, gender,phone)
