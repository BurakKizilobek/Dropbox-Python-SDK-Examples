import dropbox
# source: https://github.com/nilaykamat/dropbox_sharable_links
# Create a dropbox object using an API v2 key
dbx = dropbox.Dropbox('<ACCESS TOKEN HERE>')


# function to get the list of files in a folder
def create_links(foldername, csvfile) :
    filesList = []
    print("creating links for folder " + foldername)
    files = dbx.files_list_folder('/'+foldername)
    filesList.extend(files.entries)
    print(len(files.entries))
    
    while(files.has_more == True) :
        files = dbx.files_list_folder_continue(files.cursor)
        filesList.extend(files.entries)
        print(len(files.entries))

    for file in filesList :
        if (isinstance(file, dropbox.files.FileMetadata)) :
            filename = file.name + ',' + file.path_display + ',' + str(file.size) + ','
            link_data = dbx.sharing_create_shared_link(file.path_lower)
            filename += link_data.url + '\n'
            csvfile.write(filename)
            print(file.name)
        else :
            create_links(foldername+'/'+file.name, csvfile)

# create links for all files in the folder belgeler 
create_links('Folder/Subfolder', open('links.csv', 'w', encoding='utf-8')) 