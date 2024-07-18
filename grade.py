# passing grade = 75%
# quiz 20%
# termexam 30%
# project 30%
# attendance 10%
# participation 10%

def quiz(raw_score, total_item):
    n = raw_score / total_item
    return 0.10 * n

def exam(raw_score, total_item):
    n = raw_score / total_item
    return 0.30 * n

def proj(raw_score, total_item):
    n = raw_score / total_item
    return 0.30 * n

def att(raw_score, total_item):
    n = raw_score / total_item
    return 0.10 * n

def par(raw_score, total_item):
    n = raw_score / total_item
    return 0.10 * n

finished_quiz = int(input("How many quiz you take: "))
finished_exam = int(input("How many term you take: "))

quiz_scores = []
quiz_totals = []

for i in range(finished_quiz):
    quiz_score = int(input(f"quiz# {i+1} score: "))
    quiz_total = int(input(f"quiz# {i+1} total: "))
    quiz_scores.append(quiz_score)
    quiz_totals.append(quiz_total)

exam_scores = []
exam_totals = []

for i in range(finished_exam):
    exam_score = int(input(f"exam# {i+1} score: "))
    exam_total = int(input(f"exam# {i+1} total: "))
    exam_scores.append(exam_score)
    exam_totals.append(exam_total)

quiz_raw_score = quiz_scores[0] + quiz_scores[1]
quiz_overall = quiz_totals[0] + quiz_totals[1]

q = quiz(quiz_raw_score, quiz_overall)
e = exam(exam_scores[0], exam_totals[0])
p = proj(100, 100)
a = att(100, 100)
pr = par(100, 100)

current_average = (q + e + p + a + pr) * 100
print(current_average)
print("\n\nTo Get 75%")
need_to_pass = 75 - current_average
print(need_to_pass)




