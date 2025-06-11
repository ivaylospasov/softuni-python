def process_data():
    """
    Reads input and processes it based on the data type specified on the first line.
    Handles 'int', 'real', and 'string' types.
    """
    try:
        data_type = input()

        if data_type == "int":
            num = int(input())
            result = num * 2
            print(result)
        elif data_type == "real":
            num = float(input())
            result = num * 1.5
            print(f"{result:.2f}")  # Format to two decimal points
        elif data_type == "string":
            text = input()
            result = f"${text}$"
            print(result)
        else:
            print("Invalid data type specified.")
    except ValueError:
        print("Invalid input for the specified data type.")
    except EOFError:
        print("No input provided.")

process_data()