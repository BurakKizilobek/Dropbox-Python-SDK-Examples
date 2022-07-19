import dropbox

# Create a dropbox object using an API v2 key
d = dropbox.Dropbox('<ACCESS TOKEN HERE>')

# list all files in main root
# for entry in d.files_list_folder('').entries:
# print(entry.name)


target = "/belgeler/"              # the target folder


listing = d.files_list_folder('/belgeler')
# todo: add implementation for files_list_folder_continue

for entry in listing.entries:
    if entry.name.endswith(".pdf"):
        with open(entry.name, "wb") as f:
            # note: this simple implementation only works for files in the root of the folder
            res = d.sharing_get_shared_links(
                target + entry.name)
            # f.write(res.content)
            print(res)


# source: https://stackoverflow.com/questions/62395480/download-all-mp4-files-present-in-a-dropbox-folder#62396021
