def gather_credits(*tupples):
    points = tupples[0]
    if points <= 0:
        return f"Enrollment finished! Maximum credits: {points}.Courses:"
    points_2 = 0
    courses = []
    flag = False

    if len(tupples) == 1:
        return f"You need to enroll in more courses! You have to gather {points} credits more."

    for course, points_c in tupples[1:]:
        if course in courses:
            continue
        points -= points_c
        points_2 += points_c
        courses.append(course)
        if points <= 0:
            flag = True
            break

    if flag:
        return f"Enrollment finished! Maximum credits: {points_2}.\nCourses: {', '.join(x for x in sorted(courses))}"
    else:
        return f"You need to enroll in more courses! You have to gather {points} credits more."


print(gather_credits(80, ("Basics", 27), ))

print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27), ))

print(gather_credits(60, ("Basics", 27), ("Basics", 27), ("Basics", 27), ("Basics", 27), ("Fundamentals", 27),
                     ("Advanced", 30), ("Web", 30)))
