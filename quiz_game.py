questions = [
    {
        "quiz": "What is capital of France?",
        "options": ["A.France, B.Berlin"],
        "answer": "A"
    },

    {
        "quiz": "What is capital of Germany?",
        "options": ["A.France, B.Berlin"],
        "answer": "B"
    }

]


def play_quiz(quizes):
    score = 0
    for question in quizes:
        print(question["quiz"])
        print(question["options"])
        answer = input("What is the correct answer ?")
        # print(answer.upper())

        if answer.upper() == question["answer"]:
            score += 1
            print("You got it right!")
            print("\n")
        else:
            print("You got it wrong! . Correct answer is " + question["answer"])
            print("\n")

    print("Your score is " + str(score))


play_quiz(questions)
