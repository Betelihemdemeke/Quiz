questions = [
    # English
    {"question": "English: What is the synonym of 'happy'?", "choices": ["Sad", "Angry", "Joyful", "Tired"], "correct_index": 2},
    {"question": "English: What is the past tense of 'eat'?", "choices": ["Eated", "Ate", "Eats", "Eating"], "correct_index": 1},
    {"question": "English: Which word is an adjective?", "choices": ["Run", "Beautiful", "Quickly", "Sing"], "correct_index": 1},
    {"question": "English: What is the antonym of 'big'?", "choices": ["Huge", "Tiny", "Large", "Tall"], "correct_index": 1},
    {"question": "English: Which is a noun?", "choices": ["Jump", "Apple", "Blue", "Fast"], "correct_index": 1},

    # Math
    {"question": "Math: What is 7 + 5?", "choices": ["12", "10", "14", "11"], "correct_index": 0},
    {"question": "Math: What is 9 × 3?", "choices": ["27", "18", "21", "36"], "correct_index": 0},
    {"question": "Math: What is 15 ÷ 3?", "choices": ["5", "6", "4", "3"], "correct_index": 0},
    {"question": "Math: What is 8²?", "choices": ["64", "16", "32", "81"], "correct_index": 0},
    {"question": "Math: What is the square root of 49?", "choices": ["6", "7", "8", "9"], "correct_index": 1},

    # Biology
    {"question": "Biology: What is the basic unit of life?", "choices": ["Cell", "Atom", "Tissue", "Organ"], "correct_index": 0},
    {"question": "Biology: Which gas do plants release during photosynthesis?", "choices": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "correct_index": 1},
    {"question": "Biology: Where does digestion begin?", "choices": ["Stomach", "Mouth", "Small intestine", "Large intestine"], "correct_index": 1},
    {"question": "Biology: Which organ pumps blood in the body?", "choices": ["Lungs", "Heart", "Liver", "Kidney"], "correct_index": 1},
    {"question": "Biology: DNA stands for?", "choices": ["Deoxyribonucleic Acid", "Dynamic Nucleic Acid", "Double Nucleic Atom", "None"], "correct_index": 0},

    # Physics
    {"question": "Physics: What is the SI unit of force?", "choices": ["Joule", "Newton", "Watt", "Pascal"], "correct_index": 1},
    {"question": "Physics: Speed = ?", "choices": ["Distance/Time", "Force × Time", "Work/Energy", "Mass × Acceleration"], "correct_index": 0},
    {"question": "Physics: Which planet has the most gravity?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "correct_index": 2},
    {"question": "Physics: Light travels fastest in?", "choices": ["Water", "Air", "Vacuum", "Glass"], "correct_index": 2},
    {"question": "Physics: Energy can neither be created nor destroyed. This is?", "choices": ["Newton's Law", "Law of Conservation", "Ohm's Law", "Kepler’s Law"], "correct_index": 1},

    # Chemistry
    {"question": "Chemistry: What is H2O?", "choices": ["Hydrogen", "Oxygen", "Water", "Acid"], "correct_index": 2},
    {"question": "Chemistry: Atomic number of Carbon?", "choices": ["12", "6", "14", "8"], "correct_index": 1},
    {"question": "Chemistry: Which element is Na?", "choices": ["Nitrogen", "Sodium", "Nickel", "Neon"], "correct_index": 1},
    {"question": "Chemistry: What is the pH of neutral water?", "choices": ["5", "6", "7", "8"], "correct_index": 2},
    {"question": "Chemistry: Table salt is?", "choices": ["NaCl", "KCl", "CaCO3", "NaOH"], "correct_index": 0}
]

letter_map = ["A", "B", "C", "D"]
score = 0

print(" Multiple Choice Quiz - English, Math, Biology, Physics, Chemistry")
print("------------------------------------------------------------------")

for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['question']}")
    for idx, choice in enumerate(q["choices"]):
        print(f"   {letter_map[idx]}. {choice}")
    
    user_input = input("Your answer (A, B, C, D): ").upper()
    if user_input in letter_map:
        user_index = letter_map.index(user_input)
    if user_index == q["correct_index"]:
        print("Correct!\n")
        score += 1
    else:
            correct_letter = letter_map[q["correct_index"]]
            correct_answer = q["choices"][q["correct_index"]]
            print(f"Wrong! Correct answer is: {correct_letter}. {correct_answer}\n")
else:
    print("Invalid choice. Skipped.\n")

# Final Result
total = len(questions)

print("------------------------------------------------------------------")
print(f"You scored {score} out of {total}.")

if score >= 20:
    print("🌟 Excellent! Great job!")
elif score >= 15:
    print("👍 Good! Keep practicing.")
elif score >=10:
     print("Nice ")
else:
    print("💡 Try again. You’ll improve!")
