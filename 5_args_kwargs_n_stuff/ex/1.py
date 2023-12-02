def numbers(*args):
    positive = sum(x for x in args if x > 0)
    negative = sum(x for x in args if x < 0)

    print(negative)
    print(positive)

    if positive > abs(negative):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


print(numbers(*[int(x) for x in input().split()]))
