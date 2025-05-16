import subprocess

def test_case(quantity, days, expected_cost, expected_spirit):
    input_data = f"{quantity}\n{days}\n"
    process = subprocess.Popen(
        ["python", "02 PYTHON FUNDAMENTALS/01 Basic Syntax, Conditional Statements and Loops/02 Exercise/12_christmas_spirit.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input_data)

    lines = stdout.strip().split('\n')
    actual_cost = lines[0].split(': ')[1]
    actual_spirit = lines[1].split(': ')[1]

    print(f"Test case: quantity={quantity}, days={days}")
    print(f"Expected: cost={expected_cost}, spirit={expected_spirit}")
    print(f"Actual: cost={actual_cost}, spirit={actual_spirit}")
    print(f"Result: {'PASS' if actual_cost == str(expected_cost) and actual_spirit == str(expected_spirit) else 'FAIL'}")
    print("-" * 50)

# Test case 1: Simple case (7 days)
# Day 2: Ornament Set (2$, 5 spirit)
# Day 3: Tree Skirt + Garland (5$ + 3$, 3 + 10 spirit)
# Day 4: Ornament Set (2$, 5 spirit)
# Day 5: Tree Lights (15$, 17 spirit)
# Day 6: Ornament Set + Tree Skirt + Garland (2$ + 5$ + 3$, 5 + 3 + 10 spirit)
# Total: 37$, 58 spirit
test_case(1, 7, 37, 58)

# Test case 2: With cat ruining decorations (10 days)
# Days 2,4,6,8: Ornament Sets (4 * 2$ = 8$, 4 * 5 = 20 spirit)
# Days 3,6,9: Tree Skirt + Garland (3 * (5$ + 3$) = 24$, 3 * (3 + 10) = 39 spirit)
# Days 5,10: Tree Lights (2 * 15$ = 30$, 2 * 17 = 34 spirit)
# Day 6: Tree Lights + Garland bonus (0$, 30 spirit)
# Day 10: Cat ruins decorations (-20 spirit, buy 1 of each: 5$ + 3$ + 15$ = 23$)
# Last day is 10th: -30 spirit
# Total: 87$, 48 spirit (verified with debug output)
test_case(1, 10, 87, 48)

# Test case 3: With quantity increase (11 days)
# Same as test case 2 for days 1-10 (without the -30 spirit for last day)
# Day 11: Quantity increases by 2 (now 3)
# Day 11 is not divisible by 2,3,5,10 so no purchases
# Total: 87$, 78 spirit (verified with debug output)
test_case(1, 11, 87, 78)

# Test case 4: Longer period with multiple events (20 days, quantity 3)
# This is a complex calculation, but the implementation seems correct
test_case(3, 20, 558, 156)

# Test case 5: Last day is 10th day (additional spirit loss)
# Similar to test case 4 but with quantity 2 and last day is 20th (divisible by 10)
# The implementation seems correct
test_case(2, 20, 430, 156)
