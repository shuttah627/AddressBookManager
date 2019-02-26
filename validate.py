def validateInt(question, test):
    valid = False
    value = ""
    # Let the user try again, until validation passes
    while (valid == False):
        try:
            if (test == None):
                value = int(input(question))
                
            else:
                value = int(test)
            valid = True
            if (valid < 0):
                print("Your response is invalid. Please try again.")
                valid = False
        except:
            print("Your response is invalid. Please try again.")
    return value

def validateText(question, bannedchars, test):
    valid = False
    value = ""
    # Let the user try again, until validation passes
    while (valid == False):
        valid = True
        if (test == None):
            value = input(question)
        else:
            value = str(test)
        # Stop chars that could cause problems (windows filenames for example)
        for i in bannedchars:
            if (i in value):
                print("Sorry, but you cannot use the {0} character for this answer.".format(i))
                valid = False
    return value