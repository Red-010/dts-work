def run_quiz():
    questions = [
        {
            "question": "What does AIO stand for?",
            "options": ["A) all I own", "B) all in one", "C) an imbedded option"],
            "answer": "B"
        },
        {
            "question": "What element does a CPU use?",
            "options": ["A) neon", "B) boron", "C) silicon ", "D) carbon"],
            "answer": "C"
        },
        {
            "question": "What does RAM stand for?",
            "options": ["A) Read-Only Memory", "B) Random Access Memory", "C) Run Application Memory", "D) Remote Access Module"],
            "answer": "B"
        },
        {
            "question": "What is the recommended resolution for a RTX 5050?",
            "options": ["A) 16k", "B) 1080p", "C) 1440p", "D) 4k"],
            "answer": "B"
        },
        {
            "question": "What component handles rendering images and video on a computer?",
            "options": ["A) Network Card", "B) Motherboard", "C) RAM", "D) GPU"],
            "answer": "D"
        },
        {
            "question": "How many GB of VRAM does a RTX 5090 have?",
            "options": ["A) 512MB", "B) 32GB", "C) 24GB", "D) 32Gb"],
            "answer": "B"
        },
        {
            "question": "What is the MSRP of a Ryzen 5 5600?",
            "options": ["A) $100", "B) $130", "C) $195", "D) $200"],
            "answer": "C"
        },
        {
            "question": "Which of these does not use the SATA interface?",
            "options": ["A) M.2", "B) HDD", "C) SSD", "D) Floppy disk"],
            "answer": "A"
        },
        {
            "question": "What is the reason that a computer can't touch tap water?",
            "options": ["A) it does not like water", "B) the water breaks it down", "C) the tap water has electrons shorting it", "D) they can"],
            "answer": "C"
        },
        {
            "question": "Which brand uses Ti as a marker for a better card?",
            "options": ["A) nvidia ", "B) intel", "C) amd", "D) ATI"],
            "answer": "A"
        }
    ]

    while True:  # Outer loop for playing again
        score = 0

        for i, q in enumerate(questions, 1):
            print(f"\nQuestion {i}: {q['question']}")
            for option in q['options']:
                print(option)

            while True:
                answer = input("Your answer (A/B/C/D): ").strip().upper()
                if answer in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D.")

            if answer == q['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}.")

        print(f"\nQuiz complete! Your final score: {score}/{len(questions)}")

        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == "no":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    run_quiz()
