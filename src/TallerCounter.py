def solution(array, height):
    return len([person for person in array if person > height])

# Test cases
print(solution([149, 180, 192, 170], 167))  # Output: 3
print(solution([180, 120, 140], 190))        # Output: 0