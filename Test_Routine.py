# import re
# from tabnanny import check

# -----------------------------------------------------------#
# -----------------------------------------------------------#
# -----------------------------------------------------------#


# Employee lists #

# id_employee = []                # List - employee ID
# id_employee_counter = 1         # List - employee generate unique IDs
#
# first_name_employee = []        # List - employee first name
# last_name_employee = []         # List - employee last name
# address_employee = []           # List - employee address
# postal_code_employee = []       # List - employee postal code
# city_employee = []              # List - employee city
# country_employee = []           # List - employee country
# birthday_employee = []          # List - employee birthday
# age_employee = []               # List - employee age
# email_employee = []             # List - employee email address


# -----------------------------------------------------------#
# -----------------------------------------------------------#
# -----------------------------------------------------------#


# id_employee = []                # List - employee ID
id_employee = 1         # List - employee generate unique IDs

employee_list = []
# employee_element = []


# MENU

while True:
    print("------------------------------")
    print("|| - Employee - Program -   ||")
    print("|| (1) Create New Employee  ||")
    # print("|| (2) Create Visitor       ||")
    # print("------------------------------")
    print("|| (3) Show All Employees   ||")
    # print("|| (4) Show All Visitors    ||")
    # print("------------------------------")
    # print("|| (5) Exit Program         ||")
    # print("------------------------------")
    choice = input("Choose an option: ")

    # MENU (1) - CREATE NEW EMPLOYEE

    if choice == "1":

        # -----------------------------------------------------------#

        # FIRST NAME

        valid_chars_name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäÄöÖüÜß"
        valid_chars_address = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäÄöÖüÜß._-0123456789 "
        valid_chars_postal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZß0123456789"
        valid_chars_city = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZßäÄöÖüÜ"
        valid_chars_country = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZßäÄöÖüÜ"
        valid_chars_birthday = "0123456789."
        valid_chars_age = "0123456789"
        valid_chars_email = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäÄöÖüÜß@._-0123456789"



        # FIRST NAME

        while True:
            first_name = input("Enter First Name: ")

            if all(char in valid_chars_name for char in first_name):
                break
            else:
                print("First Name Invalid")


        # LAST NAME

        while True:
            last_name = input("Enter Last Name: ")

            if all(char in valid_chars_name for char in last_name):
                break
            else:
                print("Last Name Invalid")


        # ADDRESS

        while True:
            address = input("Enter Your Street Name and Numbers: ")

            if all(char in valid_chars_address for char in address):
                break
            else:
                print("Address invalid")


        # POSTAL CODE
        while True:
            postal = input("Enter Postal Code: ")

            if all(char in valid_chars_address for char in postal):
                break
            else:
                print("Postal Code Invalid")

        # CITY
        while True:
            city = input("Enter City: ")

            if all(char in valid_chars_city for char in city):
                break
            else:
                print("Postal City Invalid")


        # COUNTRY

        while True:
            country = input("Enter Your Country: ")

            if all(char in valid_chars_postal for char in country):
                break
            else:
                print("Country Name Invalid")

        # BIRTHDAY

        while True:
            birthday = input("Enter Your Birthday In The Format DD.MM.YYYY: ")

            if all(char in valid_chars_birthday for char in birthday):
                break
            else:
                print("Birthday Invalid")


        # AGE

        while True:
            age = input("Enter Your Age: ")

            if all(char in valid_chars_age for char in age):
                break
            else:
                print("Age Invalid")

        # EMAIL

        while True:
            email = input("Enter Your Email: ")

            if all(char in valid_chars_email for char in email):
                break
            else:
                print("Email Invalid")




        # DATA PUSH INTO LIST


        employee_list.append([id_employee, first_name, last_name, address, postal, city, country, birthday, age, email])
        id_employee += 1


    # elif choice == "2":
    #
    #     print("Choice 2 doesnt exist yet.")
    #     break



    elif choice == "3":

        if not employee_list:
            print("No employees stored yet.\n")
        else:
            # print("\nEmployee List:")
            # print("-------------------------------------------------")

            for employee_element in employee_list:
                print(f"ID: {employee_element[0]}, First Name: {employee_element[1]}, Last Name: {employee_element[2]} Address: {employee_element[3]}, Postal Code: {employee_element[4]}, City: {employee_element[5]}, Country: {employee_element[6]}, Birthday: {employee_element[7]}, Age: {employee_element[8]}, Email: {employee_element[9]}")




            # print(f"ID: {id_employee[i]}, Name: {first_name_employee[i]} {last_name_employee[i]}, Address: {address_employee[i]}, Postal Code: {postal_code_employee[i]}, City: {city_employee[i]}, Country: {country_employee[i]}, Birthday: {birthday_employee[i]}, Age: {age_employee[i]}, Email: {email_employee[i]}")
            # print("-------------------------------------------------\n")


        # print("Choice 3 doesnt exist yet.")
        # break



    # elif choice == "4":
    #
    #     print("Choice 4 doesnt exist yet.")
    #     break
    #
    #

    # elif choice == "5":
    #
    #     print("Choice 5 doesnt exist yet.")
    #     break
    #
    # else:
    #
    #     print("Invalid choice yo")

pass




