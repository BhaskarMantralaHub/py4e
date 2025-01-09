# py4e
Programming for Everybody (Getting Started with Python)


## Invoke Chevron prompt to run python statements

`>>>` Chevron prompt

```python
python3
```

`quit()` or `CTRL + D` to exit 

## Operators

`**` - Power of

## Operator precedence (PEMDAS)

> Left to right
* Parenthesis 
* Exponent / Power (**)
* Multiplication 
* Floating point Division / Multiplication / Modulus - Left to right
* Addition / Subtraction - Left to right

> In Python, the `/` operator always performs floating-point division, even if the result is a whole number

## No floating point data type for Monetary operations

Floating-point numbers are generally not used for monetary calculations because they can introduce rounding errors due to the way they represent numbers internally.

Use decimal instead:

``` python
    from decimal import Decimal

    price = Decimal('19.99')
    tax = Decimal('0.075')
    total = price + price * tax
    print(total)  # Output: 21.48925
```

## Python Ternary Operator

The ternary operator in Python is a one-liner that replaces simple if-else conditions when assigning values.

> Python doesn't support ? : ternary operators just like in Java, Javascript, ..

```
x = 10
result = "Positive" if x > 0 else "Non-positive"
print(result)  # Output: Positive

```

## Exception handling in Python (else block)

```
try:
    with open("data.txt", "r") as file:
        data = file.read()
        # Simulating some data processing
        processed_data = data.upper()  # Example: converting all text to uppercase
except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: There was an issue reading the file.")
else:
    # optional block
    # This block runs only if the try block completes successfully (no exceptions)
    print("File read successfully. Data processed:")
    print(processed_data)
finally:
    print("Program completed.")
```

