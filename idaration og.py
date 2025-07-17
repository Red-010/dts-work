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
            "question": "What is the recommended resolution for a 5050?",
            "options": ["A) 720p", "B) 1080p", "C) 1440p", "D) 4k"],
            "answer": "B"
        },
        {
            "question": "What component handles rendering images and video on a computer?",
            "options": ["A) Network Card", "B) GPU (Graphics Processing Unit)", "C) RAM", "D) Motherboard"],
            "answer": "B"
        },
        {
            "question": "How many GB of VRAM does a 5090 have?",
            "options": ["A) 512MB", "B) 32GB", "C) 24GB", "D) 32Gb"], # Typo: "32Gb" instead of "32GB" for consistency
            "answer": "B"
        },
        {
            "question": "What is the MSRP of a Ryzen 5 5600?",
            "options": ["A) $100", "B) $130", "C) $195", "D) $200"],
            "answer": "C"
        },
        {
            "question": "Which of these does not use the SATA interface?",
            "options": ["A) HDD", "B) M.2", "C) SSD"],
            "answer": "B"
        },
        {
            "question": "What is the reason that a computer can't touch tap water?",
            "options": ["A) it does not like water", "B) the water brackets it down", "C) the tap water has electrons shorting it", "D) they can"],
            "answer": "C"
        },
        {
            "question": "Which brand uses TI as a marker for a better card?",
            "options": ["A) nvidia ", "B) intel", "C) amd", "D) ATI"],
            "answer": "A"
        }
    ]

    score = 0