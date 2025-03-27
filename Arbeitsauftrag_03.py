# -----------------------------------------------------------#
# -----------------------------------------------------------#
# -----------------------------------------------------------#

# LISTS and VARIABLES
# Unique ID counter Employees
id_employee = 1

#employee_list
employee_list = []

# -----------------------------------------------------------#

# Unique ID counter Visitors
id_visitor = 1

#visitor_list
visitor_list = []


# -----------------------------------------------------------#
# -----------------------------------------------------------#
# -----------------------------------------------------------#

# Checker Variables
valid_chars_name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäÄöÖüÜß"
valid_chars_address = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäÄöÖüÜß._-0123456789 "
valid_chars_postal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZß0123456789"
valid_chars_city = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZßäÄöÖüÜ"
valid_chars_country = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZßäÄöÖüÜ"
valid_chars_birthday = "0123456789."
valid_chars_age = "0123456789"
valid_chars_email = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäÄöÖüÜß@._-0123456789"

# -----------------------------------------------------------#
# -----------------------------------------------------------#
# -----------------------------------------------------------#

# MENU LOOP (1 - 6)
while True:
    print("------------------------------")
    print("||    -     INPUT     -     ||")
    print("|| (1) Create New Employee  ||")
    print("|| (2) Create Visitor       ||")
    print("------------------------------")
    print("||    -     OUTPUT    -     ||")
    print("|| (3) Show All Employees   ||")
    print("|| (4) Show All Visitors    ||")
    print("|| (5) Show All             ||")
    print("------------------------------")
    print("|| (6) Exit Program         ||")
    print("------------------------------")
    choice = input("Choose an option: ")


    # MENU (1) - CREATE NEW EMPLOYEE
    if choice == "1":


        # FIRST NAME
        while True:
            first_name_employee = input("Enter First Name: ")
            if all(char in valid_chars_name for char in first_name_employee):
                break
            else:
                print("First Name Invalid. Only letters are allowed.")


        # LAST NAME
        while True:
            last_name_employee = input("Enter Last Name: ")
            if all(char in valid_chars_name for char in last_name_employee):
                break
            else:
                print("Last Name Invalid. Only letters are allowed.")


        # ADDRESS
        while True:
            address_employee = input("Enter Your Street Name and Numbers: ")

            if all(char in valid_chars_address for char in address_employee):
                break
            else:
                print("Address invalid")


        # POSTAL CODE
        while True:
            postal_employee = input("Enter Postal Code: ")

            if all(char in valid_chars_postal for char in postal_employee):
                break
            else:
                print("Postal Code Invalid")


        # CITY
        while True:
            city_employee = input("Enter City: ")

            if all(char in valid_chars_city for char in city_employee):
                break
            else:
                print("City Name Invalid")


        # COUNTRY
        while True:
            country_employee = input("Enter Your Country: ")

            if all(char in valid_chars_country for char in country_employee):
                break
            else:
                print("Country Name Invalid")


        # BIRTHDAY
        while True:
            birthday_employee = input("Enter Your Birthday In The Format DD.MM.YYYY: ")

            if all(char in valid_chars_birthday for char in birthday_employee):
                break
            else:
                print("Birthday Invalid")


        # AGE
        while True:
            age_employee = input("Enter Your Age: ")

            if all(char in valid_chars_age for char in age_employee):
                break
            else:
                print("Age Invalid")


        # EMAIL
        while True:
            email_employee = input("Enter Your Email: ")

            if all(char in valid_chars_email for char in email_employee):
                break
            else:
                print("Email Invalid")




        # DATA PUSH INTO LIST
        employee_list.append([id_employee, first_name_employee, last_name_employee, address_employee, postal_employee, city_employee, country_employee, birthday_employee, age_employee, email_employee])
        id_employee += 1

        # USABILITY
        print("-------------------------------")
        print("Employee was successfully added")
        print("-------------------------------")


    # MENU (2) - CREATE NEW VISITOR
    if choice == "2":


        # FIRST NAME
        while True:
            first_name_visitor = input("Enter First Name: ")
            if all(char in valid_chars_name for char in first_name_visitor):
                break
            else:
                print("First Name Invalid. Only letters are allowed.")


        # LAST NAME
        while True:
            last_name_visitor = input("Enter Last Name: ")
            if all(char in valid_chars_name for char in last_name_visitor):
                break
            else:
                print("Last Name Invalid. Only letters are allowed.")


        # ADDRESS
        while True:
            address_visitor = input("Enter Your Street Name and Numbers: ")

            if all(char in valid_chars_address for char in address_visitor):
                break
            else:
                print("Address invalid")


        # POSTAL CODE
        while True:
            postal_visitor = input("Enter Postal Code: ")

            if all(char in valid_chars_postal for char in postal_visitor):
                break
            else:
                print("Postal Code Invalid")


        # CITY
        while True:
            city_visitor = input("Enter City: ")

            if all(char in valid_chars_city for char in city_visitor):
                break
            else:
                print("City Name Invalid")


        # COUNTRY
        while True:
            country_visitor = input("Enter Your Country: ")

            if all(char in valid_chars_country for char in country_visitor):
                break
            else:
                print("Country Name Invalid")


        # BIRTHDAY
        while True:
            birthday_visitor = input("Enter Your Birthday In The Format DD.MM.YYYY: ")

            if all(char in valid_chars_birthday for char in birthday_visitor):
                break
            else:
                print("Birthday Invalid")


        # AGE
        while True:
            age_visitor = input("Enter Your Age: ")

            if all(char in valid_chars_age for char in age_visitor):
                break
            else:
                print("Age Invalid")


        # EMAIL
        while True:
            email_visitor = input("Enter Your Email: ")

            if all(char in valid_chars_email for char in email_visitor):
                break
            else:
                print("Email Invalid")




        # DATA PUSH INTO LIST
        visitor_list.append([id_visitor, first_name_visitor, last_name_visitor, address_visitor, postal_visitor, city_visitor, country_visitor, birthday_visitor, age_visitor, email_visitor])
        id_visitor += 1

        # USABILITY
        print("-------------------------------")
        print("Employee was successfully added")
        print("-------------------------------")


    # MENU (3) SHOW ALL EMPLOYEES
    elif choice == "3":
        if not employee_list:
            print("No employees stored yet.\n")
        else:
            print("\nEmployee List:")
            print("-------------------------------------------------")
            for employee_element in employee_list:
                print(f"ID: {employee_element[0]}, First Name: {employee_element[1]}, Last Name: {employee_element[2]}, Address: {employee_element[3]}, Postal Code: {employee_element[4]}, City: {employee_element[5]}, Country: {employee_element[6]}, Birthday: {employee_element[7]}, Age: {employee_element[8]}, Email: {employee_element[9]}")
            print("-------------------------------------------------\n")


    # MENU (4) SHOW ALL VISITORS
    elif choice == "4":
        if not visitor_list:
            print("No visitors stored yet.\n")
        else:
            print("\nVisitor List:")
            print("-------------------------------------------------")
            for visitor_element in visitor_list:
                print(f"ID: {visitor_element[0]}, First Name: {visitor_element[1]}, Last Name: {visitor_element[2]}, Address: {visitor_element[3]}, Postal Code: {visitor_element[4]}, City: {visitor_element[5]}, Country: {visitor_element[6]}, Birthday: {visitor_element[7]}, Age: {visitor_element[8]}, Email: {visitor_element[9]}")
            print("-------------------------------------------------\n")


    # MENU (5) SHOW ALL
    elif choice == "5":

        if not employee_list:
            print("No employees stored yet.\n")
        else:
            print("\nEmployee List:")
            print("-------------------------------------------------")
            for employee_element in employee_list:
                print(f"ID: {employee_element[0]}, First Name: {employee_element[1]}, Last Name: {employee_element[2]}, Address: {employee_element[3]}, Postal Code: {employee_element[4]}, City: {employee_element[5]}, Country: {employee_element[6]}, Birthday: {employee_element[7]}, Age: {employee_element[8]}, Email: {employee_element[9]}")
            print("-------------------------------------------------")


        if not visitor_list:
            print("No visitors stored yet.\n")
        else:
            print("\nVisitor List:")
            print("-------------------------------------------------")
            for visitor_element in visitor_list:
                print(f"ID: {visitor_element[0]}, First Name: {visitor_element[1]}, Last Name: {visitor_element[2]}, Address: {visitor_element[3]}, Postal Code: {visitor_element[4]}, City: {visitor_element[5]}, Country: {visitor_element[6]}, Birthday: {visitor_element[7]}, Age: {visitor_element[8]}, Email: {visitor_element[9]}")
            print("-------------------------------------------------\n")


    # MENU (6) EXIT PROGRAM
    elif choice == "6":
        print("----------------")
        print("Have a nice day.")
        print("----------------")
        break


    # INVALID CHOICE
    else:
        print("---------------")
        print("Invalid choice.")
        print("---------------")

pass




