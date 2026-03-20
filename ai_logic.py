# Sample MCQs
MCQS = {
    "Python": [
        {"question": "What is Python?", "options": ["Snake", "Programming Language", "Car", "Game"], "answer": 1},
        {"question": "Which keyword defines a function?", "options": ["func", "def", "function", "lambda"], "answer": 1},
        {"question": "What does len([1,2,3]) return?", "options": ["1", "2", "3", "3"], "answer": 3},
    ],
    "Java": [
        {"question": "Java is ____", "options": ["Python", "Coffee", "Language", "OS"], "answer": 2},
        {"question": "Keyword for inheritance?", "options": ["this", "super", "extends", "implements"], "answer": 2},
        {"question": "Java runs on?", "options": ["JVM", "Python", "Windows only", "Linux only"], "answer": 0},
    ],
    "Aptitude": [
        {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": 1},
        {"question": "5 * 3 = ?", "options": ["8", "15", "10", "20"], "answer": 1},
        {"question": "10 / 2 = ?", "options": ["2", "5", "8", "10"], "answer": 1},
    ]
}

# Evaluate score
def evaluate_answers(skill, answers):
    questions = MCQS.get(skill, [])
    score = 0
    for i, ans in enumerate(answers):
        if i < len(questions) and ans == questions[i]["answer"]:
            score += 1
    return score

# Analyze score
def analyze_score(score):
    if score >= 3:
        return "Expert"
    elif score == 2:
        return "Intermediate"
    else:
        return "Beginner"
