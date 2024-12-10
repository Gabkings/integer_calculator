class BigInt:
    def __init__(self, value="0"):
        if isinstance(value, int):
            value = str(value)
        if not value.isdigit() and not (value.startswith("-") and value[1:].isdigit()):
            raise ValueError("Invalid number")
        self.negative = value.startswith("-")
        self.value = value.lstrip("-")

    def __str__(self):
        return ("-" if self.negative else "") + self.value

    def __add__(self, other):
        if self.negative == other.negative:
            result = self._add(self.value, other.value)
            return BigInt(("-" if self.negative else "") + result)
        else:
            if self._compare(self.value, other.value) >= 0:
                result = self._subtract(self.value, other.value)
                return BigInt(("-" if self.negative else "") + result)
            else:
                result = self._subtract(other.value, self.value)
                return BigInt(("-" if other.negative else "") + result)

    def __sub__(self, other):
        return self + BigInt("-" + str(other))

    def __mul__(self, other):
        sign = "-" if self.negative != other.negative else ""
        result = self._multiply(self.value, other.value)
        return BigInt(sign + result)

    def __truediv__(self, other):
        if other.value == "0":
            raise ZeroDivisionError("Division by zero")
        sign = "-" if self.negative != other.negative else ""
        quotient, _ = self._divide(self.value, other.value)
        return BigInt(sign + quotient)

    def __mod__(self, other):
        if other.value == "0":
            raise ZeroDivisionError("Modulo by zero")
        _, remainder = self._divide(self.value, other.value)
        return BigInt(remainder)

    def __pow__(self, exponent):
        if exponent.negative:
            raise ValueError("Exponentiation with negative exponents not supported")
        result = self._power(self.value, exponent.value)
        return BigInt(result)

    def factorial(self):
        if self.negative:
            raise ValueError("Factorial of negative number is not defined")
        return BigInt(self._factorial(self.value))

    @staticmethod
    def _add(a, b):
        a, b = a.zfill(len(b)), b.zfill(len(a))
        carry, result = 0, []
        for i in range(len(a) - 1, -1, -1):
            summation = int(a[i]) + int(b[i]) + carry
            carry, digit = divmod(summation, 10)
            result.append(str(digit))
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])

    @staticmethod
    def _subtract(a, b):
        a, b = a.zfill(len(b)), b.zfill(len(a))
        borrow, result = 0, []
        for i in range(len(a) - 1, -1, -1):
            diff = int(a[i]) - int(b[i]) - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(diff))
        return "".join(result[::-1]).lstrip("0") or "0"

    @staticmethod
    def _multiply(a, b):
        result = "0"
        for i, digit in enumerate(reversed(b)):
            temp = str(int(a) * int(digit)) + "0" * i
            result = BigInt._add(result, temp)
        return result

    @staticmethod
    def _divide(a, b):
        quotient, remainder = "", "0"
        for digit in a:
            remainder = BigInt._add(BigInt._multiply(remainder, "10"), digit)
            count = 0
            while BigInt._compare(remainder, b) >= 0:
                remainder = BigInt._subtract(remainder, b)
                count += 1
            quotient += str(count)
        return quotient.lstrip("0") or "0", remainder

    @staticmethod
    def _power(base, exponent):
        result = "1"
        for _ in range(int(exponent)):
            result = BigInt._multiply(result, base)
        return result

    @staticmethod
    def _factorial(n):
        result = "1"
        for i in range(2, int(n) + 1):
            result = BigInt._multiply(result, str(i))
        return result

    @staticmethod
    def _compare(a, b):
        a, b = a.lstrip("0"), b.lstrip("0")
        if len(a) != len(b):
            return len(a) - len(b)
        return (a > b) - (a < b)

def repl():
    print("BigInt Calculator REPL (Type 'exit' to quit)")
    print("Supported operations: +, -, *, /, %, ^, ! (factorial)")
    while True:
        try:
            expression = input(">>> ").strip()
            if expression.lower() == "exit":
                break
            if "!" in expression:
                num = BigInt(expression.strip("!"))
                print(num.factorial())
                continue
            for operator in ["+", "-", "*", "/", "%", "^"]:
                if operator in expression:
                    left, right = expression.split(operator)
                    left, right = BigInt(left.strip()), BigInt(right.strip())
                    if operator == "+":
                        print(left + right)
                    elif operator == "-":
                        print(left - right)
                    elif operator == "*":
                        print(left * right)
                    elif operator == "/":
                        print(left / right)
                    elif operator == "%":
                        print(left % right)
                    elif operator == "^":
                        print(left ** right)
                    break
            else:
                print("Invalid expression")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
