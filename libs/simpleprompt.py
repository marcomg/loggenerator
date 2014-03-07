import sys

# Make a boolean question (default answer no)
def boolQuestion(question):
    result = input(question + ' [y/N] ')
    if result in ['y', 'Y', 'yes', 'YES']:
        return True
    else:
        return False

# Make a boolean question (default answer yes)
def boolQuestionY(question):
    result = input(question + ' [Y/n] ')
    if result in ['n', 'N', 'no', 'NO']:
        return False
    else:
        return True

# Make a multi question question (return the number of q.) if possible select 0 to exit
def multiChoose(questions, finalquestion = 'Select an item using a number: '):
    i = -1
    for question in questions:
        i += 1
        print('[' + str(i) + '] ' + question)
    result = input(finalquestion)
    try:
        return int(result)
    except:
        return 0

# Print using colors
def cprint(text, color, bold = 0):
    if color == 'red':
        sColor = '\033[01;31m'
    elif color == 'green':
        sColor = '\033[01;32m'
    else:
        sColor = ''
    print(sColor + text + '\033[0m')