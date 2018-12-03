import pandas as pd

# TODO: Set weight1, weight2, and bias
weight1_a = 1.0
weight2_a = 1.0
bias_a = -2.0

weight1_b = 1.0
weight2_b = 1.0
bias_b = -1.0

weight1_c = 0.0
weight2_c = -1.0
bias_c = 0.0

weight1_and = 1.0
weight2_and = 1.0
bias_and = -2.0

def linear_combination(weight1, weight2, bias, test_input):
	linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
	return int(linear_combination >= 0)

# DON'T CHANGE ANYTHING BELOW
# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, True, True, False]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    # linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    # output = int(linear_combination >= 0)
    output_a = linear_combination(weight1_a, weight2_a, bias_a, test_input)
    output_b = linear_combination(weight1_b, weight2_b, bias_b, test_input)
    output_c = linear_combination(weight1_c, weight2_c, bias_c, (0, output_a))
    output_and = linear_combination(weight1_and, weight2_and, bias_and, (output_c, output_b))
    output = output_and
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

# Print output
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))