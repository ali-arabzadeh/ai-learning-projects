def find_determinant(matrix):
    n = len(matrix)

    # حالت پایه: ماتریس 1x1
    if n == 1:
        return matrix[0][0]

    # حالت پایه: ماتریس 2x2
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for col in range(n):
        # ساخت ماتریس کوچک‌تر (minor)
        sub_matrix = []
        for row in range(1, n):
            sub_row = []
            for c in range(n):
                if c != col:
                    sub_row.append(matrix[row][c])
            sub_matrix.append(sub_row)

        # بسط لاپلاس روی سطر اول
        det += ((-1)**col) * matrix[0][col] * find_determinant(sub_matrix)

    return det


if __name__ == "__main__":
    # دریافت ورودی به شکل داده شده
    inp = eval(input().strip())   # مثل [[1,2,3],[4,5,6],[7,8,9]]
    result = find_determinant(inp)

    # گرد کردن به نزدیک‌ترین عدد صحیح
    print(round(result))