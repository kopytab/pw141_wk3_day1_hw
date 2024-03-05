# # Find Palindrome
# # Given a string of lowercase letters, write a function to see if the word is a palindrome (the same word spelled forward and backwards).		
# # Example Input: 'racecar'
# # Example Output: True

# def pal_test():


def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
print(palindrome("racecap"))