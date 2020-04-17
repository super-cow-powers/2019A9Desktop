#!/usr/bin/env python3
"""
Copyright David Miall, 2020
"""
import os, serial, cv2
import serialsetup

serial_device = serialsetup.return_dev()

while (1):
    avail_modules = []
    avail_conf = []
    global lib
    for file in os.listdir("lib"):
        if (file.endswith(".py") & (file != '__init__.py')):
            file = file.replace(".py","")
            avail_modules.append(file)
            exec("import lib."+file)
    for file in os.listdir("libsupport"):
        if (file.endswith(".py") & (file != '__init__.py')):
            file = file.replace(".py","")
            avail_modules.append(file)
            exec("import lib."+file)
    for file in os.listdir("conf"):
        if (file.endswith(".conf")):
            avail_conf.append(file)

    print("Available Modules:")
    i = 0
    for name in avail_modules:
        print('(' + str(i) + '): ' + name)
        i=i+1
    print("Enter number or 'exit' to quit \n")

    for obj in avail_modules:
        func_to_call = "lib." + obj + ".required_modules()"
        required_modules = eval(func_to_call);
        if (required_modules != 0):
            match=(set(avail_modules) & set(required_modules))
            if match != set(required_modules):
                print("Missing required module for " + obj)
        
        func_to_call = "lib." + obj + ".required_conf()"
        required_conf = eval(func_to_call);
        if (required_conf != 0):
            match=(set(avail_conf) & set(required_conf))
            if match != set(required_conf):
                print("Missing required config file for " + obj)
                
    i = input("Run Module #: ")
    if i == 'exit':
        break
    elif i == 'rescan':
        serial_device = serialsetup.return_dev()
    else:
        i = int(i)
        module = avail_modules[i]
    
        func_to_call = "lib." + module + "." + module + "(serial_device)"
        success = eval(func_to_call)
        if success != 0:
            print("Uh Oh - Looks like something went wrong\n")
