print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> counties = ["Arapahoe", "Denver", "Jefferson"]
#>>> counties
#['Arapahoe', 'Denver', 'Jefferson']
#>>> counties[0]
#'Arapahoe'
#>>> len(counties)
#3
#>>> counties(1:2)
#  File "<stdin>", line 1
#    counties(1:2)
#              ^
#SyntaxError: invalid syntax
#>>> counties[1:2]
#['Denver']
#>>> counties[:2}
#  File "<stdin>", line 1
#   counties[:2}
#               ^
#SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
#>>> counties[:2]
#['Arapahoe', 'Denver']
#>>> counties[1:3]
#['Denver', 'Jefferson']
#>>> counties.append("El Paso")
#>>> counties
#['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
#>>> counties.remove("El Paso")
#>>> coutnies
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'coutnies' is not defined. Did you mean: 'counties'?
#>>> counties
#['Arapahoe', 'Denver', 'Jefferson']
#>>> counties.append("El Paso")
#>>> coutnies
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'coutnies' is not defined. Did you mean: 'counties'?
#>>> counties
#['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
#>> counties(2,"El Paso")
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'list' object is not callable
#>>> counties.instert(2,"El Paso")
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'list' object has no attribute 'instert'. Did you mean: 'insert'?
#>>> counties.instert(2,"El Paso")
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'list' object has no attribute 'instert'. Did you mean: 'insert'?
#>>> counties.insert(2,"El Paso")
#>>> counties
#['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
#>>> counties.remove("El Paso:)
#  File "<stdin>", line 1
#    counties.remove("El Paso:)
#                    ^
#SyntaxError: unterminated string literal (detected at line 1)
#>>> counties.remove("El Paso")
#>>> counties
#['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
#>>> counties.pop("El Paso")
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'str' object cannot be interpreted as an integer
#>>> counties.pop[3]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'builtin_function_or_method' object is not subscriptable
#>>> counties.pop(3)
#'El Paso'
#>>> counties
#['Arapahoe', 'Denver', 'Jefferson']
#>>> counties.pop[0,1,2]="Denver","Jefferson","El Paso"
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'builtin_function_or_method' object does not support item assignment
#>>> counties_dict={"Arapahoe"}
#>>> counties_dict["Arapahoe']=422829
#  File "<stdin>", line 1
#    counties_dict["Arapahoe']=422829
#                  ^
#SyntaxError: unterminated string literal (detected at line 1)
#>>> counties_dict["Arapahoe"]=422829
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'set' object does not support item assignment
#>>> counties_dict["Arapahoe"] = 422829
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'set' object does not support item assignment
#>>> counties_dict={}
#>>> counties_dict["Arapahoe"] = 422829
#>>> counties_dict
#{'Arapahoe': 422829}
#>>> counties_dict["Denver"] = 463353
#>>> counties_dict["Jefferson"] = 432438
#>>> counties_dict
#{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
#>>> len(coutnies_dict)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'coutnies_dict' is not defined. Did you mean: 'counties_dict'?
#>>> len(counties_dict)
#3
#>>> counties_dict.items()
#dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
#>>> counties_dict.keys()
#dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
#>>> counties_dict.values()
#dict_values([422829, 463353, 432438])
#>>> counties_dict.get("Denver")
#463353
#>>> counties_dict['Arapahoe']
#422829
#>>> print(counties_dict['Arapahoe']
#... print(counties_dict.get("Arapahoe"))
#  File "<stdin>", line 1
#    print(counties_dict['Arapahoe']
#          ^^^^^^^^^^^^^^^^^^^^^^^^
#SyntaxError: invalid syntax. Perhaps you forgot a comma?
#>>> print(counties_dict['Arapahoe'])
#422829
#>>> counties_dict["Arapahoe"]
#422829
#>>> voting_data = []
#>>> voting_data.append({"county":"Arapahoe", "regstered_voters": 422829})
#>>>
#>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
#>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#>>> voting_data
#[{'county': 'Arapahoe', 'regstered_voters': 422829}, {'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
#>>> voting_data.remove[0]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'builtin_function_or_method' object is not subscriptable
#>>> voting_data.remove({"county":"Arapahoe", "regstered_voters": 422829})
#>>> voting_data
#[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
#>>> voting_data.append({"county":"El Paso", "registered_voters": 4611149})\
#... voting_data
#  File "<stdin>", line 2
#    voting_data
#    ^^^^^^^^^^^
#SyntaxError: invalid syntax
#>>> voting_data.append({"county":"El Paso", "registered_voters": 4611149})
#>>> voting_data
#[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 4611149}]
#>>> voting_data.remove({"county":"Arapahoe","registered_voters", 422829})
#  File "<stdin>", line 1
#    voting_data.remove({"county":"Arapahoe","registered_voters", 422829})
#                                                              ^
#SyntaxError: ':' expected after dictionary key
#>>> voting_data
#[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 4611149}]
#>>> voting_data.remove({"county":"Arapahoe","registered_voters": 422829})
#>>> voting_data
#[{'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 4611149}]
#>>> voting_data[3] = "Denver"
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IndexError: list assignment index out of range
#>>> voting_data.remove({"county":"Denver","registered_voters": 463353})
#>>> voting_data.append({"county":"Denver","registered_voters": 463353})
#>>> voting_dat
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'voting_dat' is not defined. Did you mean: 'voting_data'?
#>>> voting_data
#[{'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 4611149}, {'county': 'Denver', 'registered_voters': 463353}]
#>>> voting_data.append({"county":"Arapahoe","registered_voters": 422829})
#>>> voting_data
#[{'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 4611149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
#>>> voting_data.insert[0]({"county":"El Paso", "registered_voters", 461149})
#  File "<stdin>", line 1
#    voting_data.insert[0]({"county":"El Paso", "registered_voters", 461149})
#                                                                 ^
#SyntaxError: ':' expected after dictionary key
#>>> voting_data.insert({"county":"El Paso", "registered_voters", 461149})[0]
#  File "<stdin>", line 1
#    voting_data.insert({"county":"El Paso", "registered_voters", 461149})[0]
#                                                              ^
#SyntaxError: ':' expected after dictionary key
#>>> voting_data.insert({"county":"El Paso", "registered_voters", 461149})
#  File "<stdin>", line 1
#    voting_data.insert({"county":"El Paso", "registered_voters", 461149})
#                                                              ^
#SyntaxError: ':' expected after dictionary key
#>>> len("voting_data")
#11
#>>> voting_data
#[{'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 4611149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
#>>> voting_data({"county":"El Paso", "registered_voters": 461149}).insert[0]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'list' object is not callable
#>>> voting_data({"county":["El Paso", "Jefferson", "Denver", "Arapahoe"],"registered_voters":[461149, 432438, 463353, 422829]})
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'list' object is not callable
#>>> voting_data
#[{'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 4611149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
#>>> voting_data.insert(0, ({"county": "El Paso", "registered_voters": 461149})
#...
#... voting_data
#  File "<stdin>", line 1
#    voting_data.insert(0, ({"county": "El Paso", "registered_voters": 461149})
#                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#SyntaxError: invalid syntax. Perhaps you forgot a comma?
#>>> voting_data.insert(0, ({"county": "El Paso", "registered_voters": 461149}))
#>>> voting_data
#[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 4611149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]
#>>> #How many votes did you get?
#>>> my_votes = int(input("How many votes did you get in the election? "))
#How many votes did you get in the election? 200
#>>> #Total votes in election
#>>> total_votes = int(input("What is the total votes in the election? "))
#What is the total votes in the election?
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: invalid literal for int() with base 10: ''
#>>> 500
#500
#>>> 500
#500
#>>> #Calculate the percentage of votes you recieved.
#>>> Percentage_votes = (my_votes/total_votes)*100
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'total_votes' is not defined
#>>> total_votes = 500
#>>> percentage_votes
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'percentage_votes' is not defined
#>>> print("I recieved " + str(percentage_votes)+"% of the total votes.")
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'percentage_votes' is not defined
#>>>


#if "Arapahoe" in counties or "El Paso" in counties:
#   print("Arapahoe or El Paso is in the list on counties")
#else:
#    print("Arapahoe or El Paso is not in the list of counties")

#for county in counties:
#    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict.items():
#    print(county,Value)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county": "Arapahoe", "registered_voters": 422829} ,{"county": "Denver", "registered_voters": 463353},{"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for i in range(len(voting_data)):

      print(voting_data[i]['county'])

print(len(voting_data))

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for county_dict in voting_data:  

     print(county_dict.values())


for county_dict in voting_data:

     print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

#original % of votes
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#formatted % of votes
#my_votes = int(input("How many votes did you get in the election?"))
##total_votes = int(input("What is the total votes in the election?"))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


#Multiple F-String
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)



for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")
    