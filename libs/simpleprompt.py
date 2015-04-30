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
def multiChoose(questions, finalquestion):
    dim = len(questions)
    for i in range(1, dim):
        print('[' + str(i) + '] ' + questions[i - 1])    
    print('[0] ' + questions[dim - 1])
    result = input(finalquestion)
    try:
        print(result)
        return int(result)
    except:
        return 0

# Print using colors
def cprint(text, color, bold=0):
    if color == 'red':
        sColor = '\033[01;31m'
    elif color == 'green':
        sColor = '\033[01;32m'
    else:
        sColor = ''
    print(sColor + text + '\033[0m')

# Put the text in a corner of #
def cornerText(lines):
    lines = lines.split("\n")
    lengs = []
    for line in lines:
        lengs.append(len(line))
    maxlen = max(lengs)
    text = '##' + '#' * maxlen + '##' + "\n"
    for line in lines:
        tlen = len(line)
        spaces = maxlen - tlen
        text += '# ' + line + ' ' * spaces + ' #' + "\n"
    text += '##' + '#' * maxlen + '##'
    return text
