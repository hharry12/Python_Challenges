def to_jaden_case(string):

    Pow = 0
    new_string = ""
    for character in string:

        if Pow == 1:
            new_string += character.upper()
            Pow = 0
        elif character == " ":
            Pow = 1
            new_string += character
        else:
            new_string += character

    return new_string

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))