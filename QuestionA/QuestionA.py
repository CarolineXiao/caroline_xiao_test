
def checkOverlap(line1, line2):
    # make sure the first number is smaller than the second
    if line1[0] > line1[1]:
        line1 = (line1[1], line1[0])
    if line2[0] > line2[1]:
        line2 = (line2[1], line2[0])

    # check whether overlap
    if line1[0] <= line2[0] and line1[1] >= line2[0]:
        return True
    if line1[0] >= line2[0] and line2[1] >= line1[0]:
        return True
    return False


if __name__ == "__main__":
    try:
        with open('QuestionA.test', 'r') as file:
            lines = file.readlines()
    except:
        print("File not found")
    else:
        testCounter = 1

        for input in lines:
            try:
                print("test" + str(testCounter) + ": ", end='')
                x1, x2, x3, x4 = input.split()
            except ValueError:
                print("The number of variable is not correct")
            else:
                try:
                    line1 = (float(x1), float(x2))
                    line2 = (float(x3), float(x4))
                except:
                    print("Input should be integers")
                else:
                    isOverlap = checkOverlap(line1, line2)

                    print(line1, end='')
                    print(" ", end='')
                    print(line2, end='')
                    print(" - " + str(isOverlap))
            testCounter += 1