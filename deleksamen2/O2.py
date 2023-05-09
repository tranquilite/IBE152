
def question_2(courses: dict) -> tuple:
    students = ()
    for key in courses.keys():
        for student in courses[key]:
            if student[-1] == 'a':
                students = (*students, student)

    return students


if __name__ == '__main__':
    courses = {
        'IBE152': ['Juan', 'Ana', 'Claudia'],
        'IBE500': ['Pedro', 'Linda', 'Maria'],
        'HIST01': ['David', 'Laura']
    }

    print(
        f'>> {question_2(courses)}'
    )
