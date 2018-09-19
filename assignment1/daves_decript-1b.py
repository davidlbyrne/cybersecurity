import base64
base64alphabet=[ 'A', 'B', 'C', 'D' , 'E', 'F', 'G' , 'H','I','J', 'K' , 'L', 'M' , 'N', 'O' ,'P', 'Q' , 'R','S', 'T', 'U', 'V', 'W' , 'X', 'Y', 'Z',
'a','b','c','d','e','f','g','h','i','j','k','l', 'm' ,'n','o','p','q','r','s','t','u','v', 'w','x','y','z',
'0','1','2','3','4','5','6','7','8','9','+','/']
#key="2JzvLTdIqRA3nyDg9s0NhxjGf18YQrk/ei6ZM+ObWCKotaclw7FE5BXHV4puUmPS"
kay="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
key="*2****M*I*F**X***W***V**bUiYZS5*l*/D8Q**6z**P*RO**Axe***********"
#key="*W****M*S*F**X***2***V**ZUbY/Ii*l**D8Q**6z**P*RO**Axe***********"
# key="*W****M*S*F**X***2*R*V*Z*U*Y/I**l****N*********O****e***********"
#key="*W****M*S*F**X***2*RV**Z*U*Y/I**l****Q*********O****e***********"

filename="assignment-1-b-enc.txt" 
text=""
with open(filename) as f:
  while True:
    c = f.read(1)
    if c == '\n': continue
    print('decoding ',c)
    if not c:
      print("End of file")
      break
    if (c != '='):
      if (key.find(c) > 0) :
        text=text+base64alphabet[key.index(c)]
      else: text=text+c
    else: text=text+"=" 
print(text)
txtdata = base64.b64decode(text)
filename = 'davids_txt.txt'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(txtdata)

   








