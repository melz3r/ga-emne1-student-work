def ask_question(question_text):
    answer = input(question_text)
    return answer

def check_answer(answer, correct_answer):
    return answer == correct_answer

def show_feedback(is_correct):
    if is_correct:
        print("Riktig!")
    else:
        print("Feil svar.")

def run_quiz():
    score = 0

    answer = ask_question("Hva er hovedstaden i Brasil? ")
    correct = check_answer(answer, "Brasilia")
    show_feedback(correct)

    if correct:
        score += 1

    answer = ask_question("Hva er myntenheten i Nederland? ")
    correct = check_answer(answer, "Euro")
    show_feedback(correct)

    if correct:
        score += 1

    answer = ask_question("Hvilken programmeringsspråk er dette? ")
    correct = check_answer(answer, "Python")
    show_feedback(correct)

    if correct:
        score += 1

    print(f"Du fikk {score} av 3 poeng.")

run_quiz()
