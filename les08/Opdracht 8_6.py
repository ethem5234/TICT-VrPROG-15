invoer= input('voer een string in:')
for letter in invoer:
    code= ord(letter)
    print('{} {}  {:x} {:b}'.format(letter,code,code,code))
