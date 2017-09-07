score = "Score: "
grade = "; Your grade is "
def grades():

    for i in range (0, 10):
        import random
        random_num = random.randint(60, 100)


        if random_num > 89:
            grade_letter = "A"
            print score + str(random_num) + grade + grade_letter

        elif random_num > 79 < 89:
            grade_letter = "B"
            print score + str(random_num) + grade + grade_letter

        elif random_num > 69 < 79:
            grade_letter = "C"
            print score + str(random_num) + grade + grade_letter

        elif random_num > 59 < 69:
            grade_letter = "D"
            print score + str(random_num) + grade + grade_letter


grades()
