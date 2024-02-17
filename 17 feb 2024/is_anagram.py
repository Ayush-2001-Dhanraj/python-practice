def is_anagram(s, t):
    
    if len(s) != len(t):
            return False

    tracker = {}

    for ss, st in zip(s, t):
        tracker[ss] = tracker.get(ss, 0) + 1
        tracker[st] = tracker.get(st, 0) - 1

    return not any(tracker.values())


print(is_anagram("anagram", "nagaram"))
print(is_anagram("car", "rac"))