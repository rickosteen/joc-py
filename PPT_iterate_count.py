#PPT - iterate to count items
item_counts = {"apple": 3, "banana": 5, "orange": 2}

for fruit, count in item_counts.items():
    print(f"There are {count} {fruit}s.")
#
scores = {"Alice": 82, "Bob": 91, "Charlie": 87}
highest_score = max(scores, key=scores.get)
print(f"Highest scorer: {highest_score} with a score of {scores[highest_score]}")
