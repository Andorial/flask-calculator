from flask import Flask, render_template, request
import os

app = Flask(__name__)


def calculate(a: float, b: float, op: str):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    else:
        raise ValueError("Unknown operation")


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    a = request.form.get('a', '')
    b = request.form.get('b', '')
    op = request.form.get('op', '+')

    if request.method == 'POST':
        try:
            a_val = float(a)
            b_val = float(b)
            result = calculate(a_val, b_val, op)
        except ZeroDivisionError as e:
            error = str(e)
        except ValueError:
            error = "Please enter valid numbers"
        except Exception as e:
            error = f"Error: {e}"

    return render_template('index.html', a=a, b=b, op=op, result=result, error=error)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)