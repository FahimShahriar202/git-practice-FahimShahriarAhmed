from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Fahim Shahriar Ahmed")
print("Today's date:", date.today())

print("Add 10 + 5 =", add(10, 5))
print("Subtract 10 - 5 =", subtract(10, 5))
print("Multiply 10 * 5 =", multiply(10, 5))

try:
    print("Divide 10 / 0 =", divide(10, 0))
except ValueError as error:
    print("Error:", error)