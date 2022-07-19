import dropbox

# Create a dropbox object using an API v2 key
d = dropbox.Dropbox('<ACCESS TOKEN HERE>')


# list all files in main root
#for entry in d.files_list_folder('').entries:
    #print(entry.name)

# list all files in a specific folder
listim = {"listimfirstitemforremove"} # this is a set
for entry in d.files_list_folder('/belgeler').entries:
    listim.add(entry.name) # add the file name to the set

listim.remove("listimfirstitemforremove") # remove the first item from the set
print(listim)
