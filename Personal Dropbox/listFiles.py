import dropbox

# Create a dropbox object using an API v2 key
d = dropbox.Dropbox('<ACCESS TOKEN HERE>')


# list all files in main root
#for entry in d.files_list_folder('').entries:
#    print(entry.name)

# list all files in a specific folder
for entry in d.files_list_folder('').entries:
    print(entry.name)
