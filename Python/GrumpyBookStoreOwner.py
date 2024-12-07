
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        # Calculate the base number of satisfied customers
        total_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)

        # Calculate the maximum additional customers that can be satisfied by the technique
        max_additional_satisfied = 0
        additional_satisfied = 0

        # Initial window of size `minutes`
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]

        max_additional_satisfied = additional_satisfied

        # Slide the window over the rest of the customers array
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]

            max_additional_satisfied = max(max_additional_satisfied, additional_satisfied)

        # Total satisfied customers is the sum of initially satisfied and the maximum additional satisfied customers
        return total_satisfied + max_additional_satisfied
