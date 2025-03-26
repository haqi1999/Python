import random # This is called a module. In C++ its called a library This one is used for the random number function

# Comments use hashtag
# Python will execute from top to bottom (Control Flow)

# Using double quotes or single quoted print should show the same thing
print ("There is a world") 

# Python will use the most recent input in the variable of the same name.
# Example belows "Meat" as the latest and will be the final output. But it will still print the previous output in the previous line Remember to create a new print after new each variable used in the print
# The new print will NOT USE THE NEW VARIABLE if the new variable is updated AFTER THE new print.
meal = "An english muffin"
# Printing out breakfast
print ("Breakfast:")
print (meal)
# Now update meal to be lunch!
meal = "chicken"
meal = "lunch"
# Printing out lunch
print ("Lunch:")
print (meal)
# Now update "meal" to be dinner
meal = "Meat"
print ("Dinner:")
print (meal)

# SyntaxError = Something in the program is wrong 
# NameError = Python sees a word that it does not recognise (i.e Undefined variable)
# TypeError = When an operation is applied to an object of an innapropriate type

# ---------------------------------------------- Variables --------------------------------------------------------------
# When defining a variable, you dont have to assigned a data type variable with the variable name itself like in C++, Instead just create the name of the variable with the data stored
an_int = 2
a_float = 2.1 
a_double = 2.121212313
print (an_int)
print (an_int + a_float + a_double)


leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
""" # Multiline Strings use 3 quotation marks

# Boolean Variables
# DONT USE QUOTATION MARKS for boolean variables
set_to_true = True
set_to_false = False
bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

print(bool_one)    # True

print(bool_two)    # False

print(bool_three)  # True


# Generating a random number from 1-9 and storing it in random_number variable
random_number = random.randint(1,9)

# ---------------------------------------------------- Strings -----------------------------------------------------------
# \ Escape characted can be used to edit string to ensure that it is concatenated properly if the user fogot to close it with ""
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

# Iterating through string
def get_length(word):
  counter = 0;
  for letter in word:
    counter += 1
    print(counter)
  return counter

favorite_color = get_length ("blue")

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

# That takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
# The "in" operator checks part of one string is inside another (Outputs true and false)
def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common


# String Methods
# NB: String methods CREATES new strings and not modify them
# for split(), you can use \n and \t for Newline & Horizontal Tab respectively
favorite_song = 'SmOoTH'
featuring = "           rob thomas                 "
with_spaces = "You got the kind of loving that can be so smooth"
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
favorite_song_lowercase = favorite_song.lower()
favorite_song_uppercase = favorite_song.upper()
favorite_song_title = favorite_song.title()
favorite_song_split = favorite_song.split() # Any string input arguement is acceptable. It will split the string at the input arguement
reapers_line_one = " ".join(reapers_line_one_words) # Important to create a space between quotation marks to create space between the words in the lists
removing_spaces_strip = featuring.strip()
with_underscores = with_spaces.replace(' ', '_') # Replaces the 1sts inpurt arguement with the 2nd
print('smooth'.find('t')) # Finds an index of the string

# Example use of .format()
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)
print(favorite_song_statement("Smooth", "Santana"))

# Example use of format but with labelling. In Labelling you don't have to put it in order for it to work as long as you label it.
def favorite_song_statement(song, artist):
  return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

# Good Example of utiling split function, Splits at ','
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
print(author_names)

# Iterates for each elements 
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)

# Poems Project 
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

# Removes unnecessary spaces
highlighted_poems_stripped = [];
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
print( " Stripped highlighted poems", highlighted_poems_stripped)

highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split (':'))
print(highlighted_poems_details)

titles = []
poets = []
dates = []
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
print(titles)
print(poets)
print(dates)

for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
# --------------------------------- Mathematical Operations & String/Integer Concatenation --------------------------------
# NB : A variable cannot be multipled/divided by a number.
coffee_price = 1.50
number_of_coffees = 4
greeting_text = "Hey there! "
question_text = "How are you doing?"
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
number_of_miles_hiked = 12
hike_caption = "What an amazing time to walk through nature!"


print(coffee_price * number_of_coffees)
full_text = greeting_text + question_text # String concatenation
print(full_text) 
full_birthday_string = birthday_string + str(age) + birthday_string_2 # Concatenating an integer with strings is possible if we turn the integer into a string first
print(full_birthday_string) 
print(birthday_string, age, birthday_string_2) # This also prints "I am 10 years old today!"
print(birthday_string, "10", birthday_string_2) # This also prints "I am 10 years old today!"

print (25 * 68 + 13 / 28)
print(2 ** 10) # 2 to the 10th power, or 1024
print(29 % 5) # Prints 4 because 29 / 5 is 5 with a remainder of 4. If no remainder then will print out 0. Useful for performing an action every nth term

number_of_miles_hiked += 2 # Adds 2 from the old variable
print (number_of_miles_hiked)
hike_caption += " #nofilter" # Adds #nofilter from the old variable as a string concatenation
hike_caption += " #blessed"  # Adds #blessed" from the old variable as a string concatenation
print (hike_caption)

# --------------------------------------------------- User Input --------------------------------------------------------
# VariableName = input("question for interaction with the user")
likes_snakes = input("Do you like snakes? ") 
print("Does Haqi likes snakes? " + likes_snakes)

# ------------------------------------------------ Control Flow/Logic ---------------------------------------------------
# == Equals
# != Not Equals
# > Greater than
# >= Greater or equal to
# < Less than 
# <= Less than or equal to
# and Both needs to be true
# or Only one side needs to be true. 
# // floor division, returns nearest whole number or integer, which is less than or equal to the normal division result

# If Statements
# NB : the elif (else if) and the else should be at the same indentation as the if.
# Dont forget the colon after the condition
# In an else statement, there shouldnt be a condition since it is the final.
# If not is basically saying if the reverse of the condition occurs. elif not exist too.
# return can be applied after each statement to produce the result.
user_name = "angela_catlady_87"
credits = 120
gpa = 1.8

if user_name == "Dave":
  print("Get off my computer Dave!")
elif user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")
else:
  print("I know it is you, Dave! Go away!")

if not credits >= 120: 
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")

# ------------------------------------------------ Lists ---------------------------------------------------
# List is sequential 
# .append() allows addition to the list a the end of the list. Only takes 1 input arguement
# .remove() allows removal of the literally input arguement. Use quotation for strings. 
# .remove() will remove only 1 of the dupilcated elements in the list. Prioritises 1st instance
# .count() count the number of occurences of an element in a list
# .insert() insert an element into a spefic index of list (index,element inserted)
# .pop() remove an element from a specific index or from the end of list (index)
# range(start,end,increment of) create a sequence of integers. range(10) creates 0-9.
# len(list) get length of a list. Specifically number of elements on that list NOT INDEX
# .sort() sort the original list and returns none. Thus if applied into a variable, will return None. Just print the original list name to get the sorted list.
# sorted(list) same as sort but CREATES A NEW LIST of the list that is sorted. Can be put into a new variable.
# list(range) creates a list from the range created
# zip() function allows combining data sets without the needing to rely on multi-dimensional lists. Makesure to use the list() function afterwards to change it from memory address to the actual elements contained that have been combined.
# NB the list created using zip() and list is actually a TUPLE
# Only the same data type can be "+" together.
# Indexing start with 0 and uses []. Must use int not float. By using int() function to forcefully remove decimals.
# Negative indexing start with -1, reads from the last.


heights = [61, 70, 67, 64, 65]
mixed_list_common = ["Mia", 27, False, 0.5]
empty_list = []
emtpylist2 = list()

append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')

print(append_example)

example_list = [1, 2, 3, 4]

#Using Append adds  the number 5 
example_list.append(5)
print(example_list)

#Using Remove, below removes the number 2 NOT INDEX 2. Use quotation marks to remove string
example_list.remove(2) 
print(example_list)

# Adding more than 1 data to the list to a pre-existing lists
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
print (items_sold_new[1])

# Negative indexing. Prints out tart
print (items_sold_new[-1]) 

# Modifying lists
items_sold_new [0] = "fruits"
print(items_sold_new)

# 2D Lists
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]
noelles_height = heights[0][1] 
get_ava = heights [1][0] 
mia_height = heights [-1][-1]
print(noelles_height)
print(get_ava)
print(mia_height)

heights_final = heights + [["Noelle", 61], ["Haqi",70]]
print(heights_final)

tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]
for row in tic_tac_toe:
    for column in row:
        print(column + " ", end='') # end= stops the code from going to the next line
    print()

# Example of using range printing from 0-9
my_range = range(10) 
print(my_range)
# 2-8 range printed below, Notice how the start number is the same as the input arguement unlike the end number
my_list = range(2, 9) 
# The list function is required here to create the list from the range 0-9
print(list(my_list)) 
print(list(my_range)) 
# Each number is greater than 2 than the previous number example [2,4,6,8]
my_range2 = range(2, 9, 2)
print(list(my_range2))

# Good example of range
examples = ['red', 'green', 'blue', 'orange']
# This will print 4 which is the number of elements in examples.
print(len(examples))
# This will return a list ([0, 1, 2, 3]) which provides indexes to the examples.
for color in range(len(examples)):
   print(examples[color])
for color in range(4):
    print(examples[color])

# Slicing list
# NB: It will extract from starting number to the number before the end and uses indexing extraction
# Just take not of the colon position (How we extract things in MATLAB Too)
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
middle = suitcase[2:4] 
print(middle)
print(suitcase[:3]) # Take Firts :n elements (Normal Indexing)
print(suitcase[-3:]) # Take Last -n: elements (Like Inverse Indexing)
print(suitcase[:-1]) # All element but not the last element

# Sorting
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort() # Alphabetical
print(names) 
names.sort(reverse=True) # Reverse
print(names)
sorted_names = sorted(names) # Inserted in a variable
print(sorted_names)

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6] # Not including the element that is on the indexed 6
inventory_2_7 = inventory[2:7]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10,"19th Century Bed Frame")
inventory.sort()
print(inventory)
print(removed_item)
print(inventory_2_6)
print(inventory_2_7)

# Example of list comprehension using for loop 
# new_list = [<expression> for <element> in <collection>]
# NB Square brackets.
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
grade_above_80 =  [grade for grade in grades if grade > 80]
print (scaled_grades)
print (grade_above_80)

# Example of list comprehension using for and if statements
# Notice the differcen
numbers = [2, -1, 79, 33, -45]
no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]

# A Good Example of List in Medical Records
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

names.append("Priscilla")
insurance_costs.append(8320.0)
print(names)
print(insurance_costs)

medical_records_unlisted = zip(names,insurance_costs)
print (medical_records_unlisted)
medical_records = list(zip(names,insurance_costs))
print(medical_records)
num_medical_records = len(medical_records)
print (num_medical_records)

print ("There are",num_medical_records,"medical records" )
first_medical_record = medical_records[0]
print ("Here is the first medical record:", first_medical_record)

# lamda is a function that takes x as its input arguement
# x represents the tuple in the list. In this case (name,cost)
# sort the values in the 1 index in order (In this case its the insurance cost)
medical_records.sort(key=lambda x: x[1])
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

cheapest_three =  medical_records [:3]
print ("Here are the three cheapest insurance costs in our medical records:",cheapest_three)
priciest_three =  medical_records [-3:]
print ("Here are the three most expensive insurance costs in our medical records:",priciest_three)
occurrences_paul = names.count("Paul")
print (occurrences_paul)

# A Good Example use of List, If,Elif
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]


total_cost = 0;
for cost in actual_insurance_costs:
  total_cost += cost
print (total_cost)

average_cost = total_cost/len(actual_insurance_costs)
print ("Average Insurance Cost:" , average_cost )


for i in range(len(names)):
  name = names [i]
  insurance_cost = actual_insurance_costs[i]
  print ("The insurance cost for", name, "is", insurance_cost," dollars.")
  if insurance_cost > average_cost:
    print ("The insurance cost for",  name , "is above average.")
  elif insurance_cost < average_cost:
    print ("The insurance cost for",  name , "is below average.")
  else:
    print ("The insurance cost for",  name , "is equal to the average")

updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs ]
print (updated_estimated_costs)


# ------------------------------------------------ Tuples ---------------------------------------------------
# Similar to Lists, but you cant change anything to it or you cant modify it.
# Instead of square brackets, you use normal bracket parantheses ()
# you can extract the tuples contents by using named variables respectively
# NB you can create one element tuple by using the trailing coma beside the element . I.e) name = (4,)

# Example of a tuple
my_info = ("Haqi",24,"Indonesia")
# Extracting data from tuple A.k.a Unpacking
name,age,country = my_info
print (name)
print (age)
print (country)

# Using zip() function. Can be 2 or more lists
namess = ["Jenny", "Alexus", "Sam", "Grace"]
heightss = [61, 70, 67, 64]
combine_namess_heightss = zip(namess,heightss)
print(combine_namess_heightss) # this will show the location a.k.a the memory address of the TUPLES FORMAT combined
print(list(combine_namess_heightss)) # This will show the actual lists but in TUPLES FORMAT combined. Shown in termminal by the parantheses and not the square brackets

# ------------------------------------------------ Loops ---------------------------------------------------
# Indefinite iteration = number of times the loops is executed depends on how many conditions are met
# Definite iteration = number of times the loops is executed is defined advanced

# For loops
# The temporary variable is the elements inside the list.
# The temporary variable represent the actual values in the list itself
# The name of the temporary varible will not affect the content of the variable itself but it is better for you to name it in a way that it makes relation to the actual data
"""
for <temporary variable> in <list of length>:
     <action>
