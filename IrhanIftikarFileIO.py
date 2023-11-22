#Name: Irhan Iftikar
#Date: November 2023
#Description: .csv file-reading program that reads from a database of GCDS students and allows user to make menu choices
#Challenges: Creates graphs from data, deletes records from .csv, updates and changes records to .csv, creates a menu, uses functions, program repeats
#Bugs: No notable bugs found in program
#Sources: Various Internet Syntax Sources (w3schools, Stack Overflow, GeeksForGeeks, etc.)

#Imports modules used in program
import sys
from csv import writer
import matplotlib.pyplot as plt
import pandas as pd    

#Function that outputs the main screen menu options to the user
def main_screen():
        print('''
    GCDS Database File Menu:
    -------------------------------------------------------------
    1 - Add Data Record
    2 - Update/Change Data Record
    3 - Delete Data Record
    4 - Search Data Records by First/Last Name to See Record's Information
    5 - List Data Records by Last Name
    6 - Sort & Graph Data Records by Grade (9-12)
    7 - Sort & Graph Data Records by Gender
    8 - Sort & Graph Data Records by State Location
    9 - Sort & Graph Data Records by 6th Grade Males Living in Greenwich
    10 - Quit''')  

#Function that adds a new data record to .csv file
def add():
    new_entry = []
    first_name, middle_name, last_name, grade, gender, teacher, city, state, zip_code = input("Enter first name, middle, last, grade, gender, teacher, city, \nstate, and zip code (separated by commas, capitalized, no spacing): ").split(",", 9)
    new_entry.extend((first_name, middle_name, last_name, grade, gender, teacher, city, state, zip_code))
    with open("C:\\Users\\iiftikar26\\Desktop\\GCDS Comp Sci\\gcds_data.csv", "a", newline='') as fp:
        writer_object = writer(fp)
        writer_object.writerow(new_entry)
        print("Data record added!")

#Function that takes in the opened .csv file and updates an existing data record to the .csv file
def update(file_in):
    output = False
    df = pd.read_csv(file_in)       #Using Pandas to save the inputted .csv file to a dataframe called df
    user_search = input("Enter the FULL name of the student to update (case sensitive): ")
    index_count = -2
    for line in open("C:\\Users\\iiftikar26\\Desktop\\GCDS Comp Sci\\gcds_data.csv"):
        list_of_words = line.split(",")
        index_count += 1
        if (list_of_words[0] + " " + list_of_words[2]) == user_search:
            output = True
            print("Data record found!")
            first_name, middle_name, last_name, grade, gender, teacher, city, state, zip_code = input("Enter updated first name, middle, last, grade, gender, teacher, city, \nstate, and zip code (separated by commas, capitalized, no spacing): ").split(",", 9)
            #Code below uses Pandas to replace the appropriate index row with the updated information given by the user to the .csv file
            df.loc[index_count] = [first_name, middle_name, last_name, grade, gender, teacher, city, state, zip_code]
            df.to_csv("C:\\Users\\iiftikar26\\Desktop\\GCDS Comp Sci\\gcds_data.csv", index=False)
            print("Data record successfully updated and saved to .csv")
            break
    if output == False:     #If requested data record isn't found
        print("Data record not found.")

#Function that takes in the opened .csv file and deletes an existing data record and saves to the .csv file
def delete(file_in):
    output = False
    df = pd.read_csv(file_in)      #Using Pandas to save the inputted .csv file to a dataframe called df
    user_search = input("Enter the FULL name of the student to delete (case sensitive): ")
    index_count = -2
    for line in open("C:\\Users\\iiftikar26\\Desktop\\GCDS Comp Sci\\gcds_data.csv"):
        list_of_words = line.split(",")
        index_count += 1
        if (list_of_words[0] + " " + list_of_words[2]) == user_search:
            output = True
            #Code below uses Pandas to delete the index row of the record the user wants to delete in the .csv file
            df = df.drop(index_count)
            df.to_csv("C:\\Users\\iiftikar26\\Desktop\\GCDS Comp Sci\\gcds_data.csv", index=False)
            print("Data record successfully deleted and saved to .csv")
            break
    if output == False:
        print("Data record not found.")

#Function that takes in the opened .csv file and searches for a data record by first or last name. Outputs all the information of the record if found.
def search(file_in):
    output = False
    search = input("Enter EITHER the first or last name of the student to find (case sensitive): ")
    for line in file_in:
        list_of_words = line.split(",") 
        if list_of_words[0] == search or list_of_words[2] == search:  
            output = True
            print("Data Record Found! Info: ") 
            for i in range (0,10):
                print(list_of_words[i])
    if output == False:
        print("Data record not found.")

#Function that takes in the opened .csv file and outputs listed data records alphabetically by last name
#Note: Pandas lists last names starting with a lowercase letter such as 'deVeer' or 'van Niekerk' at the end as it sees these as different string types alphabetically 
#Other than the exceptions with the lowercase last names, the function properly prints the last names alphabetically
def list_name(file_in):
    df = pd.read_csv(file_in)
    df = df.sort_values(by=['NameLast', 'NameFirst'], ascending=True)
    print(df)

