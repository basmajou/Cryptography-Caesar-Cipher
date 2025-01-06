from Logo import logo

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', "Z"]

#MAKE POSITION IN ALPHABET
def refactor_position(position,cipher_type):
  if cipher_type == 'E':
    while position > 25:
        position -= 26
  else:
    while position < 0:
        position += 26
  return position

#ENCODE/DECODE THE MESSAGE
def caesar_chiper(message,shift_num,cipher_type):
  cipher_message = ""
  if cipher_type == 'D':
    shift_num *= -1
  for char in message:
    if char in alphabet:
      position = alphabet.index(char)
      position += shift_num
      position = refactor_position(position,cipher_type)
      cipher_message += alphabet[position]
    else:
      cipher_message += char
  print(f"Here's the {'decode'if cipher_type == 'D' else 'encode'}d result: {cipher_message}")

print(logo)

end_program = False
while not end_program:
  print("\n----\n")
  cipher_type = input("Type 'E' to encrypt, type 'D' to decrypt: ")
  message = input("\nEnter your message:\n").upper()
  shift_number = int(input("\nEnter the shift number: "))
  caesar_chiper(message,shift_number,cipher_type)
  restart = input("\nType 'Y' if you want to go again. Otherwise type 'N': ").upper()
  if restart == "N":
    end_program = True
    print("\nSee you next time!")
