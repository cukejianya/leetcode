class Solution:
    def dailyTemperatures(self, T):
        total_days = len(T)
        hottest_days = []
        days_till_warm = [0] * total_days
        for i in range(total_days - 1, -1, -1):
            temp = T[i]
            while hottest_days and T[i] >= T[hottest_days[-1]]:
                hottest_days.pop()
            day_diff = hottest_days[-1] - i if hottest_days else 0
            days_till_warm[i] = day_diff
            hottest_days.append(i)
        return days_till_warm