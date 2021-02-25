# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    correct = [0, 0, 0]
    for i in range(len(answers)):
        answ = answers[i]
        if answ == student1[i%len(student1)]:
            correct[0] += 1
        if answ == student2[i%len(student2)]:
            correct[1] += 1
        if answ == student3[i%len(student3)]:
            correct[2] += 1
    
    max_correct = max(correct)
    for i in range(3):
        if correct[i] == max_correct:
            answer.append(i+1)
            
    return answer