"""
sport_games = ["football", "hockey", "baseball", "cricket"]
for i in sport_games:
  print(i)

# In this case, temp is used to track the number of loops is executed. +1 Because range starts at 0-5.
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))

# One line operation of for loop
for i in sport_games: print(sport_games)

# Example of using break, stops loop at break at that iteration after printing it
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
print("End of search!")

# Example of using continue , skips the current iteration
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i <= 0:
    continue
  print(i)

# While loops
# Identation is important. If the identation is the same as While, it will recognise it outside the loop
"""
while <conditional statement>:
  <action>
"""
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1

# Example of a one line operation of while loop
while count <= 3: print(count); count += 1

# Nested loops
# Loop through each sublist
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)

#-----------------------------------------Functions--------------------------------------------------------------------
# Built in and User-defined functions
# You can access the variables inside a function once the function has been called outside of ot
def calculate_expenses(plane_ticket_price,car_rental_rate,hotel_rate,trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price

  return trip_total

# Step 5: call your function
print(calculate_expenses (200,100,100, 5))


def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )

# The following is the use of keyword arguements where the order of input of arguements is not the same as the order of the parameter in the function itself.
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100) 

# Example of the use of default value. In this case Codeacademy HQ will be outputed if no input arguements is inserted when calling the function.
def trip_planner(first_destination,second_destination,final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print ("First, we will stop in" , first_destination, "then" ,second_destination, "and lastly" ,final_destination)
first_trip = trip_planner("Brooklyn", "Queens")

# Multiple returns example using commas and extracting the respective returns
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']
def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day

monday, tuesday, wednesday = threeday_weather_report(weather_data)
print(monday)
print(tuesday)
print(wednesday)

# Example of using if, else, function etc
def analyze_smoker(smoker_status):
  if smoker_status == 1 :
    print("To lower your cost, you should consider quitting smoking");
  else: 
      print("Smoking is not an issue for you.")
  return smoker_status

 
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

# lambda is a single line function
# Suitable if you only need to use the function once
# <WHAT TO RETURN IF STATEMENT IS TRUE> if <IF STATEMENT> else <WHAT TO RETURN IF STATEMENT IS FALSE>
add_two = lambda my_input: my_input + 2
print (add_two(100))

# Checking if the inputted string is a substring of the main string
is_substring = lambda my_string: my_string in "This is the master string"
print(is_substring('I')) # false
print(is_substring('am')) # false
print(is_substring('the')) # true
print(is_substring('master')) #true

# A lambda function where grade is the input and check_if_grade is the name of the function
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'

contains_a= lambda word : "a" in word
print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))

long_string = lambda str : len(str) > 12
print(long_string("short")) # false
print(long_string("photosynthesis")) #true

# lambda function with if statements
add_or_subtract = lambda input_number: input_number - 1 if input_number >= 0 else input_number + 1

# using random.radint to produce number between (a,b) inclusively.
import random
#Write your lambda function here
add_random = lambda num : num + random.randint(1,10)
print(add_random(5))
print(add_random(100))

# Get a last name from a pre-existing name column using lambda function
get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

# Good Example of using if and else statement with the application of lambda function
# the apply function takes a function as an input and apply it to the DataFrame. Axis = 1 relates to along columns

df = pd.read_csv('employees.csv')
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
  if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
df['total_earned'] = df.apply(total_earned, axis = 1)
print(df)

#----------------------------------------- Dictionaries --------------------------------------------------------------------
# A dictionary is a set of unordered key : value . Made with curly brackets
# Each keys cannot be dupilcated. But several keys can have the same value associated with them
# Keys can be String or Numbers. While value can be anything.
# Dictionaries in Python rely on each key having a hash value, a specific identifier for the key
# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default
# .pop() works to delete items from a dictionary, when you know the key value
# .keys() method that returns a dict_keys. dict_keys object is a view object. Cannot be edited. Returns a dict_list
# .values () method returns the values in a dictionary. Returns a dict_list
# The difference is that keys() is a view object and reflects state of dictionary even if dictionary is updated. The list() function creates a list that does not update with the source dictionary.
# .items() extract the key & values and return it as tuples ()
# NB : Using in fuction for a dictionary will check the KEY ONLY if it exist or not in the dictionary itself
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry" : 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print(sensors)

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

# Example of adding key & values to a dictionary
# Use the update function to add multiple key : values
# {'Paris': 100, 'London': 75, 'New York': 83, 'Vancouver': 110}
locations = {}
locations['Paris'] = 100
locations.update({"London": 75})
locations.update({"New York": 83, "Vancouver" : 110}) 
print(locations)
print (locations ['Paris']) # Prints 100

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

# Using .get() function to create an output as it default value if the key is not in the specified dictionary 
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
print(building_heights.get('Shanghai Tower', 0)) # Prints 632
print(building_heights.get('Mt Olympus', 0)) # Prints 0
print(building_heights.get('Kilimanjaro', 'No Value')) # Prints 'No Value'

# Removes the key:value from available items and add the value to the health points, Used in Games
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
for student in test_scores.keys():
 print(student)
for scores in test_scores.values():
  print(scores)

# The 2 for loops wil print the same result
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for key, value in pct_women_in_occupation.items():
  print ("Women make up" , value , "percent of",key,"s")
for data in pct_women_in_occupation.items():
  print ("Women make up" , data[1] , "percent of",data[0],"s")


#---------------------------------------------------------- FILES --------------------------------------------------------------------------------------------------------
# The "with" is a context manager. responsible for opening and closing the file once we are done with that specific line
# It closes the file again so it wouldnt effect the performance of the code.
# CSV ~ Comma Separated File
# Parsing ~ to make something understandable
# JSON ~ JavaScript Object

# Old way of opening a file. this doesnt close the txt and can effect the performance of the code
# Has to be closed manually
fun_cities_file = open('fun_cities.txt', 'a')
fun_cities_file.close()

# .read() reads the txt file as a whole instantly
with open('welcome.txt') as text_file:
  text_data = text_file.read()
print (text_data)

# .readlines() reads each line seperately and print it seperately. its READLINE"S"
with open("how_many_lines.txt") as lines_doc:
  for lines in lines_doc.readlines():
    print (lines)
# .readline() only reads one line sequentially
with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
print (first_line)

# Writing the text "ONE D" into the "bad_bands.txt".
# "w" ~ write mode. in default it is "r" ~ read only mode
# NB: using the "w" option overwrites what ever is in the file itself
with open("bad_bands.txt","w") as bad_bands_doc:
  bad_bands_doc.write("ONE D")

# "a" ~ append, adding a text without overwritng the file inside it 
# \n ~ prints on a new line 
with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("\n... and it still is")

# Uses csv library in csv.DictReader to convert lines of CSV to Python Dictionaries
# Accessing all rows using row[] function with a key value of "Cool Fact"
import csv
with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])

# Using delimeter in the csv.DicReacder to indicate where the different values start and stop
import csv
with open("books.csv") as books_csv:
   books_reader = csv.DictReader(books_csv, delimiter='@')
   isbn_list = []
   for rows in books_reader:
    isbn_list.append(rows["ISBN"])
    print(rows["ISBN"])

# Creating CSV File from a list and files
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv,fieldnames = fields)
  log_writer.writeheader()
  for row in access_log :
    log_writer.writerow(row)

# Dealing with JSON File 
# Readidng JSON
import json
with open("message.json") as message_json:
  message = json.load(message_json)
print(message['text'])

# Writing JSON file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json
with open("data.json", "w") as data_json:
  json.dump(data_payload, data_json)

#---------------------------------------------------------- NumPy & Pandas --------------------------------------------------------------------------------------------------------
# Pandas ~ Library working with data
# NumPy ~ Facillitates efficient numerical operations, Pandas is bulit on top of NumPy
# Series is 1D
# A series object is more useful than an array due to the ablity of it to customise indices
# DataFrame ~ Similar to Matrix as it contains rows and columns. Both rows and columns can be indexed with integers or String Names
# One DataFrame can contain many different types of datam but within a column, everything has to be the same data type


import numpy as np
import pandas as pd

# From list to 1D ndarray
# Output : [1 2 3 4]
list1 = [1,2,3,4]
array1 = np.array(list1)
print(array1)
print(len(array1))
print(list1)

# List to 2D
# [[1 2 3]
#  [4 5 6]]
list2 = [[1,2,3],[4,5,6]]
array2 = np.array(list2)
print(list2)
print(array2) #Matrix


# Customising the indices of 
# Emma    |  13
# Swetha  |  25
# Serajh  |  19
dtype: int64
ages = np.array([13,25,19])
series1 = pd.Series(ages,index=['Emma', 'Swetha', 'Serajh'])
print(series1)

# Example of DataFrame filled with Python Lists
dataf = pd.DataFrame([
    ['John Smith','123 Main St',34],
    ['Jane Doe', '456 Maple Ave',28],
    ['Joe Schmo', '789 Broadway',51]
    ],
    columns=['name','address','age'])
print(dataf)
#           name      |   address     |   age
# 0    | John Smith   | 123 Main St   |   34
# 1    | Jane Doe     | 456 Maple Ave |   28
# 2    | Joe Schmo    | 789 Broadway  |   51

# Customising the indices and change it to names
dataf.set_index('name')
#   name      |   address     |  age
# John Smith   | 123 Main St   |   34
# Jane Doe     | 456 Maple Ave |   28
# Joe Schmo    | 789 Broadway  |   51

# Using pd.DataFrame using dictionary key:value format. Key = Column Name, Value = Values inside the column
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  "Product Name" : ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  "Color" : ["blue","green", "red", "black"]
})
print(df1)

# Using pd.DataFrame to create DataFrame using lists, Advantage of this is the order printed can be controlled unlike using dictionary
df2 = pd.DataFrame([[1, 'San Diego', 100],[2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
[3, "San Francisco", 90], [4, "Sacramento", 115]],
  columns=["Store ID", "Location", "Number of Employees"])
print(df2)

# Ways to open csv and load it into a DataFrame
# df = a variable name acronym from DataFrame   
df = pd.read_csv('my-csv-file.csv')
df.to_csv('new-csv-file.csv')

# Load the first 5 rows in default not including the header . Specify number of rows as an input arguement if you want to see more or less
print(df.head())

# Shows the types of data and memory load of the DataFrame
print(df.info())

# To find type of data in df. Series/DataFrame etc
print(type(df))

# Extracting columns from df and rows
# .iloc[2:4] extracts row 2 to 3 and exluding 4
# isin.([]) Extract rows that contains the input list arguement
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],     
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',p
           'clinic_west'])

clinic_north_south_columnsSelection = df[["clinic_north",'clinic_south']]
March_RowSelection = df.iloc[2]
March_To_May_RowsSelection = df.iloc[2:5]
january_row= df[df.month == "January"]
march_april = df[(df.month == 'March')|(df.month == 'April')] # Print march or april
january_february_march = df[df.month.isin(['January','February','March'])] 
print(df)
print(March_RowSelection)
print(March_To_May_RowsSelection)
print(january_row)
print(january_february_march)

df2 = df.loc[[1, 3, 5]]
df3 = df2.reset_index() # Reset the index and store it as a new df in df3
print(df3)
df2.reset_index(inplace = True, drop = True) # Reset the existing index df2 using inplace = True
print(df2)

# Adding a new column with the header as "Sold in Bulk?"
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

 # df.insert(2, 'new-col', data) ~ This is for inserting a column of data in a specific positon of the matrix
df["Sold in Bulk?"] = ["Yes","Yes","No","No"]
# Adding a column with the same value for all rows
df["Is taxed?"] = "Yes" 
# Using columns inside the df to create a new column from the pre-existing values
df['Margin'] = df['Price'] - df['Cost to Manufacture']
print(df)


df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Inserting a new column with the application of other existing column values. In this case "Name"
df['Lowercase Name'] = df.Name.apply(str.lower)

# Changing column names to a pre-existing df using .columns()
df.columns = ["ID", "Title","Category","Year Released", "Rating" ]

# Renaming specific columns using .rename(). More preferable as it specifies more than .columns()
# inplace = True ensures that we are modifying the existing df and not creating a new one
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18] 
})
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)


# In this case, "shoe_material" data will be the input in the lambda function.
orders = pd.read_csv('shoefly.csv')
print(orders.head(5))
orders['shoe_source'] = orders.shoe_material.apply(lambda x:	'animal' if x == 'leather'else 'vegan')
orders['salutation'] = orders.apply(lambda row: 'Dear Mr. ' + row['last_name'] if row['gender'] == 'male' else 'Dear Ms. ' + row['last_name'], axis=1)

  """""
  Commands and description for dataframes. Named as aggregate functions
