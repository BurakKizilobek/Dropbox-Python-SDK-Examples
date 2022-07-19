
import dropbox

dbx = dropbox.Dropbox(
    '<ACCESS TOKEN HERE>')
shared_link_metadata = dbx.sharing_create_shared_link_with_settings(
    "/belgeler")

print(shared_link_metadata.url)
