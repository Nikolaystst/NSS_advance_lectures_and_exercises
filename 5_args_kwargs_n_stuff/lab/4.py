def rectangle(leng, wid):
    if not isinstance(leng, int) or not isinstance(wid, int):
        return "Enter valid values!"
    result = []

    def area(leng, wid):
        return f"Rectangle area: {leng * wid}"

    def perimeter(leng, wid):
        return f"Rectangle area: {(leng + wid) * 2}"

    result.append(area(leng, wid))
    result.append(perimeter(leng, wid))

    return "\n".join(result)


print(rectangle(2, 10))
print(rectangle('2', 10))
