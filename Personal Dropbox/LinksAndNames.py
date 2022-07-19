import dropbox

# Create a dropbox object using an API v2 key
d = dropbox.Dropbox('<ACCESS TOKEN HERE>')


target = "/belgeler/"              # the target folder
list_of_urls = []

listing = d.files_list_folder('/belgeler')
# todo: add implementation for files_list_folder_continue

for entry in listing.entries:
    if entry.name.endswith(""):
        # note: this simple implementation only works for files in the root of the folder
        shared_link = d.sharing_get_shared_links(target + entry.name)
        for item in shared_link.links:
            list_of_urls.append(item.url)
            print(entry.name + " " + item.url)

            # source: https://stackoverflow.com/questions/62395480/download-all-mp4-files-present-in-a-dropbox-folder#62396021
