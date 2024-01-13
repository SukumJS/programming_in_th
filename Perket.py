from itertools import combinations

# Example usage with N different objects
N = int(input())  # Change N to the desired number of objects
sour = []
bitter = []

for i in range(N):
    s, b = [int(x) for x in input().split()]
    sour.append(s)
    bitter.append(b)

# Combine sour and bitter lists into a list of tuples
objects = list(zip(sour, bitter))

pair_summary = []

# Generate combinations of pairs
for i in range(2, N + 1):
    for combo in combinations(objects, i):
        sour_prod = 1
        for s, b in combo:
            sour_prod *= s
        bitter_sum = sum(b for s, b in combo)
        pair_summary.append((sour_prod, bitter_sum))

# Calculate the subtraction for each tuple in pair_summary
subtractions = [sour_prod - bitter_sum for sour_prod,
                bitter_sum in pair_summary]

for i in range(len(subtractions)):
    subtractions[i] = abs(subtractions[i])

# print(min(subtractions))

print(objects)
print(pair_summary)
