def flights(*tuples):
    result = dict()
    for i in range(0, len(tuples), 2):
        if tuples[i] == "Finish":
            break
        elif tuples[i] not in result.keys():
            result[tuples[i]] = 0
        result[tuples[i]] += tuples[i + 1]

    return result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
