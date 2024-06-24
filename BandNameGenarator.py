#This program takes the name of city and name of pet to generate the name of your Band 

print("Welcome to band name Generator!!!")

#get name of city from user
name_of_city = input("Enter the name of your city\n")
#get name of user's pet
name_of_pet = input("What is the name of your pet?\n")

#Now combine these two names to form the name of your band
band_name = name_of_city + " " + name_of_pet

print(band_name)