#Function that takes in opened .csv file and outputs sorted list and graph of proportion of students in grades 9-12
def sort_grade(file_in):
    seniors = 0
    juniors = 0
    sophomores = 0
    freshmen = 0
    for line in file_in:  
        list_of_words = line.split(",") 
        if list_of_words[3] == "12":
            seniors += 1
        elif list_of_words[3] == "11":
            juniors +=1
        elif list_of_words[3] == "10":
            sophomores +=1
        elif list_of_words[3] == "9":
            freshmen +=1
    print("Number of Seniors: ", seniors)
    print("Number of Juniors: ", juniors)
    print("Number of Sophomores: ", sophomores)
    print("Number of Freshmen: ", freshmen)

    #Code below creates a graph using Matplotlib using variables above showing grade distribition
    x_axis = ["Freshman", "Sophomores", "Juniors", "Seniors"]
    y_axis = [freshmen, sophomores, juniors, seniors]
    plt.bar(x_axis, y_axis)
    plt.title('Graphed Data of Grade Proportion in the GCDS High School in 2019')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.show()

#Function that takes in opened .csv file and outputs a sorted list and graph of proportion of students by gender
def sort_gender(file_in):
    boys = 0
    girls = 0
    for line in file_in:   
        list_of_words = line.split(",")
        if list_of_words[4] == "M":
            boys += 1
        elif list_of_words[4] == "F":
            girls +=1
    print("Number of Boys: ", boys)
    print("Number of Girls: ", girls)

    #Code below creates a graph using Matplotlib using variables above showing gender distribition
    x_axis = ["Boys", "Girls"]
    y_axis = [boys, girls]
    plt.bar(x_axis, y_axis)
    plt.title('Graphed Data of Gender Proportion in GCDS in 2019')
    plt.xlabel('Gender')
    plt.ylabel('Number of Students')
    plt.show()

#Function that takes in opened .csv file and outputs a sorted list and graph of proportion of students by state
def sort_state(file_in):
    connecticut = 0
    new_york = 0
    for line in file_in:   
        list_of_words = line.split(",") 
        if list_of_words[8] == "CT":
            connecticut += 1
        elif list_of_words[8] == "NY":
            new_york +=1
    print("Number of Students from Connecticut: ", connecticut)
    print("Number of Students from New York: ", new_york)

    #Code below creates a graph using Matplotlib using variables above showing state distribition
    x_axis = ["Connecticut", "New York"]
    y_axis = [connecticut, new_york]
    plt.bar(x_axis, y_axis)
    plt.title('Graphed Data of State Location Proportion in GCDS in 2019')
    plt.xlabel('State')
    plt.ylabel('Number of Students')
    plt.show()
    
#Function that takes in opened .csv file and outputs a sorted list and graph of proportion of 6th Grade Males in Greenwich
def gradesix_males_greenwich(file_in):
    gradesix_males_greenwich = 0
    gradesix = 0
    for line in file_in:   
        list_of_words = line.split(",")
        if list_of_words[3] == "6":
            gradesix += 1
            if (list_of_words[3] == "6" and list_of_words[4] == "M" and list_of_words[7] == "Greenwich"):
                gradesix_males_greenwich += 1
    print("Number of 6th Grade Males living in Greenwich: ", gradesix_males_greenwich, ", out of : ", gradesix, "total 6th Graders.")
    
    #Code below creates a graph using Matplotlib using variables above showing distribition of sixth grade males in Greenwich to total 6th graders
    x_axis = ["6th Grade Males living in Greenwich", "Total 6th Graders"]
    y_axis = [gradesix_males_greenwich, gradesix]
    plt.bar(x_axis, y_axis)
    plt.title('Graphed Data of Proportion of 6th Grade Males in Greenwich to Total 6th Graders in GCDS in 2019')
    plt.xlabel('Criteria')
    plt.ylabel('Number of Students')
    plt.show()

#Function that terminates the program
def quit():
    sys.exit(0)

#Main function that prompts user for input and executes the other functions
def main():
    file_in = open("C:\\Users\\iiftikar26\\Desktop\\GCDS Comp Sci\\gcds_data.csv")
    choice = input("Select an option from the menu (numbers 1-10): ")
    if choice == "1":
        add()
    elif choice == "2":
        update(file_in)
    elif choice == "3":
        delete(file_in)
    elif choice == "4":
        search(file_in)
    elif choice == "5":
        list_name(file_in)
    elif choice == "6":
        sort_grade(file_in)
    elif choice == "7":
        sort_gender(file_in)
    elif choice == "8":
        sort_state(file_in)
    elif choice == "9":
        gradesix_males_greenwich(file_in)
    elif choice == "10":
        quit()
    else:
        print("Menu choice not valid, try again.")

main_screen()      #Calls main_screen function to print user menu options
while True:         #While loop that repeats program continuously 
    try:
        main()          #Calls main function to execute program
    except IndexError:     
        pass
    except ValueError or FileNotFoundError:
        print("Input or file error occured, please try again.")