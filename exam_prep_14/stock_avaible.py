from collections import deque


def stock_availability(lst, *args):
    lst = deque(lst)
    to_do = args[0]
    if to_do == "delivery":
        for boxes in args[1:]:
            lst.append(boxes)
    elif to_do == "sell":
        if len(args) == 1:
            lst.popleft()
        elif type(args[1]) == int:
            for i in range(int(args[1])):
                lst.popleft()
        elif args[1]:
            lst = list(lst)
            for flavor in args[1:]:
                while flavor in lst:
                    lst.remove(flavor)

    return [x for x in lst]


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
