class Solution:
    def dailyTemperatures(self, T):
        hottest_temps = []
        days_till_warm = []
        total_days = len(T)
        for i in range(total_days - 1, -1, -1):
            temp = T[i]
            while hottest_temps:
                day, hot_temp = hottest_temps.pop()
                if hot_temp > temp:
                    hottest_temps.append((day, hot_temp))
                    days_till_warm.insert(0, day - i)
                    break
            if not hottest_temps:
                days_till_warm.insert(0, 0)
            hottest_temps.append((i, temp))
        return days_till_warm