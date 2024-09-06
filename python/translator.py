import sys
# Letters a-z
BRAILLE_A = "O....."
BRAILLE_B = "O.O..."
BRAILLE_C = "OO...."
BRAILLE_D = "OO.O.."
BRAILLE_E = "O..O.."
BRAILLE_F = "OOO..."
BRAILLE_G = "OOOO.."
BRAILLE_H = "O.OO.."
BRAILLE_I = ".O.O.."
BRAILLE_J = ".OOO.."
BRAILLE_K = "O...O."
BRAILLE_L = "O.O.O."
BRAILLE_M = "OO..O."
BRAILLE_N = "OO.OO."
BRAILLE_O = "O..OO."
BRAILLE_P = "OOO.O."
BRAILLE_Q = "OOOOO."
BRAILLE_R = "O.OOO."
BRAILLE_S = ".OO.O."
BRAILLE_T = ".OOOO."
BRAILLE_U = "O...OO"
BRAILLE_V = "O.O.OO"
BRAILLE_W = ".OOO.O"
BRAILLE_X = "OO..OO"
BRAILLE_Y = "OO.OOO"
BRAILLE_Z = "O..OOO"


# Numbers O-9


BRAILLE_1 = BRAILLE_A
BRAILLE_2 = BRAILLE_B
BRAILLE_3 = BRAILLE_C
BRAILLE_4 = BRAILLE_D
BRAILLE_5 = BRAILLE_E
BRAILLE_6 = BRAILLE_F
BRAILLE_7 = BRAILLE_G
BRAILLE_8 = BRAILLE_H
BRAILLE_9 = BRAILLE_I
BRAILLE_0 = BRAILLE_J


#Special characters
SPACE = "......"
CAPTIAL_FOLLOWS =  ".....O"
NUMBER_FOLLOWS = ".O.OOO"




BRAILLE_TO_ALPHA = {
   BRAILLE_A: 'a',
   BRAILLE_B: 'b',
   BRAILLE_C: 'c',
   BRAILLE_D: 'd',
   BRAILLE_E: 'e',
   BRAILLE_F: 'f',
   BRAILLE_G: 'g',
   BRAILLE_H: 'h',
   BRAILLE_I: 'i',
   BRAILLE_J: 'j',
   BRAILLE_K: 'k',
   BRAILLE_L: 'l',
   BRAILLE_M: 'm',
   BRAILLE_N: 'n',
   BRAILLE_O: 'o',
   BRAILLE_P: 'p',
   BRAILLE_Q: 'q',
   BRAILLE_R: 'r',
   BRAILLE_S: 's',
   BRAILLE_T: 't',
   BRAILLE_U: 'u',
   BRAILLE_V: 'v',
   BRAILLE_W: 'w',
   BRAILLE_X: 'x',
   BRAILLE_Y: 'y',
   BRAILLE_Z: 'z'}
  
BRAILLE_TO_NUM = {
   BRAILLE_1: '1',
   BRAILLE_2: '2',
   BRAILLE_3: '3',
   BRAILLE_4: '4',
   BRAILLE_5: '5',
   BRAILLE_6: '6',
   BRAILLE_7: '7',
   BRAILLE_8: '8',
   BRAILLE_9: '9',
   BRAILLE_0: '0'
}


ALPHA_AND_NUM_TO_BRAILLE = {
   'a': BRAILLE_A,
   'b': BRAILLE_B,
   'c': BRAILLE_C,
   'd': BRAILLE_D,
   'e': BRAILLE_E,
   'f': BRAILLE_F,
   'g': BRAILLE_G,
   'h': BRAILLE_H,
   'i': BRAILLE_I,
   'j': BRAILLE_J,
   'k': BRAILLE_K,
   'l': BRAILLE_L,
   'm': BRAILLE_M,
   'n': BRAILLE_N,
   'o': BRAILLE_O,
   'p': BRAILLE_P,
   'q': BRAILLE_Q,
   'r': BRAILLE_R,
   's': BRAILLE_S,
   't': BRAILLE_T,
   'u': BRAILLE_U,
   'v': BRAILLE_V,
   'w': BRAILLE_W,
   'x': BRAILLE_X,
   'y': BRAILLE_Y,
   'z': BRAILLE_Z,


   '1': BRAILLE_1,
   '2': BRAILLE_2,
   '3': BRAILLE_3,
   '4': BRAILLE_4,
   '5': BRAILLE_5,
   '6': BRAILLE_6,
   '7': BRAILLE_7,
   '8': BRAILLE_8,
   '9': BRAILLE_9,
   '0': BRAILLE_0
}


def translate(input_string):



   if '.' in input_string:
       return braille_to_english(input_string)
  
   return english_to_braille(input_string)


def english_to_braille(input):


   result = ''
   num_sequence__not_started = True


   for c in input:


       if c == " ":


           num_sequence__not_started = True
           result += SPACE


       elif c.isalpha():


           c_in_braille = ALPHA_AND_NUM_TO_BRAILLE[c.lower()]


           if c.isupper():
               result += CAPTIAL_FOLLOWS


          
           result += c_in_braille


       else:
           c_in_braille = ALPHA_AND_NUM_TO_BRAILLE[c]


           if num_sequence__not_started:
               num_sequence__not_started = False
               result += NUMBER_FOLLOWS
          
           result += c_in_braille
  
   return result


def braille_to_english(input):


   result = ''
   cap_next_char = False
   curr_map_to_refer = BRAILLE_TO_ALPHA


   for i in range(0, len(input), 6):


       braille_char = input[i:i+6]


       if braille_char == SPACE:


           curr_map_to_refer = BRAILLE_TO_ALPHA
           result += ' '


       elif braille_char == CAPTIAL_FOLLOWS:
           cap_next_char = True


       elif braille_char == NUMBER_FOLLOWS:
           curr_map_to_refer = BRAILLE_TO_NUM


       else:
           english_char = curr_map_to_refer[braille_char]


           if cap_next_char:


               english_char = english_char.upper()
               cap_next_char = False
          
         


           result += english_char
   return result
          


def main():
    #input_string = ' '.join(sys.argv[1:])
    print(translate("Abc 123 xYz"))

if __name__ == "__main__":
    main()


