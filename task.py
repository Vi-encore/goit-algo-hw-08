import heapq


def min_cost(cables_lengths):
    if len(cables_lengths) <= 1:
        return 0

    heapq.heapify(cables_lengths)
    total_cost = 0

    while len(cables_lengths) > 1:
        cable_1 = heapq.heappop(cables_lengths)
        cable_2 = heapq.heappop(cables_lengths)

        connection_cost = cable_1 + cable_2
        total_cost += connection_cost

        heapq.heappush(cables_lengths, connection_cost)

    return total_cost


def print_result(cables_lengths):
    print(
        f"Cost of connecting cables: {cables_lengths} is equal to {min_cost(cables_lengths)}"
    )


# Printing results
print_result([1, 2, 3, 4, 5, 6, 7])
print_result([3, 2, 1])
print_result([1, 1])
print_result([0])
print_result([3])
print_result([])
