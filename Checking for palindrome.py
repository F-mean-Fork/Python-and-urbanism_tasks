def is_palindrome(sentence):
    new_list = sentence.lower()
    new_list = "".join(new_list.split())
    reversed_list = new_list[::-1]
    return new_list == reversed_list

print(is_palindrome("радар"))
