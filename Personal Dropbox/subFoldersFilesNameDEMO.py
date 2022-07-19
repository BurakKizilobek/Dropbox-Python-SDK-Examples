import dropbox

ACCESS_TOKEN = "<ACCESS TOKEN HERE>"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

mainFolder = '/FB/'

firstFolderName = dbx.files_list_folder(path='/FB')

for a in firstFolderName.entries:
    if isinstance(a, dropbox.files.FolderMetadata):
        secondfolderName = a.name
        resp2 = dbx.files_list_folder(mainFolder + secondfolderName)
        secondRoot = mainFolder + secondfolderName + '/'

        for b in resp2.entries:
            if isinstance(b, dropbox.files.FolderMetadata):
                thirdfolderName = b.name
                resp3 = dbx.files_list_folder(secondRoot + thirdfolderName)
                # print(b.name)
                for c in resp3.entries:
                    # if isinstance(c, dropbox.files.FolderMetadata):
                    print(c.name)
