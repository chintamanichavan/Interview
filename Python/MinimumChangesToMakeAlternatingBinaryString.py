def minOperations(s):
    # Count the number of changes needed for two scenarios: starting with '0' and starting with '1'
    changes_start_with_0 = 0
    changes_start_with_1 = 0

    for i in range(len(s)):
        if i % 2 == 0:
            # Even index: should be '0' in one scenario and '1' in another
            if s[i] != '0':
                changes_start_with_0 += 1
            if s[i] != '1':
                changes_start_with_1 += 1
        else:
            # Odd index: should be '1' in one scenario and '0' in another
            if s[i] != '1':
                changes_start_with_0 += 1
            if s[i] != '0':
                changes_start_with_1 += 1

    # Return the minimum of the two scenarios
    return min(changes_start_with_0, changes_start_with_1)

# Test the function with the provided examples
example1_input = "0100"
example1_output = minOperations(example1_input)

example2_input = "10"
example2_output = minOperations(example2_input)

example3_input = "1111"
example3_output = minOperations(example3_input)

example1_output, example2_output, example3_output

