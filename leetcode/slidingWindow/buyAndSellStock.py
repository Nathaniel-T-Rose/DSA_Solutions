def maxProfit(self, prices):
        prevMin=float('inf')
        maxProf=0
        for price in prices:
            if price<prevMin:
                prevMin=price

            profit=price-prevMin
            if profit>0 and profit>maxProf:
                maxProf=profit
        return maxProf