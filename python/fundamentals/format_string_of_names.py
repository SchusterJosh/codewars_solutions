# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, which should be
# separated by an ampersand.

def nameList(names):
    # return just the name if it's one
    if len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return f"{names[0]['name']} & {names[1]['name']}"
    else:
        others = ''
        for i in range(0, len(names) - 2):
            others += f"{names[i]['name']}, "
        return f"{others}{names[-2]['name']} & {names[-1]['name']}"


print(nameList([{'name': 'Josh'}, {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
