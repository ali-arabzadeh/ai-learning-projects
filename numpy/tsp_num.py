import numpy as np

def batched_tsp(dist: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    B, n, _ = dist.shape
    # تعداد زیرمجموعه‌ها: 2^(n-1) چون شهر 0 ثابت است
    Nsub = 1 << (n - 1)

    # DP[b, mask, j] = کمینه هزینه رسیدن به شهر j با بازدید مجموعه mask از {1,...,n-1}
    DP = np.full((B, Nsub, n), np.inf)
    parent = np.full((B, Nsub, n), -1, dtype=int)

    # مقدار اولیه: فقط از شهر 0 به j می‌رویم
    for j in range(1, n):
        mask = 1 << (j - 1)
        DP[:, mask, j] = dist[:, 0, j]
        parent[:, mask, j] = 0

    # پر کردن DP
    for mask in range(Nsub):
        for j in range(1, n):
            if not (mask & (1 << (j - 1))):
                continue
            prev_mask = mask ^ (1 << (j - 1))
            if prev_mask == 0:
                continue
            for k in range(1, n):
                if not (prev_mask & (1 << (k - 1))):
                    continue
                new_cost = DP[:, prev_mask, k] + dist[:, k, j]
                better = new_cost < DP[:, mask, j]
                DP[better, mask, j] = new_cost[better]
                parent[better, mask, j] = k

    # محاسبه‌ی کمینه هزینه‌ی تور کامل
    full_mask = Nsub - 1
    best_costs = np.full(B, np.inf)
    last_city = np.full(B, -1, dtype=int)
    for j in range(1, n):
        cost = DP[:, full_mask, j] + dist[:, j, 0]
        better = cost < best_costs
        best_costs[better] = cost[better]
        last_city[better] = j

    # بازسازی مسیرها
    tours = np.zeros((B, n + 1), dtype=int)
    for b in range(B):
        mask = full_mask
        j = last_city[b]
        path = [0]
        stack = []
        while j != 0:
            stack.append(j)
            pj = parent[b, mask, j]
            mask ^= (1 << (j - 1))
            j = pj
        path.extend(reversed(stack))
        path.append(0)
        tours[b, :] = path

    return best_costs.tolist(), tours.tolist()
