import dropbox

# Create a dropbox object using an API v2 key
d = dropbox.Dropbox('<ACCESS TOKEN HERE>')


# list all files in main root
#for entry in d.files_list_folder('').entries:
    #print(entry.name)

# list all files in a specific folder
listim = [] # this is a set
for entry in d.files_list_folder('/belgeler').entries:
    listim.append(entry.name) # add the file name to the set

# listim.remove("listimfirstitemforremove") # remove the first item from the set
# (len(listim)) # print the length of the list of files
# (listim) # print the list of files
print(listim[0])   # print the 6th file in the list of files. starts from 0
