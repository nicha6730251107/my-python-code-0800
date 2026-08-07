scores = []

for i in range(1, 6):
    score = int(input("Enter score of student " + str(i) + ": "))
    scores.append(score)

print()

for i in range(5):
    score = scores[i]
    if score >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"
    print("Student", str(i + 1) + ":", score, "->", result)