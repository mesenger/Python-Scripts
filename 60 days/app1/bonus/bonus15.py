import json

with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(f'{index + 1}) {alternative}')
    user_choice = int(input('Enter your answer: '))
    question['user_choice'] = user_choice
    if user_choice == question['correct_answer']:
        score = score + 1

for question in data:
    print('-------------------')
    print(question['question_text'])
    
    print(f'Your answer: {question["alternatives"][question["user_choice"] - 1]}')
    print(f'Correct answer: {question["alternatives"][question["correct_answer"] - 1]}')


print(f'Your score is {score}, out of {len(data)}')