"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""
from typing import List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change_arr = [amount + 1] * (amount + 1)
        change_arr[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    change_arr[i] = min(change_arr[i], change_arr[i - coin] + 1)
        if change_arr[amount] == amount + 1:
            return -1
        return change_arr[amount]


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or len(coins) == 0:
            return 0
        q = deque([[0, 0]])
        max_level = (amount // min(coins)) + 1
        seen = {0}
        nxt_lvl = 0
        while q and nxt_lvl < max_level:
            sub_amount, nxt_lvl = q.popleft()
            nxt_lvl += 1
            for coin in coins:
                new_amount = sub_amount + coin
                if new_amount not in seen:
                    seen.add(new_amount)
                    q.append([new_amount, nxt_lvl])
                if new_amount == amount:
                    return nxt_lvl
        return -1



def test_case_4():
    coins = [186, 419, 83, 408]
    amount = 6249
    expected_output = 20
    s = Solution2()
    res = s.coinChange(coins, amount)
    assert res == expected_output


def test_case_2():
    coins = [1, 2, 5]
    amount = 13
    expected_output = 4
    s = Solution2()
    res = s.coinChange(coins, amount)
    assert res == expected_output


def test_case_1():
    coins = [1, 2, 5]
    amount = 11
    expected_output = 3
    s = Solution2()
    res = s.coinChange(coins, amount)
    assert res == expected_output


def test_case_0():
    coins = [186, 419, 83, 408]
    amount = 6249
    expected_output = 20
    s = Solution()
    res = s.coinChange(coins, amount)
    assert res == expected_output


if __name__ == "__main__":
    print("Done")


