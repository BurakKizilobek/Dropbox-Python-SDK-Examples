import dropbox

_dropbox_token = "<ACCESS TOKEN HERE>"
admin_email = "<ADMIN EMAIL HERE>"

dbx_team = dropbox.DropboxTeam(_dropbox_token)

_member_id = dbx_team.team_members_get_info([dropbox.team.UserSelectorArg.email(admin_email)])[0].get_member_info().profile.team_member_id

dbx_admin = dbx_team.as_admin(_member_id)

root_namespace_id = dbx_admin.users_get_current_account().root_info.root_namespace_id

dbx_admin_team_root = dbx_admin.with_path_root(dropbox.common.PathRoot.root(root_namespace_id))

listing = dbx_admin_team_root.files_list_folder('/Folder/Subfolder/Subfolder')
for entry in listing.entries:
    print(entry.name)

while listing.has_more:
    listing = dbx_admin_team_root.files_list_folder_continue(listing.cursor)
    for entry in listing.entries:
        print(entry.name)