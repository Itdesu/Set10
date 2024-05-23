import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


with open("qrlist.txt","r") as f:
    qr_links = f.readlines()
    for i, qr_link in enumerate(qr_links):
        qr_link = qr_link.rstrip("\n")
        # print(qr_link)
    
        img = qrcode.make(qr_link)

        img.save('output/'+str(i + 1) + '.png')