def gather_credits(num, *tupples):
    points = num
    if points <= 0:
        return f"Enrollment finished! Maximum credits: {points}.\nCourses: "
    courses = []
    points_done = 0

    for tuple_1 in tupples:
        course = tuple_1[0]
        course_points = tuple_1[1]

        if course in courses:
            continue

        points -= course_points
        points_done += course_points
        courses.append(course)

        if points <= 0:
            return f"Enrollment finished! Maximum credits: {points_done}.\nCourses: {', '.join(sorted(courses))}"

    return f"You need to enroll in more courses! You have to gather {num - points_done} credits more."


print(gather_credits(80, ("Basics", 27), ))

print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27), ))

print(gather_credits(60, ("Basics", 30), ("Basics", 27), ("Basics", 27), ("Basics", 27), ("Fundamentals", 30),
                     ("Advanced", 30), ("Web", 30)))
