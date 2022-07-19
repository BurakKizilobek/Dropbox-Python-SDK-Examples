import dropbox

_dropbox_token = "<ACCESS TOKEN HERE>"
admin_email = "<ADMIN EMAIL HERE>"

dbx_team = dropbox.DropboxTeam(_dropbox_token)

_member_id = dbx_team.team_members_get_info([dropbox.team.UserSelectorArg.email(admin_email)])[0].get_member_info().profile.team_member_id

dbx_admin = dbx_team.as_admin(_member_id)

root_namespace_id = dbx_admin.users_get_current_account().root_info.root_namespace_id

dbx_admin_team_root = dbx_admin.with_path_root(dropbox.common.PathRoot.root(root_namespace_id))





# function to get the list of files in a folder
def create_links(foldername, csvfile) :
    filesList = []
    print("creating links for folder " + foldername)
    files = dbx_admin_team_root.files_list_folder('/'+foldername)
    filesList.extend(files.entries)
    print(len(files.entries))
    
    while(files.has_more == True) :
        files = dbx_admin_team_root.files_list_folder_continue(files.cursor)
        filesList.extend(files.entries)
        print(len(files.entries))

    for file in filesList :
        if (isinstance(file, dropbox.files.FileMetadata)) :
            filename = file.name + ',' + file.path_display + ',' + str(file.size) + ','
            link_data = dbx_admin_team_root.sharing_create_shared_link(file.path_lower)
            filename += link_data.url + '\n'
            csvfile.write(filename)
            print(file.name)
        else :
            create_links(foldername+'/'+file.name, csvfile)

# create links for all files in the folder belgeler 
create_links('/Folder A/Folder B/Folder C', open('links.csv', 'w', encoding='utf-8'))
