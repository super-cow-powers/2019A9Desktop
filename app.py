import importlib
import os

while (1):
    avail_modules = []
    for file in os.listdir("lib"):
        if (file.endswith(".py") & (file != '__init__.py')):
            file = file.replace(".py","")
            avail_modules.append(file)
            exec("import lib."+file)

    print("Available Modules")
    i = 0
    for name in avail_modules:
        print('(' + str(i) + '): ' + name)
        i=i+1
    print("Or type 'exit' to quit \n")

    i = input("Run Module #: ")
    if i == 'exit':
        break
    i = int(i)
    module = avail_modules[i]
    func_to_call = "lib." + module + "." + module + "()"
    success = eval(func_to_call)
    if success != 0:
        print("Uh Oh - Looks like something went wrong\n")
