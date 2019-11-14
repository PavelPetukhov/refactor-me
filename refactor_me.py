#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from operator import itemgetter

Expense = namedtuple('Expense', 'expense_name amount')


def sum_expenses(expenses, min_amount=0):
    aggregated_expenses = defaultdict(int)
    for expense in expenses:
        if expense.amount >= min_amount:
            aggregated_expenses[expense.expense_name] += expense.amount
    return aggregated_expenses


def print_expenses(expenses):
    for expense, amount in sorted(expenses.items(), key=itemgetter(1)):
        print(expense, amount)


if __name__ == '__main__':
    # TODO(dmu) HIGH: Use static fixtures and dynamic fixture framework instead
    test_expenses = (Expense('food', 4), Expense('food', 3), Expense('car', 3), Expense('dog', 1))
    print_expenses(sum_expenses(test_expenses, 2))
