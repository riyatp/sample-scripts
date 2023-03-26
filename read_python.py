# open the text file that contains a list of file names
with open('file_list.txt', 'r') as f:
    # read the file names into a list
    file_names = f.read().splitlines()

# loop over the list of file names
for file_name in file_names:
    # open each file and read its contents
    with open(file_name, 'r') as f:
        file_contents = f.read()
        # do something with the file contents
        print(file_contents)
