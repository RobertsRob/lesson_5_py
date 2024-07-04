questions = ["Как тебя зовут", "Сколько тебе лет", "Где ты живёшь", "Есть ли у тебя домашнее животное"]
answers = []

print("Вопросы:")
for question in questions:
    print(question+"?")
    answer = input("")
    answers.append(answer)

print("Ответы:")
for i in range(len(questions)):
    print(questions[i]+":", answers[i])