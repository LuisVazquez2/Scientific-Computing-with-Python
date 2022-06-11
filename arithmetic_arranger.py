def get_number_and_operator(line):
    line = line.split()
    n1 = line[0]
    op = line[1]
    n2 = line[2]
    return [n1, op, n2]


def do_operation(list):
    n1 = int(list[0])
    n2 = int(list[2])
    return n1+n2 if list[1] == '+' else n1-n2


def arithmetic_arranger(lista, solve=False):
    ret = ["", "", "", ""]
    flag = False
    if len(lista) > 5:
        return "Error: Too many problems."
    for current in lista:
        if flag:
            ret[0] += "    "
            ret[1] += "    "
            ret[2] += "    "
            ret[3] += "    "
        ans = get_number_and_operator(current)
        n1_l, n2_l = len(ans[0]), len(ans[2])
        if ans[1] != '+' and ans[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if not ans[0].isdigit() or not ans[2].isdigit():
            return "Error: Numbers must only contain digits."
        if n1_l > 4 or n2_l > 4:
            return "Error: Numbers cannot be more than four digits."
        operation = str(do_operation(ans))
        if n1_l > n2_l:
            ret[0] += "  " + ans[0]
            ret[1] += ans[1]+" "*(n1_l - n2_l + 1)+ans[2]
            dashes = n1_l + 2
            ret[2] += '-' * dashes
            ret[3] += " " * (dashes - len(operation)) + operation
        else:
            ret[0] += " "*(n2_l - n1_l + 2)+ans[0]
            ret[1] += ans[1]+" "+ans[2]
            dashes = n2_l + 2
            ret[2] += '-' * dashes
            ret[3] += " "*(dashes - len(operation))+operation
        flag = True

    if solve:
        return f"{ret[0]}\n{ret[1]}\n{ret[2]}\n{ret[3]}"
    else:
        return f"{ret[0]}\n{ret[1]}\n{ret[2]}"
