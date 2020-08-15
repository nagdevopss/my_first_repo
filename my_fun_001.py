from sys import argv
def my_first_fun():
    """This is my first python function"""
    print("  ", "Welcome to python programming")
    print("  ", "Python is easy programming Language")
    print("  ", "Python is object oriented programming")

def my_second_fun():
    """This is my second python function"""
    list_01 = ["Nagendra", "Prasad"]
    str_02 = "  "   
    str_03 = str_02.join(list_01)
    str_03 = str_02.join(list_01)
    f_name = "Nagendra"
    l_name = "Prasad"
    full_n = f_name + "  " + " " + l_name
    print("  ", "My Full name is: ", full_n)

my_second_fun()    
