import dropbox

ACCESS_TOKEN = "<ACCESS TOKEN HERE>"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

mainFolder = '/'

resp = dbx.files_list_folder(path='')
for i in resp.entries:
    if isinstance(i, dropbox.files.FolderMetadata):
        foldName = i.name
        for entry in dbx.files_list_folder(mainFolder + foldName).entries:
            print(entry.name)
