intvar = 1
floatvar = 0.1
boolvar = False
complexvar = 1 + 3j
listvar = ['a', 'b']
tuplevar = (0, 1)
setvar={0,1,2}
dictvar = {'12011905': 'gjx'}
strvar = 'test_str'

def func(intvar,floatvar,boolvar,complexvar,listvar,tuplevar,setvar,dictvar,strvar):
    intvar+=1
    floatvar+=0.1
    boolvar=True
    complexvar += 1j
    listvar.append('c')
    tuplevar = tuplevar.__add__((2, 3))
    setvar.add(3)
    dictvar['12011906'] = 'tyf'
    strvar = 'test_str_2'

if __name__=="__main__":
    print(type(intvar), id(intvar))
    print(type(floatvar), id(floatvar))
    print(type(boolvar), id(boolvar))
    print(type(complexvar), id(complexvar))
    print(type(listvar), id(listvar))
    print(type(tuplevar), id(tuplevar))
    print(type(setvar),id(setvar))
    print(type(dictvar), id(dictvar))
    print(type(strvar), id(strvar))

    print("____________________")

    # intvar += 1
    # floatvar += 1
    # (boolvar) = True
    # complexvar += 1j
    # listvar.append('c')
    # tuplevar=tuplevar.__add__((2,3))
    # setvar.add(3)
    # dictvar['12011906']='tyf'
    # strvar = 'test_str_2'

    func(intvar, floatvar, boolvar, complexvar, listvar, tuplevar, setvar, dictvar, strvar)
    print(type(intvar), id(intvar))
    print(type(floatvar), id(floatvar))
    print(type(boolvar), id(boolvar))
    print(type(complexvar), id(complexvar))
    print(type(listvar), id(listvar))
    print(type(tuplevar), id(tuplevar))
    print(type(setvar),id(setvar))
    print(type(dictvar), id(dictvar))
    print(type(strvar), id(strvar))