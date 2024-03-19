# 1. Python Indentation Practice with if Statements
# Task 1: Code Correction
weather = "sunny"
#error with indentadtion on line 6,8 corrected
if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")


# Task 2: Your Mood Today
    mood = "happy"
if mood == "happy":
    print("That's great to hear!")
else:
    print("I hope your day gets better!")


# 2. Python Naming Convention Practice
    #fixed error in variable names as we use snake_case
        #removed (<span class="hljs-number">x</span>) from code line >> is not python code 
pi_value = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000


#3. Python Data Types and type() Function
    #identifying the data type of each variable
variable_a = "Hello, World!"
# class string ()
print (type(variable_a)) #confirm type
variable_b = 23
# class integer ()
print(type(variable_b)) #confirm type
variable_c = 3.14
#class float ()
print(type(variable_c)) #confirm type
variable_d = True
#class boolean ()
print(type(variable_d)) #confirm type


# 4. Arithmetic Operations in Daily Life
# Task 1: Grocery Store Math
amount = float(water_case + cat_food + redbull)
water_case = 4.99
cat_food = 35.99
redbull = 12.99
#calculated the total rounded amount to the nearest hundredth
rounded_total = round(amount, 2)
print("your total amount is", rounded_total) 


#Task 2: Bank Interest
savings = int(10000)
interest = .07
print("total amount saved", savings*interest+savings) #output should be 700 + 10000


# 5. Understanding Assignments and Comparisons
# Task 1: Value Swapping
a = 2
b = 4
#swapping the two values
print("a =" , b) # output should be 4
print("b=", a) # output should be 2