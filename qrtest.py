import qrcode

url = 'https://github.com/Sion99'
img = qrcode.make(url)
img.save('mygithub.png')
