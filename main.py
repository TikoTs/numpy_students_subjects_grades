import numpy as np
import random
from data.data_students import georgian_first_names, georgian_last_names
from tabulate import tabulate
from data.data_subjects import subjects

num_students = 100
num_subjects = len(subjects)

grades = np.random.randint(1, 101, size=(num_students, num_subjects))

table = []
for i in range(num_students):
    name = (
        random.choice(georgian_first_names) + " " + random.choice(georgian_last_names)
    )
    table.append([name] + list(grades[i]))

headers = ["სტუდენტი"] + subjects
print(
    tabulate(
        table,
        headers=headers,
        tablefmt="pretty",
        colalign=("center",) * len(headers),
        numalign="center",
    )
)


def student_with_highest_avg_score(grades, table):
    average_scores = np.mean(grades, axis=1)
    highest_average_index = np.argmax(average_scores)
    highest_average_student = table[highest_average_index][0]
    highest_average_score = average_scores[highest_average_index]
    return highest_average_student, highest_average_score


def student_with_extreme_math_scores(grades, table, subjects):
    math_scores = grades[:, subjects.index("მათემატიკა")]
    highest_math_score_index = np.argmax(math_scores)
    lowest_math_score_index = np.argmin(math_scores)
    highest_math_score_student = table[highest_math_score_index][0]
    lowest_math_score_student = table[lowest_math_score_index][0]
    return highest_math_score_student, lowest_math_score_student


def students_above_avg_english_score(grades, table, subjects):
    english_scores = grades[:, subjects.index("ინგლისური")]
    average_english_score = np.mean(english_scores)
    above_avg_english_students = [
        (student[0], score)
        for student, score in zip(table, english_scores)
        if score > average_english_score
    ]
    return above_avg_english_students


def print_results(
    highest_average_student,
    highest_average_score,
    highest_math_score_student,
    lowest_math_score_student,
    students_above_avg_english_score,
    table,
):
    print("\nსტუდენტი ყველაზე მაღალი საშუალო ქულით:")
    print(
        tabulate(
            [[highest_average_student, highest_average_score]],
            headers=["სტუდენტი", "ქულა"],
            tablefmt="pretty",
        )
    )

    print("\nსტუდენტები ყველაზე მაღალი და დაბალი მათემატიკის ქულით:")
    print(
        tabulate(
            [
                ["ყველაზე მაღალი მათემატიკის ქულა", highest_math_score_student],
                ["ყველაზე დაბალი მათემატიკის ქულა", lowest_math_score_student],
            ],
            headers=["კატეგორია", "სტუდენტი"],
            tablefmt="pretty",
        )
    )

    print("\nსტუდენტები, რომელთა ინგლისურის ქულაც მეტია საშუალო ინგლისურის ქულაზე:")
    print(
        tabulate(
            [[name, score] for name, score in students_above_avg_english_score],
            headers=["სტუდენტი", "ქულა"],
            tablefmt="pretty",
        )
    )


highest_average_student, highest_average_score = student_with_highest_avg_score(
    grades, table
)

highest_math_score_student, lowest_math_score_student = (
    student_with_extreme_math_scores(grades, table, subjects)
)
above_avg_english_students = students_above_avg_english_score(grades, table, subjects)

print_results(
    highest_average_student,
    highest_average_score,
    highest_math_score_student,
    lowest_math_score_student,
    above_avg_english_students,
    table,
)
