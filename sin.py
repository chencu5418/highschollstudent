def sine():
    import numpy as np
    import math
    x = np.linspace(0, 2*np.pi, 100)
    c = float(input())
    d = float(input())
    A = float(input())
    r = c*x+d
    temp = np.sin(r)
    y1 = A*temp
    y2 = np.sin(x)
    import matplotlib.pyplot as plt
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.xlabel('x of y=Asin(ωx+φ)')
    plt.ylabel('y of y=Asin(ωx+φ)')
    plt.title('y=Asin(ωx+φ)')
    plt.show()
    return 0
def Exp():
    import numpy as np
    import matplotlib.pyplot as plt
    b = int(input("起始点"))
    e = int(input("结束点"))
    x = np.linspace(b, e, 200)
    a = float(input("a"))
    k = float(input("k"))
    n = float(input("n"))
    c = float(input("c"))
    T1 = x+n
    T2 = T1**a
    y1 = k * T2 + c
    y2 = x**a
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y=k(x+n)^a+c')
    plt.show()
    return 0
def indlog():
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    b = int(input("起始点"))
    e = int(input("结束点"))
    x = np.linspace(b, e, 200)
    #k1 = float(input("k of ind"))
    #k2 = float(input("k of log"))
    a = float(input("a"))
    y1 = a**x
    def log_base_a(x, a):
        return np.log(x) / np.log(a)
    # for i in x:
    #    if i == 0:
    #        i = 1
    #    else:
    #        temp = np.array[math.log(i, a)]
    #        y2 = np.array[k2*temp]
    #temp = np.array([])
    #temp = np.log(x, a)
    #y2 = 2*np.log(x, a)
    temp = log_base_a(x, a)
    y2 = temp
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('ind&log')
    plt.show()
    return 0
def xuanzepaixu(list):
    for fill_slot in range(len(list) -1, 0, -1):
        max_index = 0
        for location in range(1 , fill_slot + 1):
            if list [location] > list[max_index]:
                max_index = location
        list [fill_slot],list[max_index] = list[max_index],list[fill_slot]