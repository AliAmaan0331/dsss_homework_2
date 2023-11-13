import random


def GetRandomNumber(min, max):
    """Randomly selects a number between the min and max input."""
    return random.randint(min, max)


def GetRandomOperator():
    """Randomly selects the operator for the math problem."""
    return random.choice(['+', '-', '*'])


def GetSolution(number_a, number_b, operator):
    """Solves a math problem.
    
    Parameters
    ----------
    number_a : int
        First Operand of the math problem.
    number_b : int
        Second Operand of the math problem.
    operator : string
        Operand of the math problem.
    
    Returns
    -------
    problem : string
        The math problem being solved, to display to the user.
    result : int
        Output of the math problem.
    """
    problem = f"{number_a} {operator} {number_b}"
    if operator == '+': result = number_a + number_b
    elif operator == '-': result = number_a - number_b
    else: result = number_a * number_b
    return problem, result

def math_quiz():
    """Presents math problems to user, gets user input and checks if the answer is correct or not.
    Counts the correct answers and outputs the final score."""
    score = 0
    total_questions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    try:
        for question in range(total_questions):
            number_a = GetRandomNumber(1, 10); number_b = GetRandomNumber(1, 5.5); operator = GetRandomOperator()
    
            problem, answer = GetSolution(number_a, number_b, operator)
            print(f"\nQuestion: {problem}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
    
            if useranswer == answer:
                print("Correct! You earned a point.")
                score += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
    except:
        print("Something went wrong, please try again with a suitable answer.")
    else:
        print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
