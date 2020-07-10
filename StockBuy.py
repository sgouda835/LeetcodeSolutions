def maxProfit(prices):
    # If the stocks can't be bought
    i = 0
    j = 1
    sell = 0
    while j < len(prices) and i < len(prices):
        if prices[i] >= prices[j]:
            i = j
            j = j + 1

        else:
            sell = max(sell, (prices[j] - prices[i]))
            j = j + 1
    return sell


# Driver code
if __name__ == '__main__':
    prices = [1, 5, 2, 3, 7, 6, 4, 5]
    print(maxProfit(prices));