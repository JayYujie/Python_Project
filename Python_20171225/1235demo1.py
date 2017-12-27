def demo(_str):
    length = len(_str)
    preLen = 70-length
    strVal= "{0}{1}".format(' '*preLen , _str)
    print(strVal+" :{0}".format(len(strVal)))
demo("_abcd")

