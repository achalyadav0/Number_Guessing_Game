from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number_to_guess = int(request.form['number_to_guess'])
        guess = int(request.form['guess'])
        attempts = int(request.form['attempts']) + 1

        if guess < number_to_guess:
            message = "Too low! Try again."
        elif guess > number_to_guess:
            message = "Too high! Try again."
        else:
            message = f"Congratulations! You guessed the number in {attempts} attempts."
            return render_template('index.html', message=message, success=True)

        return render_template('index.html', message=message, attempts=attempts, number_to_guess=number_to_guess)

    number_to_guess = random.randint(1, 100)
    return render_template('index.html', attempts=0, number_to_guess=number_to_guess)


if __name__ == '__main__':
    app.run(debug=True)
