import random

# ==========================================
# 1. GENERAL KNOWLEDGE QUESTION BANK
# ==========================================
GK_QUESTION_BANK = [
    {
        "question": "What is the capital city of Australia?",
        "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
        "answer": "C",
    },
    {
        "question": "Which planet in our solar system is known as the 'Red Planet'?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": [
            "A. Atlantic Ocean",
            "B. Indian Ocean",
            "C. Arctic Ocean",
            "D. Pacific Ocean",
        ],
        "answer": "D",
    },
    {
        "question": "Who painted the famous masterpiece 'Mona Lisa'?",
        "options": [
            "A. Vincent van Gogh",
            "B. Pablo Picasso",
            "C. Leonardo da Vinci",
            "D. Claude Monet",
        ],
        "answer": "C",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Au", "B. Ag", "C. Fe", "D. Gd"],
        "answer": "A",
    },
    {
        "question": "Which animal is the largest living land mammal?",
        "options": [
            "A. White Rhinoceros",
            "B. African Elephant",
            "C. Hippopotamus",
            "D. Giraffe",
        ],
        "answer": "B",
    },
    {
        "question": "How many players are on the field for one team in a standard soccer (association football) match?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "C",
    },
    {
        "question": "Which country is famously known as the 'Land of the Rising Sun'?",
        "options": ["A. China", "B. Japan", "C. South Korea", "D. Thailand"],
        "answer": "B",
    },
    {
        "question": "What is the hardest naturally occurring substance found on Earth?",
        "options": ["A. Granite", "B. Titanium", "C. Quartz", "D. Diamond"],
        "answer": "D",
    },
    {
        "question": "Which is the smallest country in the world by land area?",
        "options": ["A. Monaco", "B. Vatican City", "C. San Marino", "D. Nauru"],
        "answer": "B",
    },
]

# ==========================================
# 2. HELPER FUNCTIONS
# ==========================================
def get_valid_input(valid_choices=("A", "B", "C", "D")):
    """Continuously prompts the user until a valid letter is provided."""
    while True:
        choice = input("Your answer: ").strip().upper()
        if choice in valid_choices:
            return choice
        print(f"Invalid input. Please choose from: {', '.join(valid_choices)}")


def get_performance_message(score, total):
    """Calculates percentage and provides a targeted result summary."""
    percentage = (score / total) * 100
    if percentage == 100:
        return "Flawless! You're a true trivia master."
    if percentage >= 80:
        return "Excellent job! You have fantastic general knowledge."
    if percentage >= 50:
        return "Good effort! A little more trivia practice and you'll ace it."
    return "Keep learning! Every quiz is a chance to discover new facts."


# ==========================================
# 3. QUIZ EXECUTION ENGINE
# ==========================================
def run_quiz(questions):
    """Handles shuffling, input handling, real-time score tracking, and output."""
    # Shuffling ensures a different question sequence every session
    quiz_items = questions.copy()
    random.shuffle(quiz_items)

    score = 0
    total = len(quiz_items)

    print("=" * 48)
    print("      WELCOME TO THE GENERAL KNOWLEDGE QUIZ     ")
    print("=" * 48)

    for index, item in enumerate(quiz_items, start=1):
        print(f"\nQuestion {index}/{total}")
        print(item["question"])
        for option in item["options"]:
            print(f"  {option}")

        user_answer = get_valid_input()

        if user_answer == item["answer"]:
            score += 1
            print(f"Correct! | Score: {score}/{index}")
        else:
            correct_option = next(
                opt for opt in item["options"] if opt.startswith(item["answer"])
            )
            print(
                f"Incorrect! The correct answer was: {correct_option} | Score: {score}/{index}"
            )

    # Final Summary Screen
    print("\n" + "=" * 48)
    print("                 FINAL RESULTS                  ")
    print("=" * 48)
    print(f"Total Score: {score}/{total} ({(score / total) * 100:.1f}%)")
    print(f"Rating: {get_performance_message(score, total)}")
    print("=" * 48)


# ==========================================
# 4. ENTRY POINT
# ==========================================
if __name__ == "__main__":
    run_quiz(GK_QUESTION_BANK)
