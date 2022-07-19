import dropbox

ACCESS_TOKEN = "<ACCESS TOKEN HERE>"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

shared_link = "<SHARED LINK HERE>"

metadata, res = dbx.sharing_get_shared_link_file(url=shared_link)

print(metadata.id)
# print(res.text)  # or res.content, or iter_content, or iter_lines, etc. as needed
