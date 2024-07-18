# Test Cases
test_cases = [
    "A 4,A 3,B,A 5,A 8,B",
    "A 4,A 3,B,S,B,A 5,A 8,B",
    "A 4,A 3,B,S,B,A 5,A 8,B,S,B",
    "A 4,A 3,B,S,B,A 5,A 6,B,S,B",
    "S,S,S,B,B,A 6,S,S,S,S,S,S,S,S,B",
    "A 10,A 9,A 8,A 7,B,S,B,A 7,A 1,B,A 50,A 31,S,S,S,S,B",
    "A 5,A 4,B,S,S,A 4,B",
    "A 3,A 4,B,S,S,S,S,S,B"
]

# Process and print results for each test case
for i, test in enumerate(test_cases, start=1):
    inputs = test.split(",")
    results = process_inputs(inputs)
    print(f"Test Case #{i}")
    for result in results:
        print(result)
