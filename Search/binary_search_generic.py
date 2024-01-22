tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
  'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
   'query': 6},
  'output': 2}]

def evaluateTests(alog, tests):
    for test in tests:
        print(test)
        actual = test['output']
        predicted = alog(**test['input'])
        print(actual == predicted)
        print("actual " , actual)
        print("predicted " , predicted, "\n")

def firstMatch(cards, mid, query):
    if cards[mid] == query:
        if cards[mid] == cards[mid - 1]:
            return "left"
        else:
            return "found"
    elif cards[mid] > query:
        # move right
        return "right"
    else:
        # move left
        return "left"
    

def binary_search(cards, query):
    lo = 0
    hi = len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        condition = firstMatch(cards, mid, query)
        if condition == "found":
            return mid
        elif condition == "left":
            hi = mid - 1
        elif condition == "right":
            lo = mid + 1
    return -1 


evaluateTests(binary_search, tests)