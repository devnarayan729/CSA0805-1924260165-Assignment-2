# Assignment 2 Report

Student name: To be filled in  
Register number: 1924260165

## Q1: Electricity subsidy

Before running the program, I predicted these results:

| Household | Units | Ration card | Member above 80 | Predicted result |
|---|---:|---|---|---|
| A | 100 | No | No | Full subsidy |
| B | 101 | Yes | No | Partial subsidy |
| C | 101 | No | No | No subsidy |
| D | 200 | Yes | No | Partial subsidy |
| E | 200 | No | No | No subsidy |
| F | 201 | No | Yes | Elderly exception subsidy |
| G | 201 | Yes | No | No subsidy |
| H | 80 | Yes | Yes | Full subsidy |

The program's observed output agrees with all eight predictions.

Both implementations give the same result because the three tested ranges do not overlap. Separate `if` statements can print more than one result when their conditions overlap. An `if`-`elif`-`else` chain selects only its first matching branch. For example, changing the second condition to `units <= 200 and ration_card` could give a household at 100 units two results.

Combined Boolean conditions make the policy readable here. A guarded `match` alternative could check `case _ if units <= 100`, then `case _ if 101 <= units <= 200 and ration_card`, followed by the elderly condition and a default case. With `k` slabs, either a chain or a searched list takes O(k) time. The chain uses O(1) extra space; the list uses O(k) space. A match statement also uses O(1) extra space for these conditions.

Review: Testing 100, 101, 200, and 201 made the limits easier to understand.

## Q2: OTP attempts

The program includes a `while` design and a `for` design. Blank responses are skipped and do not increment the `while` attempt count. The `for` loop calls a helper that skips blanks before each counted attempt. A correct OTP uses `break`; `continue` skips blank entries; `pass` is an empty placeholder branch. The loop `else` reports a lock only when the attempts finish without a successful `break`.

A `while` loop is natural when the number of counted inputs can change. Putting the counter update after a success check can miscount attempts; forgetting the update can cause an infinite loop. A correct security answer expands the limit from three to five. Both loop designs take O(a) time and O(1) extra space for `a` attempts. A recursive version also takes O(a) time, but uses O(a) call-stack space.

The recursive alternative would check the current OTP, return on success, and otherwise call itself with one fewer attempt. It would stop and lock when the remaining-attempt count reaches zero. The blank-input case would call itself again without reducing the remaining-attempt count. That design still takes O(a) time for `a` counted attempts, but uses O(a) stack space.

Review: The blank-entry test showed why loop iterations and real attempts are not always the same.

## Q3: Registration validation

The program removes spaces and hyphens, converts text to uppercase, and validates the state, district, series, and final four digits using slices and string methods. It prints a receipt format for valid entries and rejects malformed entries.

Strings are immutable, so `text.upper()` returns a new string and does not change `text`. For a valid 9-character string, `s[-4:]` is the last four digits and `s[4:-4]` is the one-letter series. For a valid 10-character string, `s[-4:]` is still the last four digits and `s[4:-4]` is the two-letter series. A regular expression with `fullmatch` can express the same format in one pattern. Both checks take O(L) time for text of length L; slicing is explicit about each field, while the expression is shorter but may be harder for a beginner to read.

The regular-expression alternative is `re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg) is not None`. Both approaches use O(L) time for input length L; the expression does not need to be kept after validation, while slicing creates short temporary strings.

Review: Normalising first lets the validator handle spaces, hyphens, and lowercase letters consistently.

## Q4: Building long text

The program compares repeated `+=`, `join`, and f-string line construction for 1,000, 10,000, and 200,000 lines. It makes three timing measurements for each method and prints every result and the average. These are the averages from this run:

| Lines | `+=` average | `join` average | f-string average |
|---:|---:|---:|---:|
| 1,000 | 0.000130 s | 0.000054 s | 0.000049 s |
| 10,000 | 0.001006 s | 0.000744 s | 0.000561 s |
| 200,000 | 0.346087 s | 0.017564 s | 0.017688 s |

