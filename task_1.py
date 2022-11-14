def is_perfect(n):
    result = []    
    for a in range(1, (int(n/2) + 1)):
        if n % a == 0:
           result.append(a)
    if sum(result) == n:
        return True
    return False     

  


def get_perfect_numbers(n):
    result = []
    i = 0
    while len(result) != n: 
        i = i + 1       
        if is_perfect(i) == True:
                result.append(i)

               
    return result 
