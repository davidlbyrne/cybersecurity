filename="bas64_encode7.txt" 
text=""
with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      print("End of file")
      break
    c = f.read(1)
    c = f.read(1)
    fourth = f.read(1)
    text=text+fourth
print(text)
    