The three raw timings for every method are saved in `Task04/output.txt`. Timing varies between computers and runs.

Strings cannot be changed in place. Repeated concatenation may copy existing text repeatedly, giving up to O(n²) copied characters. `join` processes the pieces together in O(n) time and needs memory for the pieces and final result. Another alternative is to open a file and write each formatted line as it is made, which takes O(n) time and avoids holding the full statement in memory. `io.StringIO` can be used similarly when the final result needs to be read as a string. CPython can sometimes optimise `+=`, but `join` clearly expresses the operation and performs well consistently.

Review: The timing output is generated on this computer and should be compared by method at the same input size.

## Q5: Functions and scope

The buggy function keeps one list in its default argument. The list is created when Python defines the function, so later calls share it. The corrected function starts a fresh list when `order` is `None`. The program shows three independent customer orders and prints `add_item_buggy.__defaults__`, which contains the shared list.

Positional arguments are useful for short, clear calls. Keyword arguments make the chosen parameter explicit. Default arguments support common values such as quantity one. `calculate_bill` returns both subtotal and tax as a tuple. Local names belong to a function call, `global` changes a module-level name, and `nonlocal` changes a name in an enclosing function. Global state is usually avoided because it makes functions less independent and harder to test.

Another safe design is to require the caller to create and pass an empty order list each time. This uses O(1) time per appended item and O(m) space for an order with m items. A closure can instead create an order list once inside an outer function and return an inner `add_item` function; that also uses O(1) time per item and O(m) space. Both approaches avoid a shared mutable default.

Review: Passing an order list explicitly keeps each customer's items separate.

## Q6: Recursion and limits

The base case returns one when there are zero or one steps. The recursive case adds the results for `n - 1` and `n - 2`. For five steps, the start of the call tree is `ways(5) -> ways(4) + ways(3)`, then `ways(4) -> ways(3) + ways(2)` and `ways(3) -> ways(2) + ways(1)`. This shows that `ways(3)` and `ways(2)` are calculated more than once. The answers for one through six steps are 1, 2, 3, 5, 8, and 13. The call counts for 10, 20, 25, and 30 compare plain recursion with memoisation. Memoisation saves completed results, but the recursive call stack still grows with `n`.

Plain recursion takes O(φⁿ) time, memoisation takes O(n) time and O(n) cache and stack space, and the loop takes O(n) time and O(1) extra space. The measured naive/memoised call counts are 177/11 at 10 steps, 21,891/21 at 20, 242,785/26 at 25, and 2,692,537/31 at 30. The memoised function's cached base case accounts for the call-count convention in these results. The program attempts the memoised calculation at 1,000 steps and reports a `RecursionError` if the interpreter's recursion limit is reached. Python reports a default limit of 1,000 here. The loop computes the same answer without increasing the recursion limit.

Review: Memoisation removes repeated calculations, while the loop also avoids recursion depth and cache storage.

## Q7: Redesign and validation

The original stairs function is the Q6 plain recursive version. Its work grows rapidly because it solves the same smaller staircases repeatedly. The redesign objective is to return the same answer for each tested input while making the number of additions grow linearly and using constant extra memory.

The redesigned loop keeps only the results for the previous two step counts. For each new step count, it adds those two values, then moves the stored values forward. It does not need a cache or a recursive call stack. The prediction is that for n=30, the redesign will use 29 additions instead of the many recursive calls made by the original.

The Q7 program runs both versions with the same n values, prints whether their answers agree, records call and addition counts, and measures their execution times. It also computes n=1,000 with the loop. At n=30, the run used 2,692,537 naive calls and 29 loop additions; both returned 1,346,269. The loop's timings may vary, but its linear operation count and constant extra space support the design objective. The original recursive version is still useful for explaining the recurrence on small inputs.

Review: Keeping the last two values is enough to calculate the next result, so the loop avoids storing the full history.
