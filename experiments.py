import mlflow

def calculator(a, b, operation=None):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        raise ValueError("Invalid operation specified.")

if __name__ == "__main__":
    a, b, opt = 1084, 3140, "add"
    
    with mlflow.start_run(): # service side
        result = calculator(a, b, opt)

        # Log input parameters and the operation type
        mlflow.log_param("a", a)
        mlflow.log_param("b", b)
        mlflow.log_param("operation", opt)

        # Log the result as a metric (since it's numerical)
        mlflow.log_metric("result", result)

        print(f"My result is {result}")
