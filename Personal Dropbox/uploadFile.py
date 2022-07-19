import dropbox
access_token = '<ACCESS TOKEN HERE>'
file_from = 'C:/Users/brkkz/thumb.png'
file_to = '/ae/thumb.png'


def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)


upload_file(file_from, file_to)
