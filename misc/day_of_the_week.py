class Solution:
    def dayOfTheWeek(self, day, month, year):
        num_of_years = year - 1969
        years_into_days = num_of_years // 4 + (num_of_years * 365)
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months_into_days = sum(days_in_months[:month-1])
        leap_day = 1 if year % 4 == 0 and month > 2 else 0
        num_of_days = day + years_into_days + months_into_days + leap_day
        day_of_week = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ]
        return day_of_week[(2 + num_of_days) % 7]