def gather_credits(num, *tupples):
    points = num
    courses = []

    for tuple_1 in tupples:
        course = tuple_1[0]
        course_points = tuple_1[1]

        if course in courses:
            continue

        points -= course_points
        courses.append(course)

        if points <= 0:
            return f"Enrollment finished! Maximum credits: {num - points}.\nCourses: {', '.join(sorted(courses))}"

    return f"You need to enroll in more courses! You have to gather {num - (num - points)} credits more."


# print(gather_credits(80, ("Basics", 27), ))
#
# print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27), ))
#
# print(gather_credits(60, ("Basics", 27), ("Basics", 27), ("Basics", 27), ("Basics", 27), ("Fundamentals", 27),
#                      ("Advanced", 30), ("Web", 30)))

from unittest import TestCase, main


class Test(TestCase):
    def test_students_credits(self):
        result = gather_credits(
            80,
            ("Basics", 27),

        )

        self.assertEqual(
            result.strip(),
            """You need to enroll in more courses! You have to gather 53 credits more.""")


if __name__ == '__main__':
    main()
