# ? Writing & creating a new file

# with open("MyFile.txt", "w") as ourFile:
#   ourFile.write("Hello, I am a software engineer.\nI am learning python programming")


# ourFile = open("MyFile2.docx", "w")
#   ourFile.write("This is our Document file that can be opened with MS Word.")
# ourFile.close()

#! ---------------------------------------------------------------

# ? Reading form a file

with open("myFile.txt", "r") as ourFile:
    print(ourFile.read(), "File opened successfully")
