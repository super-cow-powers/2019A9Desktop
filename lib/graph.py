"""
Copyright David Miall, 2020
"""

def required_conf(): #Returns a list of the required conf files
    list = ["serial_dev.conf"]
    return list

def required_modules():
    list = ["serialparse"]
    return list


def graph(serial_dev):
    def onClick(event):
        if event.key.isspace():
            if anim.running:
                anim.event_source.stop()
            else:
                anim.event_source.start()
            anim.running ^= True
        
    import lib.serialparse
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import numpy as np
    size = int(input("Points to plot: "))
    print("Start and stop using the space-bar")
    print("The plot must be stopped to save")
    
    packet = lib.serialparse.serialparse_packet(serial_dev)
    packet = lib.serialparse.serialparse_packet(serial_dev)
    vals = [packet.get_value()]
    mType = packet.get_mType()
    if mType == 'v':
        mult = 1
    elif mType == 'mv':
        mult = 0.001
    elif mType == 'a':
         mult = 1
    elif mType == 'ma':
        mult = 0.001
    elif mType == 'ohm':
        mult = 1
    elif mType == 'hz':
        mult = 1
    t = []

    ymx = 20*mult
    ymn = -20*mult
    
    t=0
    fig = plt.figure()
    ax = plt.axes(xlim=(0, size), ylim=(ymn, ymx))
    line, = ax.plot([], [], lw=2)
   
    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        if len(vals) >= size:
            vals.clear()
        packet = lib.serialparse.serialparse_packet(serial_dev)
        vals.append(packet.get_value())
        x = np.linspace(0, len(vals),len(vals))
        y = vals
        line.set_data(x, y)    
        return line,
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=1, interval=1, blit=False)
    anim.running = True
    fig.canvas.mpl_connect('key_press_event', onClick)
    plt.show()
    return 0
