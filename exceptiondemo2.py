numbers = [1, 2, 3, 0, "hi", 5]

for num in numbers:
    try:
        result = 10 / num
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as e:
        print("Unknown Error:", e)
    finally:
       print("thank you")    


