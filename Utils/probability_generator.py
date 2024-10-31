import numpy as np

def generate_probabilities(K):
    # Step 1: Generate K random numbers
    random_numbers = np.random.rand(K)
    
    # Step 2: Normalize the numbers to make their sum equal to 1
    probabilities = random_numbers / np.sum(random_numbers)
    
    return probabilities