##(2Q)
#Write another Python function to read from a text file,
# The function will take the name of the text file and display the content of the file into the console.

def readtextfile(newfile):
    try:
        with open (newfile,'r') as file:
            storagefile = newfile.read()
            print(f"read textfile:{newfile}")
    except:
        print(f"error:{newfile}")
readtextfile('textfile23-11-22_00-05-53.txt')


#output-> error:textfile23-11-22_00-05-53.txt

