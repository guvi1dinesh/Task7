#(1Q)
# program using a) function will create a text file with current timestamp,
# b)The file content should have the content of the currenttime stamp


import datetime

def createtextfile_timestamp():
    emptyfile = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    newfile = f"textfile{emptyfile}.txt"
    with open(newfile,'w') as file:
        file.write("create a text file with current timestamp")
    print(f"created textfile:{newfile}")
createtextfile_timestamp()


#OUTPUT-> created textfile:textfile23-11-22_00-05-53.txt




