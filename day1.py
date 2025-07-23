# 1st task: List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
nums=[x,y,z]

result = [[i, j, k]
          for i in range(x + 1)
          for j in range(y + 1)
          for k in range(z + 1)
          if i + j + k != n]

print(result)

# 2nd task: Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    
    unique_scores = list(set(arr))          
    unique_scores.sort(reverse=True)        
    
    print(unique_scores[1])                 

