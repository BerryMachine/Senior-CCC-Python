while True: 
    radius = int(input())
    if radius == 0: break
    
    x = 0
    y = radius
    
    counter = 0
    
    while True: 
        x += 1
        counter += y*2
        
        while True:
            if (x**2 + y**2) > radius**2: y -= 1
            else: break
    
        if x == radius: break

    print((counter - radius*2)*2 + radius*4 + 1)