mean	Average of all values in column
std	Standard deviation
median	Median
max	Maximum value in column
min	Minimum value in column
count	Number of values in column
nunique	Number of unique values in column
unique	List of unique values in column

groupby Groups the column as one rather than using loop to iterate for each row. 
df.groupby('column1').column2.measurement() ~ Creates a new series. 
df.groupby('column1').column2.measurement().reset_index()  creates a new df
i.e) df.groupby('student').grade.mean()
Example of application : They want to know the most expensive shoe for each shoe_type

df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
Calculate the average sales for each store on each day of the week across multiple months

NB: usually to find the number of counts, we can use the id column and reset_index to create a new index for the new df created.
"""

# np.percentile can calculate any percentile over an array of values
high_earners = df.groupby('category').wage.apply(lambda x: np.percentile(x, 75)).reset_index()

# Pivtoting a table ~ changing how the table looks after extracting the data
shoe_counts_pivot = shoe_counts.pivot(
    columns='shoe_color',
    index='shoe_type',
    values="id").reset_index()

# Example of merging 2 data frames
# NB : Looks at matching columns, then matching rows.
sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales,targets)
print(sales_vs_targets)
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

# Chain of command of merging 2 Data Frames
# Merge orders to customers df, then merge it with products
big_df = orders.merge(customers).merge(products)

# Renaming column of a df to match the required merging columns title 
orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders,products.rename(columns={'id' : 'product_id'}))

# Another example of merging to specified columns using left on, right on an suffixes
# Its basically saying merge the product id from orders to id in products. Suffixes to prevent confusion in the new df
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

orders_products = pd.merge(
	orders,
	products,
	left_on = 'product_id',
	right_on = 'id',
	suffixes = ['_orders', '_products']
)

# Inner merge : merging two DataFrames whose rows don't match perfectly, we lose the unmatched rows
# Outer Join : merging two DataFrames which will include all rows from both tables, even if they don't match. Any missing values are filled in with None or NaN
# If the merge function is used and the how parameter is not inputted, by default an inner merge will be done.
# pd.merge(company_a, company_b, how='outer')
# Replaces all nan values with 0
# df.fillna(0, inplace=True)
# Left Merge : A Left Merge includes all rows from the first (left) table, but only rows from the second (right) table that match the first table
# Right Merge : Right merge is the exact opposite of left merge
# pd.concat([]) concatenates 2 data frames with the same columns. 
# Exploratory Data Analysis (Data inspection, Numerical Summarisation, Data Visualisation)

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_left = pd.merge(store_a ,store_b, how ="left" )
store_b_a_left = pd.merge(store_b,store_a , how ="left")
print(store_a_b_left)
print(store_b_a_left)

menu = pd.concat([bakery,ice_cream])

# Good Example of merge
# Part 1: print to inspect each DataFrame
print(visits.head(10))
print(checkouts.head(10))

# Part 2: merge visits and checkouts
v_to_c = pd.merge(visits, checkouts)

# Part 3: define the column time to be the different between checkout time and visit time
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time
print(v_to_c.time.mean())

# categorical variables (can be strings, numbers as long as it is classfied as a category values)
# numerical variables (has to be numbers)

# Types of categorical variables
# 1) Nominal Variable ~ Describes something (Zip codes, user ids, yellow, blue, hot, cold) (Store is as string)
# 2) Ordinal Variable ~ Have an inherent ranking (1st. 2nd. 3rd) (Store it as objects)
# 3) Binary Variables ~ Have only 2 variable variations (Yes,No,True,False, On,Off) (Store it as bool)

# Types of Numerical Variables
# 1) Continuous (Measurements) ~ Length, Time, Temperature (Store it as float data type)
# 2) Discrete (Counts) ~ Peoples, Cars, Dogs (Store is at integers)

# changing the id data type in cereal data to a string
# cereal['id'] = cereal['id'].astype("string")
# print(cereal.dtypes) (Evaluating the data types in cereal data frame)

# Fill in the missing cast_count values with 0
movies['cast_count'].fillna(0, inplace = True)
print(cereal['shelf'].unique())

# Using the categorical function from pandas to change the rating data type to categorical with an order of [‘NR’, ‘G’ , ‘PG’, ‘PG-13’, ‘R’]
movies['rating'] = pd.Categorical(movies['rating'], ['NR', 'G','PG','PG-13','R'], ordered= True)

# Using get_dummies() function to create a new binary variable for each categories within our original variable
# Useful when managing nominal variables because it encodes the variables without creating an order among the categories
cereal = pd.get_dummies(data=cereal, columns=['mfr'])