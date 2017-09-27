
def int2bit(n,num):

    bit_str = []
    for _ in range(n):
        mod = int(num % 2)
        num = int(num / 2)
        bit_str.insert(0,mod)

    return bit_str


def Quiz1Solver(n, arr1, arr2):
    arr1_map = []
    for val in arr1:
        arr1_map.append(int2bit(n, val))

    arr2_map = []
    for val in arr2:
        arr2_map.append(int2bit(n, val))

    final_map = []
    for i in range(n):
        final_row = []
        for j in range(n):
            final_row.append(str(arr1_map[i][j] | arr2_map[i][j]))
        final_map.append("".join(final_row))

    print(final_map)

