"""Greedy algorithm vs Dynamic Programming for food selection"""
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items_dict, budget):
    """Greedy algorithm: maximize calories/cost ratio"""
    sorted_items = sorted(
        items_dict.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    selected = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected, total_cost, total_calories


def dynamic_programming(items_dict, budget):
    """Dynamic programming: optimal solution for maximum calories"""
    item_names = list(items_dict.keys())
    n = len(item_names)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        cost = items_dict[item_name]["cost"]
        calories = items_dict[item_name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = item_names[i - 1]
            selected.append(item_name)
            w -= items_dict[item_name]["cost"]

    return selected, budget - w, dp[n][budget]


if __name__ == "__main__":
    budget = 100

    print("=" * 60)
    print(f"ВИБІР ПРОДУКТІВ НА ВКАЗАНИЙ БЮДЖЕТ - {budget}")
    print("=" * 60)

    greedy_selected, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
    print("\nЖадібний алгоритм:")
    print(f"  Обрані продукти: {', '.join(greedy_selected)}")
    print(f"  Витрати: {greedy_cost}")
    print(f"  Калорії: {greedy_calories}")

    dp_selected, dp_cost, dp_calories = dynamic_programming(items, budget)
    print("\nДинамічне програмування (ДП):")
    print(f"  Обрані продукти: {', '.join(dp_selected)}")
    print(f"  Витрати: {dp_cost}")
    print(f"  Калорії: {dp_calories}")

    print("\nПорівняння:")
    print(f"  Різниця в калоріях: {dp_calories - greedy_calories}")
    print(f"  {'ДП оптимальніший' if dp_calories > greedy_calories else 'Жадібний оптимальніший' if greedy_calories > dp_calories else 'Однаковий результат'}")
