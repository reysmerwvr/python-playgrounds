import sys

if len(sys.argv) >= 2:
    try:
        numberArgument = int(sys.argv[1])
    except ValueError:
        numberArgument = None
        print("Oops!  That was no valid number.  Try again...")
    if numberArgument is not None:
        stringNumber = str(numberArgument)
        stringNumberLength = len(stringNumber)
        # for index in range(stringNumberLength):
        #     print("{:04d}".format(int(stringNumber[stringNumberLength-1-index]) * 10 ** index))
        listOfNumbers = []
        for index in range(stringNumberLength):
            formatWeight = stringNumberLength - index
            firstFormat = "{:<0{f}d}".format(int(stringNumber[index]), f=formatWeight)
            secondFormat = "{:>0{n}d}".format(int(firstFormat), n=stringNumberLength)
            listOfNumbers.append(secondFormat)
        listOfNumbers.reverse()
        for number in listOfNumbers:
            print(number)
else:
    print('Error: Missing arguments')
