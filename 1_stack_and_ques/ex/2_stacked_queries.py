nss_stack = []

func_map = {
    1: lambda x: nss_stack.append(x[1]),
    2: lambda x: nss_stack.pop() if nss_stack else None,
    3: lambda x: print(max(nss_stack)) if nss_stack else None,
    4: lambda x: print(min(nss_stack)) if nss_stack else None
}

for i in range(int(input())):
    command = [int(x) for x in input().split()]
    func_map[command[0]](command)

nss_stack.reverse()
print(", ".join([str(x) for x in nss_stack]))
