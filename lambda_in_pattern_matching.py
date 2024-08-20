def evaluate_lambda(expression, environment=None):
    if environment is None:
        environment = {}

    match expression:
        case _ if isinstance(expression, type(lambda: None)) and expression(environment):
            return expression(environment)
        case _:
            raise ValueError("Unsupported or unmatched expression type.")

# Example environment
env = {"x": 15, "y": 20, "z": 5}

# 1. Lambda to check if x is greater than 10
lambda_check_x = lambda env: env["x"] > 10
print(evaluate_lambda(lambda_check_x, env))  # Output: True

# 2. Lambda to check if z exists in the environment
lambda_check_z = lambda env: "z" in env
print(evaluate_lambda(lambda_check_z, env))  # Output: True

# 3. Lambda to check if y is even
lambda_check_y_even = lambda env: env["y"] % 2 == 0
print(evaluate_lambda(lambda_check_y_even, env))  # Output: True
