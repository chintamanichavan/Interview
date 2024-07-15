class Solution:
    def totalMoney(self, n: int) -> int:
        # Initialize total money and the money to put in the bank on the current day
        total_money = 0
        current_money = 1
        week_day = 1  # Starting on Monday

        for day in range(1, n + 1):
            total_money += current_money

            # If it's Sunday, reset the week day and increase the money for next Monday
            if week_day == 7:
                week_day = 0
                current_money = current_money - 6  # Reset to the amount of the last Monday
            current_money += 1
            week_day += 1

        return total_money
