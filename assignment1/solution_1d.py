import base64
base64alphabet=[ 'A', 'B', 'C', 'D' , 'E', 'F', 'G' , 'H','I','J', 'K' , 'L', 'M' , 'N', 'O' ,'P', 'Q' , 'R','S', 'T', 'U', 'V', 'W' , 'X', 'Y', 'Z',
'a','b','c','d','e','f','g','h','i','j','k','l', 'm' ,'n','o',' p','q','r','s','t','u','v', 'w','x','y','z',
'0','1','2','3','4','5','6','7','8','9','+','/']
#key="2JzvLTdIqRA3nyDg9s0NhxjGf18YQrk/ei6ZM+ObWCKotaclw7FE5BXHV4puUmPS"
key="2JzvLTdIARK3nyDg9s0NhxjGf18YQrk/ei6ZM+ObWCqotaclw7FE5BXHV4puUmPS"
filename="assignment-1-d-enc-clean.txt" 
image=""
with open(filename) as f:
  while True:
    c = f.read(1)
    print('decoding ',c)
    if not c:
      print("End of file")
      break
    if (c != '='):
      print(c,' ',key.index(c))
      image=image+base64alphabet[key.index(c)]
    else: image=image+"=" 

imgdata = base64.b64decode(image)
filename = 'solution_1d.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata)

   








