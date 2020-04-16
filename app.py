import os, serial, cv2

while (1):
    avail_modules = []
    avail_conf = []
    for file in os.listdir("lib"):
        if (file.endswith(".py") & (file != '__init__.py')):
            file = file.replace(".py","")
            avail_modules.append(file)
            exec("import lib."+file)
    for file in os.listdir("conf"):
        if (file.endswith(".conf")):
            avail_conf.append(file)

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
    func_to_call = "lib." + module + ".required_modules()"
    required_modules = eval(func_to_call);
    if (required_modules != 0):
        match=(set(avail_modules) & set(required_modules))
        if match != set(required_modules):
            print("Missing required module for " + module)
        
    func_to_call = "lib." + module + ".required_conf()"
    required_conf = eval(func_to_call);
    if (required_conf != 0):
        match=(set(avail_conf) & set(required_conf))
        if match != set(required_conf):
            print("Missing required config file for " + module)
    
    func_to_call = "lib." + module + "." + module + "()"
    success = eval(func_to_call)
    if success != 0:
        print("Uh Oh - Looks like something went wrong\n")
