"""Monte Carlo simulation of two dice rolls"""
import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    """Simulate rolling two dice and calculate sum frequencies"""
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1

    return sums_count


def calculate_probabilities(sums_count, num_rolls):
    """Calculate probability for each sum"""
    probabilities = {}
    for sum_val, count in sums_count.items():
        probabilities[sum_val] = count / num_rolls
    return probabilities


def analytical_probabilities():
    """Analytical probabilities for two dice (from reference table on LMS)"""
    return {
        2: 0.0278,   # 1/36 = 2.78%
        3: 0.0556,   # 2/36 = 5.56%
        4: 0.0833,   # 3/36 = 8.33%
        5: 0.1111,   # 4/36 = 11.11%
        6: 0.1389,   # 5/36 = 13.89%
        7: 0.1667,   # 6/36 = 16.67%
        8: 0.1389,   # 5/36 = 13.89%
        9: 0.1111,   # 4/36 = 11.11%
        10: 0.0833,  # 3/36 = 8.33%
        11: 0.0556,  # 2/36 = 5.56%
        12: 0.0278   # 1/36 = 2.78%
    }


def print_results(probabilities, analytical, num_rolls):
    """Print results in table format"""
    print("=" * 70)
    print(f"РЕЗУЛЬТАТИ СИМУЛЯЦІЇ ({num_rolls:,} кидків)")
    print("=" * 70)
    print(f"{'Сума':<8} {'Монте-Карло':<15} {'Аналітичний':<15} {'Відхилення':<15}")
    print("-" * 70)

    for sum_val in range(2, 13):
        mc_prob = probabilities[sum_val]
        an_prob = analytical[sum_val]
        diff = abs(mc_prob - an_prob)
        print(f"{sum_val:<8} {mc_prob:>14.4%} {an_prob:>14.4%} {diff:>14.4%}")


def plot_results(probabilities, analytical, num_rolls):
    """Create bar chart comparing Monte Carlo and analytical probabilities"""
    sums = list(range(2, 13))
    mc_probs = [probabilities[s] for s in sums]
    an_probs = [analytical[s] for s in sums]

    x = range(len(sums))
    width = 0.45

    _, ax = plt.subplots(figsize=(16, 6))
    bars1 = ax.bar([i - width/2 for i in x], mc_probs, width, label='Монте-Карло', color='blue')
    bars2 = ax.bar([i + width/2 for i in x], an_probs, width, label='Аналітичний розрахунок', color='orange')

    ax.set_xlabel('Сума на кубиках')
    ax.set_ylabel('Ймовірність')
    ax.set_title(f'Порівняння ймовірностей: Монте-Карло vs Аналітичний розрахунок ({num_rolls:,} кидків)')
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Adding values to the columns
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2%}',
                   ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig('dice_probabilities.png', dpi=300, bbox_inches='tight')
    print("\nГрафік збережено: dice_probabilities.png")
    plt.show()


if __name__ == "__main__":
    num_rolls = 100000

    print("Симуляція кидків двох кубиків методом Монте-Карло")
    print(f"Кількість кидків: {num_rolls:,}\n")

    sums_count = simulate_dice_rolls(num_rolls)

    probabilities = calculate_probabilities(sums_count, num_rolls)
    analytical = analytical_probabilities()

    print_results(probabilities, analytical, num_rolls)

    # Plotting the results graph
    plot_results(probabilities, analytical, num_rolls)
