
totalCalibration = 0
def main():
    formDigit("calibrations.txt")

def sumCalibrations(x,y):
    global totalCalibration
    totalCalibration += (int(x + y))
    print(totalCalibration)


def formDigit(calibrationFile):
    firstDigit = 0
    lastDigit  = 0
    with open(calibrationFile,"r") as  c:
        for line in c:
            first_DigitFound = False
            for char in line:
                if(char.isdigit()):
                    if (not first_DigitFound):
                        firstDigit = char
                    lastDigit = char
                    first_DigitFound = True
            sumCalibrations(firstDigit, lastDigit)


if __name__ == '__main__':
    main()