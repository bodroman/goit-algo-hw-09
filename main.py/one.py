import heapq

def find_coins_greedy(amount):
    """
    Ця функція визначає оптимальний спосіб видачі решти за допомогою жадібного алгоритму.

    Параметри:
    amount (int): Сума видачі покупцеві.

    Повертає:
    dict: Словник із кількістю монет кожного номіналу.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    
    return result

def find_min_coins(amount):
    """
    Дана функція визначає мінімальну кількість монет для видачі решти за допомогою динамічного програмування.

    Параметри:
    amount (int): Сума видачі.

    Повертає:
    dict: Словник із кількістю монет кожного номіналу.
    """
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціюємо таблицю для зберігання мінімальної кількості монет для кожної суми
    min_coins = [0] + [float('inf')] * amount
    # Ініціюємо таблицю для відслідковування вибраних монет
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Приклади використання
amount = 113

greedy_result = find_coins_greedy(amount)
print(f"Жадібний алгоритм для {amount}: {greedy_result}")

dp_result = find_min_coins(amount)
print(f"Динамічне програмування для {amount}: {dp_result}")
