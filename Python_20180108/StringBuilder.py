class StringBuilder:

    def __init__(self):
        pass

    @staticmethod
    def trim() :

        strValue = "     sadsaff asdasdsa adasda    ";
        length = len(strValue)
        startIndex = 0
        endIndex = -1

        while strValue[startIndex] == ' ':
            startIndex = startIndex + 1;
        while strValue[endIndex] == ' ':
            endIndex = endIndex - 1;

        str = strValue[startIndex:length+endIndex+1]
        print(str)
        return str;
