#import modules that will be used
import os

#define functions

#check if a string contains a number-period sequence
def check_for_ndot(txt):
    test = False
    for i in range(10):
        sub_string=str(i)+"."
        if sub_string in txt: test = True
    return test

def check_for_nspace(txt):
    test = False
    for i in range(10):
        sub_string=str(i)+" "
        if sub_string in txt: test = True
    return test

def check_for_ndash(txt):
    test = False
    for i in range(10):
        sub_string=str(i)+"-"
        if sub_string in txt: test = True
    return test

def check_for_nbracket(txt):
    test = False
    for i in range(10):
        sub_string=str(i)+")"
        if sub_string in txt: test = True
    return test

def check_valid_musicfile(file_name):
    #check if file_name is a valid file
    valid_file = False
    if ".mp3" in file_name:
        valid_file = True
    elif ".MP3" in file_name:
        valid_file = True
    elif ".m4a" in file_name:
        valid_file = True
    elif ".flac" in file_name:
        valid_file = True
    elif ".wma" in file_name:
        valid_file = True        
    #also check for hidden files in maxOS which start at .    
    if file_name[0] == ".":
        valid_file = False
    return valid_file

def clean_filename(file_name,search_word):
    #this function assumes that search_word is contained in file_name
    #the function will delete the string from [0] to the end of matching search_word
    #warning: no checks will be made based on the above assumptions
    x = len(file_name)
    y = file_name.index(search_word)
    z = y + len(search_word)
    #position z such that the next character will not be a space character
    while file_name[z] == " ":
        z = z + 1
    new_name=file_name[z:x]
    return new_name

#It would be nice to select the directory path using finder-like capability
#This will do for now.
path = input("input file path: ")
os.chdir(path)
print(os.getcwd())
files = os.listdir(os.getcwd())

#first round of test is to check for typical conditions for cleaning
for file_name in files:
    #check if file_name is a valid file
    valid_file = check_valid_musicfile(file_name)
    #first test is for ndot format
    if check_for_ndot(file_name) and valid_file:
        new_name = clean_filename(file_name, ".")
        print(new_name)
        os.renames(file_name, new_name)
    #second test is for nspace format
    elif check_for_nspace(file_name) and valid_file:
        new_name = clean_filename(file_name, " ")
        print(new_name)
        os.renames(file_name, new_name)
    #third test is for ndash format
    elif check_for_ndash(file_name) and valid_file:
        new_name = clean_filename(file_name, "-")
        print(new_name)
        os.renames(file_name, new_name)
    #fourth test is for nbracket format
    elif check_for_nbracket(file_name) and valid_file:
        new_name = clean_filename(file_name, ")")
        print(new_name)
        os.renames(file_name, new_name)

search_word = input("Search character, word or phrase? :")

#second round will look for specific search word
files = os.listdir(os.getcwd())
for file_name in files:
    #check if file_name is a valid file
    valid_file = check_valid_musicfile(file_name)
    if search_word in file_name and valid_file:
        new_name = clean_filename(file_name, search_word)
        print(new_name)
        os.renames(file_name, new_name)