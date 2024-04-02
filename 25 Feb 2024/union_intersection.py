def intersection(a, b):
    a, b = list(set(a)), list(set(b))

    tracker = {}

    for i in range(len(a) if len(a) < len(b) else len(b)):

        tracker[a[i]] = tracker.get(a[i], 0) + 1
        tracker[b[i]] = tracker.get(b[i], 0) - 1

    return [key for key, value in tracker.items() if value == 0]


a = [1, 2, 3, 4, 5]
b = [1, 2, 3]

print(intersection(a, b))