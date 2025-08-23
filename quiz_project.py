# General Quiz Program

questions = """1. Which organelle produces ATP during respiration?
A. Nucleus
B. Mitochondrion
C. Golgi apparatus
D. Lysosome

2. In DNA, adenine pairs with?
A. Guanine
B. Thymine
C. Cytosine
D. Uracil

3. Light reactions of photosynthesis occur in?
A. Stroma
B. Thylakoid membranes
C. Cytosol
D. Matrix

4. Natural selection means?
A. Individuals change traits by need
B. Best camouflage always survives
C. Heritable traits improving fitness spread
D. Evolution has a goal

5. What carries oxygen in human blood?
A. Platelets
B. Hemoglobin in RBC
C. Plasma proteins
D. WBC

6. Derivative of x^3 is?
A. x^2
B. 3x^2
C. 3x
D. 2x

7. Solve: 2x + 5 = 17
A. 4
B. 5
C. 6
D. 7

8. Area of circle radius 3?
A. 6π
B. 9π
C. 3π
D. 18

9. Probability of 6 on a die?
A. 1/3
B. 1/6
C. 1/5
D. 1/12

10. 2^3 × 2^4 = ?
A. 16
B. 64
C. 128
D. 32

11. Newton’s second law?
A. E=mc^2
B. F=ma
C. p=mv^2
D. V=IR

12. Unit of resistance?
A. Volt
B. Ohm
C. Watt
D. Ampere

13. Speed of light (vacuum)?
A. 3×10^6
B. 3×10^8
C. 3×10^10
D. 3×10^5

14. In an isolated system, mechanical energy?
A. KE always increases
B. PE always decreases
C. Total stays constant
D. Energy is created

15. Work done (F parallel d)?
A. W=F/d
B. W=Fd
C. W=Fd^2
D. W=F/v

16. pH of neutral solution (25°C)?
A. 5
B. 6
C. 7
D. 8

17. Avogadro’s number?
A. 6.022×10^20
B. 6.022×10^23
C. 3×10^8
D. 1.38×10^-23

18. Bond by sharing electrons?
A. Ionic
B. Metallic
C. Covalent
D. Hydrogen

19. Ideal gas law?
A. PV=nRT
B. P=ρgh
C. Q=mcΔT
D. E=hν

20. Oxidation means?
A. Gain e-
B. Loss e-
C. Gain proton
D. Loss

21. What is the capital of France?
A. London
B. Berlin
C. Paris
D. Madrid

22. Who wrote Romeo and Juliet?
A. Charles Dickens
B. William Shakespeare
C. Mark Twain
D. Jane Austen

23. What is the opposite of "hot"?
A. Cold
B. Warm
C. Heat
D. Cool

24. How many days are there in a week?
A. Five
B. Six
C. Seven
D. Eight

25. What is the past tense of "go"?
A. Goed
B. Went
C. Gone
D. Going
"""

answers = {
    1: "B", 2: "B", 3: "B", 4: "C", 5: "B",
    6: "B", 7: "C", 8: "B", 9: "B", 10: "C",
    11: "B", 12: "B", 13: "B", 14: "C", 15: "B",
    16: "C", 17: "B", 18: "C", 19: "A", 20: "B",
    21: "C", 22: "B", 23: "A", 24: "C", 25: "B"
}

print("Welcome to the General Quiz")
name = input("Enter your full name: ")
print(f"\nDear {name}, let's start!\n")
print("Please Read carefullly the following Instruction")
print("Instr.1:Don't forgot to write your full Name")
print("Instr.2:Cheating will nulnify your total result")

question = [question.strip() for question in questions.strip().split("\n\n")]

mark = 0

for item, question in enumerate(question, start=1):
    print(f"Q{item}. {question}")
    
    while True:
        answer = input("Choose the correct answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid choice! Please enter only A, B, C, or D.")

    if answer == answers[item]:
        print(f" Correct! You got 1 points.\n")
        mark += 1
    else:
        print(f"Incorrect. The correct answer was {answers[item]}.\n")

print(f"Quiz Completed!\n{name}, your total score is {mark} / {len(answers)*2}")

if mark >=20:
    print(f"{mark}/25,Excellent")
elif mark >= 15:
       print(f"{mark}/25,V.good")
elif mark >= 10:
       print(f"{mark}/25,Gooood!")
elif mark >= 5:
       print(f"{mark}/25,Satisfactory")
elif mark <= 25:
       print(f"{mark}/25,Failed")

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

    

    
