class VersionComparison:

    def __init__(self):
        self.isLarger = False
        self.isEqual = False

    def __setEqual(self):
        self.isEqual = True

    def __setLarger(self):
        self.isLarger = True

    def compare(self, v1, v2):
        # split the strings into arrays
        v1_arr = v1.split(".")
        v2_arr = v2.split(".")
        v1_len = len(v1_arr)
        v2_len = len(v2_arr)

        # check whether two inputs are valid
        if self.__isInputValid(v1_arr) is False or self.__isInputValid(v2_arr) is False:
            print("Input not valid")
            return

        if v1 == v2:
            self.__setEqual()
            self.__printResult(v1, v2)
            return

        i = 0
        while i < v1_len and i < v2_len:
            value1 = int(v1_arr[i])
            value2 = int(v2_arr[i])

            if value1 > value2:
                self.__setLarger()
                self.__printResult(v1, v2)
                return
            elif value1 < value2:
                self.__printResult(v1, v2)
                return
            i += 1

        if i < v1_len:
            if self.__checkZeros(v1_arr, i):
                self.__setEqual()
            else:
                self.__setLarger()

        if i < v2_len:
            if self.__checkZeros(v2_arr, i):
                self.__setEqual()
        self.__printResult(v1, v2)


    def __isInputValid(self, arr):
        for s in arr:
            if s.isnumeric() is False:
                return False
        return True

    # check if the rest are all zeros
    def __checkZeros(self, arr, index):
        for i in range(index, len(arr)):
            if arr[i] != "0":
                return False
        return True

    def __printResult(self, v1, v2):
        if self.isEqual:
            print("\"" + v1 + "\"" + " is equal to " + "\"" + v2 + "\"")
        elif self.isLarger:
            print("\"" + v1 + "\"" + " is larger than " + "\"" + v2 + "\"")
        else:
            print("\"" + v1 + "\"" + " is smaller than " + "\"" + v2 + "\"")

if __name__ == "__main__":
    try:
        with open('QuestionB.test', 'r') as file:
            lines = file.readlines()
    except:
        print("File not found")
    else:
        testCounter = 1

        for input in lines:
            try:
                print("test" + str(testCounter) + ": ", end='')
                v1, v2 = input.split()
            except ValueError:
                print("The number of variable is not correct")
            else:
                versionCompare = VersionComparison()
                versionCompare.compare(v1, v2)
                testCounter += 1