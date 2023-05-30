import streamlit as st

def is_credit_card_valid(number):

    # Remove any non-digit characters

    number = ''.join(filter(str.isdigit, number))

    

    # Reverse the digits

    reversed_digits = number[::-1]

    

    # Double every second digit

    doubled_digits = [int(digit) * 2 if index % 2 == 1 else int(digit) for index, digit in enumerate(reversed_digits)]

    

    # Subtract 9 from any numbers over 9

    subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]

    

    # Calculate the sum of all digits

    total_sum = sum(subtracted_digits)

    

    # Check if the total sum is divisible by 10

    return total_sum % 10 == 0

def main():

    st.title("Credit Card Validator")

    st.write("Enter a credit card number to check its validity.")

    

    credit_card_number = st.text_input("Credit Card Number")

    

    if st.button("Validate"):

        if is_credit_card_valid(credit_card_number):

            st.success("Valid credit card number!")

        else:

            st.error("Invalid credit card number!")

    

if __name__ == "__main__":

    main()

