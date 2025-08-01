def Encryption(message, shift_value):
    encrypted_code = ""
    for i in range(len(message)):
        ascii_char_value = ord(message[i])
        new_character_value = ascii_char_value + shift_value
        new_char = chr(new_character_value)
        encrypted_code += new_char
    return encrypted_code

def Decryption(encrypted_code, shift_value):
    decrypted_code = "" 
    for i in range(len(encrypted_code)):
        ascii_char_value = ord(encrypted_code[i])
        de_new_character_value = ascii_char_value - shift_value
        new_char = chr(de_new_character_value)
        decrypted_code += new_char
    return decrypted_code 
message = "hello world"
shift_value = 2

encrypted_message = Encryption(message, shift_value)
decrypted_message = Decryption(encrypted_message, shift_value)

print("The Encrypted message: " + encrypted_message)
print("The Decrypted message: " + decrypted_message)
