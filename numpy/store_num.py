import numpy as np

def find_price(income, number, products):
    # تعداد فروشگاه‌ها و محصولات
    m = len(income)
    n = len(products)

    # بررسی شرط: تعداد محصولات باید برابر تعداد فروشگاه‌ها باشد
    if n != m:
        return "No"

    # تبدیل لیست‌ها به آرایه numpy
    A = np.array(number, dtype=float)
    b = np.array(income, dtype=float)

    try:
        # حل دستگاه معادلات خطی
        prices = np.linalg.solve(A, b)
        return prices
    except np.linalg.LinAlgError:
        # اگر دستگاه معادلات حل‌پذیر نباشد
        return "No"