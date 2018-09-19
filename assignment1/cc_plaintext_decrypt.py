import base64

base64alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                  'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b',
                  'c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                  'q','r','s','t','u','v','w','x','y','z','0','1','2','3',
                  '4','5','6','7','8','9','+','/']

f = open("assignment-1-a-enc.txt", "r")
f.readline()
encrypted_base64_string = f.read()

for guess_offset in range(1, 64):
    base64_string = ""
    for character in encrypted_base64_string:
        if ((character != '=') and (character != '\n')):
            alphabet_index = base64alphabet.index(character)
            base64_string += base64alphabet[(alphabet_index -
                                             guess_offset) % 64]
        elif (character == '\n'):
            base64_string += '\n'
        else:
            base64_string += '='
    output = base64.b64decode(base64_string)
    print(output)
