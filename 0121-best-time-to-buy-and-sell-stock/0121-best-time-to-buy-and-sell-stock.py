class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lg=len(prices)
        smallest=prices[0]
        biggest=prices[lg-1]
        best_profit=0
        list_smallest={smallest:biggest-smallest}
        for i in range(1,lg):
            if prices[i]<smallest:
                list_smallest[smallest]=biggest-smallest
                smallest=prices[i]
                biggest=prices[lg-1]
                list_smallest[smallest]=biggest-smallest
            else:
                if prices[i]>biggest:
                    biggest=prices[i]
        print(list_smallest)
        for smallest in list_smallest:
            print(list_smallest[smallest])
            if biggest-smallest>list_smallest[smallest]:
                profit=biggest-smallest
            else:
                profit=list_smallest[smallest]
            if profit>best_profit:
                best_profit=profit
        return best_profit
                