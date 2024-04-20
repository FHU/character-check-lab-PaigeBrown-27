#Remove pass and complete the code
def check_character(word, index):
   for i in word:
      character = word[index] 
      if character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
         return "digit"
      elif character == " ":
         return "white space" 
      elif character in ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
         return "letter" 
      else:
         return "unknown"

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))