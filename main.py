# print('hello ')
# <------------------------------------------------------------------------------>

# arithmetic operator

# print(20*20)
# <------------------------------------------------------------------------------>

# string concatenate

# print('the sum of 4 and 4 is ' + str(8))
# print('20 days are ' + str(50) + ' minutes')
# print(f"20 days are {50} minutes")
# <------------------------------------------------------------------------------>

# variables

# calculation_to_units=24
# name_of_unit="hours"

# print(f'20 days are {20 * calculation_to_units} {name_of_unit}')
# print(f'35 days are {35 * calculation_to_units} {name_of_unit}')
# print(f'50 days are {50 * calculation_to_units} {name_of_unit}')
# <------------------------------------------------------------------------------>

# functions and variables

# these are global variables
# calculation_to_units=24
# name_of_unit="hours"

# these are local variables num_of_days custom_message
# def days_to_unit(num_of_days,custom_message):
#     print(f'{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}')
#     print(custom_message)

# days_to_unit(20,'All ok')
# days_to_unit(35,'All ok')
# <------------------------------------------------------------------------------>

# taking input from user

# calculation_to_units=24
# name_of_unit="hours"

# def days_to_unit(num_of_days):
#     return(f'{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}')
   
# user_input=input('hey user enter number of days and i will convert it into hours\n')
# user_input_number=int(user_input)
# calculated_value=days_to_unit(user_input_number)
# print(calculated_value)
# <------------------------------------------------------------------------------>

# if else conditional statements

# calculation_to_units=24
# name_of_unit="hours"

# if else condition

# def days_to_unit(num_of_days):
#     if num_of_days>0:
#        return(f'{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}')
#     elif num_of_days==0:
#        return("you have entered zero please enter valid number")
#     else:
#        return("number you have entered is invalid")    
   
# def validate_and_execute():
#    if user_input.isdigit():
#     user_input_number=int(user_input)
#     calculated_value=days_to_unit(user_input_number)
#     print(calculated_value)
#    else:
#     print('user input is not valid dont ruin my code!!!') 
    
# user_input=input('hey user enter number of days and i will convert it into hours\n')
# validate_and_execute()

# nested if else condition

# def days_to_unit(num_of_days):
   
#        return(f'{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}')
    
         
   
# def validate_and_execute():
#    if user_input.isdigit():
#     user_input_number=int(user_input)
#     if user_input_number>0:
#        calculated_value=days_to_unit(user_input_number)
#        print(calculated_value)
#     elif user_input_number==0:
#          return("you have entered zero please enter valid number")
#    else:
#     print('user input is not valid dont ruin my code!!!') 
    
# user_input=input('hey user enter number of days and i will convert it into hours\n')
# validate_and_execute()

# <------------------------------------------------------------------------------>

# try/except block

# calculation_to_units=24
# name_of_unit="hours"

# def days_to_unit(num_of_days):
   
#        return(f'{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}')
    
         
   
# def validate_and_execute():
#     try:
#         user_input_number = int(user_input)
#         if user_input_number > 0:
#             calculated_value = days_to_unit(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("You have entered zero. Please enter a valid number.")
#     except ValueError:
#         print("User input is not valid. Don't ruin my code!!!")

# user_input = input("Hey user, enter the number of days and I will convert it into hours\n")
# validate_and_execute()


# <------------------------------------------------------------------------------>
#while_loop
# calculation_to_units=24
# name_of_unit="hours"
# def days_to_unit(num_of_days):
   
#        return(f'{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}')
    
         
   
# def validate_and_execute():
#     try:
#         user_input_number = int(user_input)
#         if user_input_number > 0:
#             calculated_value = days_to_unit(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("You have entered zero. Please enter a valid number.")
#     except ValueError:
#         print("User input is not valid. Don't ruin my code!!!")
# user_input=""        
# while user_input != "exit":
#       user_input = input("Hey user, enter the number of days and I will convert it into hours\n")
#       validate_and_execute()
      
# <------------------------------------------------------------------------------>
#for_loop

# calculation_to_units=24
# name_of_unit="hours"
# def days_to_unit(num_of_days):
   
#        return(f'{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}')
    
         
   
# def validate_and_execute():
#     try:
#         user_input_number = int(num_of_days_element)
#         if user_input_number > 0:
#             calculated_value = days_to_unit(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("You have entered zero. Please enter a valid number.")
#     except ValueError:
#         print("User input is not valid. Don't ruin my code!!!")
# user_input=""        
# while user_input != "exit":
#       user_input = input("Hey user, enter the number of days comma separated list and  I will convert it into hours\n")
#       print(type(user_input.split(",")))
#       print(user_input.split(","))
#       for num_of_days_element in user_input.split(", "):
#           validate_and_execute()


#list
# my_list=["jan", "feb", "mar"]
# my_list[1]
# print(my_list[1])
# my_list.append("apr")
# print(my_list)


# <------------------------------------------------------------------------------>

# set


# calculation_to_units=24
# name_of_unit="hours"
# def days_to_unit(num_of_days):
   
#        return(f'{num_of_days} days are {num_of_days* calculation_to_units} {name_of_unit}')
    
         
   
# def validate_and_execute():
#     try:
#         user_input_number = int(num_of_days_element)
#         if user_input_number > 0:
#             calculated_value = days_to_unit(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("You have entered zero. Please enter a valid number.")
#     except ValueError:
#         print("User input is not valid. Don't ruin my code!!!")
        
        
# user_input=""        
# while user_input != "exit":
#       user_input = input("Hey user, enter the number of days comma separated list and  I will convert it into hours\n")
#       list_of_days=user_input.split(", ")
#       print(list_of_days)
#       print(set(list_of_days))
#     #   print(type(list_of_days))
#     #   print(type(set(list_of_days)))
      
  
#       for num_of_days_element in set(list_of_days):
#           validate_and_execute()


# my_set={"jan", "feb", "mar"}
# for element in my_set:
#     print(element)
    
# my_set.add("apr")
# print(my_set)

# my_set.remove("jan")
# print(my_set)

# my_set={"jan", "feb", "mar"}
# my_set.remove("jan")
# print(my_set)


# <------------------------------------------------------------------------------>