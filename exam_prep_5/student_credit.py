def students_credits(*args):
    dilan_dict = dict()
    final_return = []

    for tupple_1 in args:
        tupple_for_touch = tupple_1.split("-")
        course_name = tupple_for_touch[0]
        credits = float(tupple_for_touch[1])
        max_points = float(tupple_for_touch[2])
        dilan_points = float(tupple_for_touch[3])

        dilan_dict[course_name] = credits * (dilan_points / max_points)

    final_score = sum(dilan_dict.values())
    if final_score >= 240:
        final_return.append(f"Diyan gets a diploma with {final_score:.1f} credits.")
    else:
        final_return.append(f"Diyan needs {240 - final_score:.1f} credits more for a diploma.")

    for key, val in sorted(dilan_dict.items(), key=lambda x: -x[1]):
        final_return.append(f"{key} - {val:.1f}")
    return "\n".join(final_return)

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
#
# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
