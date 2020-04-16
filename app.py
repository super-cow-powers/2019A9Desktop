import importlib
import os

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
print("\n")

i = int(input("Run Module #: "))
module = avail_modules[i]
func_to_call = "lib." + module + "." + module + "()"
eval(func_to_call)
