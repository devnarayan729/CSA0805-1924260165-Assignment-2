# Assignment 2 Report

Student name: To be filled in  
Register number: 1924260165

## Q1: Electricity subsidy

| Household | Units | Ration card | Member above 80 | Predicted result |
|---|---:|---|---|---|
| A | 100 | No | No | Full subsidy |
| B | 101 | Yes | No | Partial subsidy |
| C | 101 | No | No | No subsidy |
| D | 200 | Yes | No | Partial subsidy |
| E | 200 | No | No | No subsidy |
| F | 201 | No | Yes | Elderly exception |
| G | 201 | Yes | No | No subsidy |
| H | 80 | Yes | Yes | Full subsidy |

The program matched all predictions. Separate `if` statements can give multiple results if conditions overlap. `if`-`elif`-`else` picks one result. Combined conditions are clearest here. For `k` slabs, a chain or searched list takes O(k) time; the chain uses O(1) extra space and the list O(k).

Review: Testing boundary values helped me check the rules.

## Q2: OTP attempts

The program shows both loop types. Blank responses do not count. `continue` skips blanks, `break` stops after success, and `pass` is an empty statement. The loop `else` locks after failed attempts. A correct security answer gives two extra attempts.

`while` is useful when the attempt count can change. A missed counter update can cause an infinite loop. Both loops take O(a) time and O(1) space for `a` attempts. Recursion also takes O(a) time, but uses O(a) stack space.

Review: Blank entries should not use up an attempt.

## Q3: Registration validation

The program removes spaces and hyphens, changes letters to uppercase, validates each part, and formats valid numbers for printing. `upper()` returns a new string because strings cannot be changed in place. For 9 or 10 characters, `s[-4:]` gives the last four digits; `s[4:-4]` gives the series letters.

A regular expression can validate the same pattern. Both methods take O(L) time for a string of length L. Slicing shows each part clearly.

Review: Normalising first makes the input easier to validate.

## Q4: Building long text

The program measures `+=`, `join`, and f-strings three times each. These are average times from one run:

| Lines | `+=` | `join` | f-string |
|---:|---:|---:|---:|
| 1,000 | 0.000130 s | 0.000054 s | 0.000049 s |
| 10,000 | 0.001006 s | 0.000744 s | 0.000561 s |
| 200,000 | 0.346087 s | 0.017564 s | 0.017688 s |

The raw times are in `Task04/output.txt`. Strings cannot be changed in place, so repeated `+=` may copy text many times. `join` takes O(n) time and is a good choice for many pieces. Writing directly to a file can use less memory.

Review: In my test, `join` was much faster for 200,000 lines.

## Q5: Functions and scope

The buggy function reuses its default list between calls. Using `None` and creating a new list fixes this. The program shows separate customer orders and prints the shared default list.

Positional arguments are simple; keyword arguments name the values; defaults provide common values. A function can return multiple values as a tuple. Local names belong to a function, `global` refers to a module-level name, and `nonlocal` refers to an enclosing function's name. Passing a new list to each customer also avoids shared orders.

Review: A new list keeps each customer's order separate.

## Q6: Recursion and limits

The base case is zero or one step; otherwise, the function adds results for `n-1` and `n-2`. For 1–6 steps, the answers are 1, 2, 3, 5, 8, 13. Plain recursion repeats work: calculating five steps calls the three-step calculation more than once.

Naive/memoised call counts: 10 steps: 177/11; 20: 21,891/21; 25: 242,785/26; 30: 2,692,537/31. Naive recursion takes O(φⁿ) time. Memoisation takes O(n) time and space. The loop takes O(n) time and O(1) extra space. The memoised version hits the recursion limit at 1,000 steps; the loop works without raising it.

Review: The loop is a better choice for a large number of steps.

## Q7: Redesign and validation

The naive stairs function recalculates the same values. The redesign keeps only the last two results and uses them to calculate the next one.

At 30 steps, both programs returned 1,346,269. The naive version made 2,692,537 calls; the loop used 29 additions. The loop also calculates 1,000 steps with O(1) extra space. This meets the goal of fewer calculations and less memory.

Review: Saving only the last two results makes the loop simple and efficient.
