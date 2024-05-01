def knapsack_bb(weights, values, capacity, n):
    """
    Knapsack problem using Branch and Bound technique.
    
    Args:
        weights (list): List of weights of items.
        values (list): List of values of items.
        capacity (int): Maximum capacity of the knapsack.
        n (int): Number of items.
        
    Returns:
        int: Maximum value that can be obtained.
    """
    # Base case
    if n == 0 or capacity == 0:
        return 0
    
    # If weight of the nth item is greater than the capacity, skip it
    if weights[n-1] > capacity:
        return knapsack_bb(weights, values, capacity, n-1)
    
    # Return the maximum of two cases:
    # 1) nth item included
    # 2) nth item excluded
    else:
        return max(values[n-1] + knapsack_bb(weights, values, capacity - weights[n-1], n-1),
                   knapsack_bb(weights, values, capacity, n-1))

def bound(weights, values, capacity, n, current_weight, current_value):
    """
    Compute an upper bound on the maximum value that can be obtained.
    
    Args:
        weights (list): List of weights of items.
        values (list): List of values of items.
        capacity (int): Maximum capacity of the knapsack.
        n (int): Number of items.
        current_weight (int): Weight of the current solution.
        current_value (int): Value of the current solution.
        
    Returns:
        int: Upper bound on the maximum value.
    """
    # Base case
    if n == 0:
        return current_value
    
    # If weight of the nth item is greater than the remaining capacity, skip it
    if weights[n-1] > capacity - current_weight:
        return bound(weights, values, capacity, n-1, current_weight, current_value)
    
    # Return the maximum of two cases:
    # 1) nth item included
    # 2) nth item excluded
    else:
        return max(bound(weights, values, capacity, n-1, current_weight + weights[n-1], current_value + values[n-1]),
                   bound(weights, values, capacity, n-1, current_weight, current_value))

if __name__ == "__main__":
    # Example usage
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    n = len(weights)
    
    print("Recursive solution:", knapsack_bb(weights, values, capacity, n))
    
    # Initialize current weight and value
    current_weight = 0
    current_value = 0
    
    print("Branch and Bound solution:", bound(weights, values, capacity, n, current_weight, current_value))