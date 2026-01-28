"""
Insure an Investment

Your friend just purchased a share on a stock for S_0 = 100 dollars. (All numbers presented are examples and will vary in the coding task.)
 Alas, he's now worried that the investment might lose its value. To hedge against this risk, your friend asks you to insure him against future
  loss of value. Specifically, after T = 52 weeks, if the share price S_T has dropped below S_0, you compensate him the difference S_0 - S_T.

How much should you charge for such insurance? You have decided to value the insurance by its expected compensation at time T.
 (This ignores time value of money, but is appropriate in a zero interest rate environment.)

After each week, you expect the stock to either go up by a factor of u = 1.02 with probability p = 0.495, or down by a factor of d = 1 / u otherwise.
 This yields a simulation procedure — a discrete "random walk" — from which you can derive the final share price S_T and thus the realized insurance compensation.

Task
Given S_0, T, u and p, calculate the value of the insurance; that is, the expected insurance compensation.

The number of weeks T is always an integer between 1 and 52 * 5 = 260, inclusive. Remember, the simulation is discrete in time, with the stock price changing each week.

Example
For the above values S_0 = 100, T = 52, u = 1.02 and p = 0.495, the insurance value is roughly 5.6695 dollars. Your answer should be within 0.01% of the correct answer.

Notes
Here we concentrate on the programming challenge, and will not cover where the u and p parameters come from. In particular, you may wonder why p < 0.5 in all
tests — shouldn't stocks have a tendency to rise, not fall? The answer is that p does not reflect the true probability of a share price increase, but is determined solely by the riskiness of the stock. Such p can still be interpreted as the probability of the price going up, just in an "alternative world".

While this sounds complex, it can be shown that this is the only way to produce fairly priced investment insurance. To keep things simple,
we provide the proper p in this kata as a parameter. If you are interested in the full theory, look into (lattice-based) options pricing.

uttumuttu
https://www.codewars.com/kata/664d80ea3f11c760dc23c35f/train/python
"""

from math import comb


def insurance_value(S_0, T, u, p):
    d = 1 / u
    expected_value = 0.0

    for k in range(T + 1):
        S_T = S_0 * (u ** k) * (d ** (T - k))

        payoff = max(0.0, S_0 - S_T)

        if payoff > 0:
            prob = comb(T, k) * (p ** k) * ((1 - p) ** (T - k))
            expected_value += payoff * prob

    return expected_value
