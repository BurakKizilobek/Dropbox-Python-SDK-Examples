import dropbox

# the source file
filename = "Untitled-1.pdf"         # file name

# target location in Dropbox
target = "/belgeler/"              # the target folder
targetfile = target + filename   # the target path and file name

# Create a dropbox object using an API v2 key
d = dropbox.Dropbox(
    '<ACCESS TOKEN HERE>')


# create a shared link
link = d.sharing_create_shared_link(targetfile)

# url which can be shared
url = link.url

# link which directly downloads by replacing ?dl=0 with ?dl=1
dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
print(dl_url)
