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


    
