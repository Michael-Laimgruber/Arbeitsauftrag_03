from Test_Routine import id_employee

# -----------------------------------------------------------#
# -----------------------------------------------------------#
# -----------------------------------------------------------#

# Employee Lists
# id_employee = []                # List - employee ID
# id_employee_counter = 1         # List - employee generate unique IDs

id_employee = 1         # List - employee generate unique IDs

employee_list = []





# -----------------------------------------------------------#
# -----------------------------------------------------------#
# -----------------------------------------------------------#

# Visitor Lists
# id_visitor = []                 # List - visitor ID
# id_visitor_counter = 1          # List - visitor generate unique IDs
#
# first_name_visitor = []         # List - visitor first name
# last_name_visitor = []          # List - visitor last name
# address_visitor = []            # List - visitor address
# postal_code_visitor = []        # List - visitor postal code
# city_visitor = []               # List - visitor city
# country_visitor = []            # List - visitor country
# birthday_visitor = []           # List - visitor birthday
# age_visitor = []                # List - visitor age
# email_visitor = []              # List - visitor email address

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

            # all function returns True or False if ->
            # -> if characters in user input "first_name_employee_temp" exist in valid_chars_name variable
            # -> if everything OK break to next input ELSE error message
            # -> repeat this for every user_input
            if all(char in valid_chars_name for char in first_name_employee):
                break
            else:
                print("First Name Invalid")


        # LAST NAME
        while True:
            last_name_employee = input("Enter Last Name: ")

            if all(char in valid_chars_name for char in last_name_employee):
                break
            else:
                print("Last Name Invalid")


        # ADDRESS
        while True:
            address_street_employee = input("Enter Your Street Name and Numbers: ")

            if all(char in valid_chars_address for char in address_street_employee):
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

    # print("-------------------------------")
    # print("Employee was successfully added")
    # print("-------------------------------")


    # DATA PUSH INTO LIST

    employee_list.append([id_employee, first_name_employee, last_name_employee, address_street_employee, postal_employee, city_employee, country_employee, birthday_employee, age_employee, email_employee])
    id_employee += 1


    # employee_list.append(id_employee)
    # employee_list.append(first_name_employee)
    # employee_list.append(last_name_employee)
    # employee_list.append(address_street_employee)
    # employee_list.append(postal_employee)
    # employee_list.append(city_employee)
    # employee_list.append(country_employee)
    # employee_list.append(birthday_employee)
    # employee_list.append(age_employee)
    # employee_list.append(email_employee)
    #
    # employee_list.append(employee_list)
    # id_employee_counter += 1
    #
    # id_employee = 1  # List - employee generate unique IDs
    #
    # employee_list = []

        # id_employee.append(id_employee_counter)
        #
        # first_name_employee.append(first_name_employee_temp)
        # last_name_employee.append(last_name_employee_temp)
        # address_employee.append(address_street_employee_temp)
        # postal_code_employee.append(postal_employee_temp)
        # city_employee.append(city_employee_temp)
        # country_employee.append(country_employee_temp)
        # birthday_employee.append(birthday_employee_temp)
        # age_employee.append(age_employee_temp)
        # email_employee.append(email_employee_temp)


    # MENU (2) - CREATE NEW VISITOR
    elif choice == "2":

        # -----------------------------------------------------------#

        # FIRST NAME VISITOR
        while True:
            first_name_visitor_temp = input("Enter First Name: ")

            if all(char in valid_chars_name for char in first_name_visitor_temp):
                break
            else:
                print("First Name Invalid")

        # LAST NAME VISITOR
        while True:
            last_name_visitor_temp = input("Enter Last Name: ")

            if all(char in valid_chars_name for char in last_name_visitor_temp):
                break
            else:
                print("Last Name Invalid")

        # ADDRESS VISITOR
        while True:
            address_street_visitor_temp = input("Enter Your Street Name and Numbers: ")

            if all(char in valid_chars_address for char in address_street_visitor_temp):
                break
            else:
                print("Address invalid")

        # POSTAL CODE VISITOR
        while True:
            postal_visitor_temp = input("Enter Postal Code: ")

            if all(char in valid_chars_address for char in postal_visitor_temp):
                break
            else:
                print("Postal Code Invalid")

        # CITY VISITOR
        while True:
            city_visitor_temp = input("Enter City: ")

            if all(char in valid_chars_city for char in city_visitor_temp):
                break
            else:
                print("City Name Invalid")

        # COUNTRY VISITOR
        while True:
            country_visitor_temp = input("Enter Your Country: ")

            if all(char in valid_chars_country for char in country_visitor_temp):
                break
            else:
                print("Country Name Invalid")

        # BIRTHDAY VISITOR
        while True:
            birthday_visitor_temp = input("Enter Your Birthday In The Format DD.MM.YYYY: ")

            if all(char in valid_chars_birthday for char in birthday_visitor_temp):
                break
            else:
                print("Birthday Invalid")

        # AGE VISITOR
        while True:
            age_visitor_temp = input("Enter Your Age: ")

            if all(char in valid_chars_age for char in age_visitor_temp):
                break
            else:
                print("Age Invalid")

        # EMAIL VISITOR
        while True:
            email_visitor_temp = input("Enter Your Email: ")

            if all(char in valid_chars_email for char in email_visitor_temp):
                break
            else:
                print("Email Invalid")




        # DATA PUSH INTO LIST VISITOR

        # id_visitor.append(id_visitor_counter)
        # first_name_visitor.append(first_name_visitor_temp)
        # last_name_visitor.append(last_name_visitor_temp)
        # address_visitor.append(address_street_visitor_temp)
        # postal_code_visitor.append(postal_visitor_temp)
        # city_visitor.append(city_visitor_temp)
        # country_visitor.append(country_visitor_temp)
        # birthday_visitor.append(birthday_visitor_temp)
        # age_visitor.append(age_visitor_temp)
        # email_visitor.append(email_visitor_temp)
        # # UNIQUE ID COUNTER +1
        # id_visitor_counter += 1


    # MENU (3) SHOW ALL EMPLOYEES
    elif choice == "3":

        if not employee_list:
            print("No employees stored yet.\n")
        else:
            # print("\nEmployee List:")
            # print("-------------------------------------------------")

            for employee_element in employee_list:
                print(f"ID: {employee_element[0]}, First Name: {employee_element[1]}, Last Name: {employee_element[2]} Address: {employee_element[3]}, Postal Code: {employee_element[4]}, City: {employee_element[5]}, Country: {employee_element[6]}, Birthday: {employee_element[7]}, Age: {employee_element[8]}, Email: {employee_element[9]}")


    # # MENU (4) SHOW ALL VISITORS
    # elif choice == "4":
    #
    #     if not id_visitor:
    #         print("-------------------------")
    #         print(" No Visitors Stored Yet. ")
    #         print("-------------------------")
    #     else:
    #         print("\nVisitor List:")
    #         print("-------------------------------------------------")
    #         for i in range(len(id_visitor)):
    #             print(f"ID: {id_visitor[i]}, Name: {first_name_visitor[i]} {last_name_visitor[i]}, Address: {address_visitor[i]}, Postal Code: {postal_code_visitor[i]}, City: {city_visitor[i]}, Country: {country_visitor[i]}, Birthday: {birthday_visitor[i]}, Age: {age_visitor[i]}, Email: {email_visitor[i]}")
    #         print("-------------------------------------------------\n")


    # MENU (5) SHOW ALL

    # elif choice == "5":
    #
    #     if not id_employee:
    #         print("-------------------------")
    #         print(" No Employees Stored Yet. ")
    #         print("-------------------------")
    #     else:
    #         print("\nEmployee List:")
    #         print("-------------------------------------------------")
    #         for i in range(len(id_employee)):
    #             print(
    #                 f"ID: {id_employee[i]}, Name: {first_name_employee[i]} {last_name_employee[i]}, Address: {address_employee[i]}, Postal Code: {postal_code_employee[i]}, City: {city_employee[i]}, Country: {country_employee[i]}, Birthday: {birthday_employee[i]}, Age: {age_employee[i]}, Email: {email_employee[i]}")
    #         print("-------------------------------------------------\n")
    #
    #     if not id_visitor:
    #         print("-------------------------")
    #         print(" No Visitors Stored Yet. ")
    #         print("-------------------------")
    #     else:
    #         print("\nVisitor List:")
    #         print("-------------------------------------------------")
    #         for i in range(len(id_visitor)):
    #             print(
    #                     f"ID: {id_visitor[i]}, Name: {first_name_visitor[i]} {last_name_visitor[i]}, Address: {address_visitor[i]}, Postal Code: {postal_code_visitor[i]}, City: {city_visitor[i]}, Country: {country_visitor[i]}, Birthday: {birthday_visitor[i]}, Age: {age_visitor[i]}, Email: {email_visitor[i]}")
    #             print("-------------------------------------------------\n")
    #

    # MENU (6) EXIT PROGRAM
    elif choice == "6":
        print("----------------------------------------------------")
        print("There Is No Exit. You Are Trapped Here Forever. Lol.")
        print("----------------------------------------------------")
        break


    # U STOOPID
    else:
        print("-----------------")
        print("Invalid choice yo")
        print("-----------------")

pass




