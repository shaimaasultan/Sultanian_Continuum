import numpy as np

def sultanian_identity_test(n_terms, epsilon):
    """
    Generates a sequence based on a perturbed functional identity.
    We'll use a simplified model of a zeta-related constraint.
    """
    sequence = []
    for n in range(1, n_terms + 1):
        # A mock identity: term must satisfy a transcendental relation 
        # influenced by the 'epsilon' parameter.
        val = np.sin(n * np.pi * epsilon) + np.log1p(n)
        sequence.append(val)
    return np.array(sequence)

# Parameters to compare
epsilon_values = [0.5, 0.5000000001, 0.6]
results = {}

for e in epsilon_values:
    results[e] = sultanian_identity_test(10, e)

for e, seq in results.items():
    print(f"Epsilon {e}: {seq[:3]}...") # Showing first 3 terms