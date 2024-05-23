import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

file_name = 'qrlist.txt'

# read text file()
with open(file_name,"r") as f:
    # get lines
    qr_links = f.readlines()
    # create qr-codes
    for i, qr_link in enumerate(qr_links):
        # restrip "\n"
        qr_link = qr_link.rstrip("\n")
        # create qr-code.img    
        img = qrcode.make(qr_link)
        img.save('output/'+str(i + 1) + '.png')