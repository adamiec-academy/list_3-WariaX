def fibonacci_sequence(n):
    result = []
    i = 0
    if n == 0:
        return result    
    result.append(0)

    if n == 1:
        return result
    result.append(1)

    if n == 2:
        return result

    while len(result) < n:    
        result.append(result[i]+result[i+1])
        i += 1
    

    return result
