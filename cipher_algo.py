from time import sleep

alphabets = 'abcdefghijklmnopqrstuvwxyz'

def key():
    try:
        with open("key.txt","r") as f:
            return f.readline().lower()
    except FileNotFoundError:
        return "default"
    
def letter_assign(word):
    
    alphabet_dict = {letter: i for i, letter in enumerate(alphabets , start=1)}
    result = [alphabet_dict[letter.lower()] if letter.isalpha() else letter for letter in word]
    
    return result

def number_assign(list):
    alphabet_dict = { i : letter for i , letter in enumerate(alphabets, start=1)}
    result = []
    for i in range(len(list)):
        if type(list[i]) == int:
            result.append(alphabet_dict[list[i]%26 if list[i] % 26 != 0 else 1])
        else:
            result.append(list[i])
    return result
        

def encrypt(text):
    key_list = letter_assign(key())
    text_list = letter_assign(text)
    result = []
    j=0
    for i in range(len(text_list)):
        if type(text_list[i]) == int:
            result.append(key_list[j%len(key_list)] + text_list[i])
            j+= 1
        else:
            result.append(text_list[i])
    
    return "".join(number_assign(result))


def decrypt(text):
    key_list = letter_assign(key())
    text_list = letter_assign(text)
    
    result = []
    j = 0
    for i in range(len(text_list)):
        if type(text_list[i]) == int:
            if text_list[i] < key_list[ j % len(key_list)]:
                result.append(text_list[i] + 26 - key_list[j % len(key_list)])
            else:
                value = text_list[i] - key_list[j % len(key_list)]
                result.append(value if value != 0 else 1 )
            j+=1
        else:
            result.append(text_list[i])
    
    return "".join(number_assign(result))

def main():
    print("\n\t\tTEXTS HERE ARE ENCRYPTED")
    print("\t\t***********************\n\n")
    while True:
        option = input("Options:\n1.Encrypt\n2.Decrypt\n:")
        match option:
            case "1":
                normal_text = input("Type text to encrypt : ")
                
                print(encrypt(normal_text))

            case "2":
                encrypted_text = input("Type the encrypted text to decrypt : ")
                
                print(decrypt(encrypted_text))

            case _:
                print("Invalid Option!")
                continue



if __name__ == "__main__":
    main()