import dropbox
import numpy as np


# Create a dropbox object using an API v2 key
d = dropbox.Dropbox('<ACCESS TOKEN HERE>')


# target location in Dropbox
filename = "Untitled-1.pdf"         # file name
target = "/belgeler/"              # the target folder
targetfile = target + filename   # the target path and file name


# list all files in a specific folder
for entry in d.files_list_folder(target).entries:
    listim = entry.name

    if listim == filename:
        print("File found")
        # note: this simple implementation only works for files in the root of the folder
        res = d.sharing_create_shared_link(targetfile)
        # f.write(res.content)
        print(res.url)
