# 2019A9Desktop
This is a desktop companion to the University Of York Electronics Second Year Multimeter Project.
It is written in Python, and contains - at the least - a launcer which will allow choosing of modules placed in /lib .
These modules use a standard interface, having at the least a a function returning the required config file/s,
and a function with the same name as the module (which will launch the module).

Config files should be located in /conf, and should be called <name>.conf


Certainly reuqires: pySerial, openCV2, matplotlib, numpy.
May require others, check the scripts.
