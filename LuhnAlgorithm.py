# to check if the provided card number is valid or not
import string
def verify_card_number(card_number):
    # we have to reverse the card_number
    card_number_reversed = card_number[::-1]
    
    # the card number is now reversed
    number_of_odd_digits = 0
    
    # 2 hops between digits to get the odd digits (digit 1,3,...)
    odd_digits = card_number_reversed[::2]
    
    # the card number is still in string format
    # count your odd digits
    for digits in odd_digits:
        number_of_odd_digits += int(digits)
    number_of_even_digits = 0
    
    # starting from alternative positions, hop two times and count your even digits
    even_digits = card_number_reversed[1::2]
    
    # double to even digits. if theyre greater than 10, add the double digits
    for digits in even_digits:
        number = int(digits)*2
        if number >= 10:
            number = (number // 10) + (number % 10)
        number_of_even_digits += number
    total = number_of_odd_digits + number_of_even_digits
    
    # if the total is a multiple of 10, the card number is valid
    return total%10 == 0

def main():
    card_number = '4111-1111-8243-1141'
    translation = str.maketrans({'-': '', ' ': ''})
    
    # apply this translation on card_number
    translated_card_number = card_number.translate(translation)
    # all non-digits are removed

    # now applying the verification on this translated card number
    if verify_card_number(translated_card_number):
        print('This card number '+ card_number +' is valid')
    else:
        print('this card number '+ card_number +' is invalid')
main()
