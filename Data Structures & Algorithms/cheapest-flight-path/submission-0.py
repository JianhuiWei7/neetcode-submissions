class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0
        for _ in range(k+1):
            next_prices = prices.copy()
            for start, end, price in flights:
                if prices[start] == float("inf"):
                    continue
                next_prices[end] = min(
                    price + prices[start],
                    next_prices[end] 
                )
            prices = next_prices.copy()
        return -1 if prices[dst] == float("inf") else prices[dst]