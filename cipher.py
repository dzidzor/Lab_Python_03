phrase_to_encode=raw_input("enter a phrase to be coded:")
shift_value=input("enter number of shifts:")
encoded_phrase=''
for c in phrase_to_encode:
    letter=c
    ascii_code=ord(letter)
    encoded_phrase= ascii_code+ shift_value
    letter_res=chr(encoded_phrase)
    
    print letter_res,
