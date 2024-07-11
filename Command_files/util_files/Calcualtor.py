"""Professional Calculator"""
def Calcu():
    try:
        print("Calculator\n")
        while True:
            num=str(input(">"))
            print(eval(num))
    except SyntaxError:
        print("\nERROR : Invalid")
    except NameError:
        print("\nERROR : Invalid")
Calcu()

