
def fractional_knapsack(a, b, c):

    n = len(a)
    

    items = []
    for i in range(n):
        items.append((b[i], a[i], b[i] / a[i])) 
    

    items.sort(key=lambda x: x[2], reverse=True)
    
    sum = 0.0 
    for value, weight, ratio in items:
        if c == 0:
            break
        if weight <= c:

            sum += value
            c -= weight
        else:

            sum += value * (c / weight)
            c = 0 
    
    return sum


a = [10, 20, 30]  
b = [60, 100, 120] 
c = 50 

max_value = fractional_knapsack(a, b, c)
print(f"Maximum value in Knapsack: {max_value}")
