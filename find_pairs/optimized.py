def find_pairs_optimized(numbers, target):
   seen = set()
   pairs = []
  
   for num in numbers:
       complement = target - num
      
       if(complement in seen):
           pairs.append((complement, num))
      
       seen.add(num)
  
   return pairs


numbers = [1, 2, 3, 4, 5]
target = 6
result = find_pairs_optimized(numbers, target)
print(result)