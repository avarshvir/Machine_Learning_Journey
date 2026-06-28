import numpy as np

input_data = [2,5,7];
weights = [0.5, 0.25, 0.75];
bias = 1;

def neuron_output(input_data, weights, bias):
    # Convert input_data and weights to numpy arrays
    input_array = np.array(input_data)
    weights_array = np.array(weights)
    
    # Calculate the weighted sum of inputs
    weighted_sum = np.dot(input_array, weights_array) + bias
    
    # Apply the activation function (e.g., ReLU)
    output = max(0, weighted_sum)  # ReLU activation
    
    return output

# Example usage
output = neuron_output(input_data, weights, bias)
print(output)