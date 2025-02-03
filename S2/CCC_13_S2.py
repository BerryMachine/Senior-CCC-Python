W = int(input())  
N = int(input())  #

weights = [] 

for i in range(N):
    value = int(input())
    weights.append(value)

current_weight = 0 
queue = []
num_of_carts = 0  

for weight in weights:
    queue.append(weight)
    current_weight += weight 

    if len(queue) > 4:
        current_weight -= queue.pop(0)

    if current_weight > W:  
        break

    num_of_carts += 1 

print(num_of_carts)
