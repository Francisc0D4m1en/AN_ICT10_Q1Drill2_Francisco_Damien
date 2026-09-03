from pyscript import document

def compute(event):
    num1 = float(document.querySelector("#num1").value)
    num2 = float(document.querySelector("#num2").value)

    operation = document.querySelector("#operation").value

    # If addition is selected, it adds num1 and num2 together.
    if operation == "+":
        result = num1+num2 

    # If subtraction is selected, it subtracts num2 from num1.
    elif operation == "-":
        result = num1-num2

    # If multiplication is selected, it multiplies num1 and num2 together.
    elif operation == "x":
        result = num1*num2

    # If division is selected, it divides num1 by num2.
    elif operation == "/":

        # This is put in place to prevent the user from dividing by zero, which is impossible.
        if num2 == 0:
            document.querySelector("#result").innerHTML = "why are you trying to divide by ZERO?"
            return
        result = num1/num2

    document.querySelector("#result").innerText = "It's " + str(result)