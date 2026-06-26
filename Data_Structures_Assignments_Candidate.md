# Data Structures using Python — Practice Assignments

**For candidates · Bajaj Finance Ltd. · 2-Day Hands-On**

These exercises follow the two-day notebook. Each one is short and framed around a lending / banking situation so the data structure has a reason to exist. Work in a Jupyter or Colab cell — everything here uses only the standard library (plus `collections` and `time`, which are built in).

**How to approach each one**
- Read the story, then the task.
- Write the smallest code that produces the expected output.
- Predict the output *before* you run it — then check.
- A hint is provided, but try without it first.

> There is rarely one "correct" solution. Clear, working code that produces the right result is the goal.

---

## Assignment 1 — Which query will choke? (Big-O intuition)

**Story.** The reporting team has two queries. `query_a` looks up a single customer by position in a list. `query_b` compares every transaction against every other transaction to find duplicates. Tonight the data set grows from 1,000 rows to 10,000 rows.

**Your task.**
1. Write `query_a(data)` that returns `data[0]` (a single lookup).
2. Write `query_b(data)` that counts how many pairs of equal values exist (a nested loop over `data`).
3. Time both on a list of size 1,000 and again on size 10,000. Print the four timings.
4. In a comment, state which query's time grew roughly 100× and why.

**Expected output (shape, numbers will vary).**
```
query_a  n=1000:    0.001 ms   n=10000:    0.001 ms
query_b  n=1000:   12.ishms    n=10000: 1200.ishms
# query_b is O(n^2): 10x data -> ~100x time
```

**Hint.** Use `time.perf_counter()` around each call. `list(range(n))` makes test data quickly.

---

## Assignment 2 — The teller's transaction log (Linked List)

**Story.** A branch teller wants a running log of today's transactions where the **most recent** transaction is always at the front, ready to display first.

**Your task.**
1. Using a `Node` class and a simple linked list, add transactions so each new one goes to the **front**.
2. Add a method `total()` that walks the chain and returns the sum of all amounts.
3. Add the amounts `1500`, `320`, `9800` (in that order) and print the chain front-to-back, then the total.

**Expected output.**
```
chain (newest first): [9800, 320, 1500]
total: 11620
```

**Hint.** Front insertion means `new_node.next = self.head; self.head = new_node`. To total, start at `head` and follow `.next` until `None`.

---

## Assignment 3 — Is the formula valid? (Stack)

**Story.** Analysts type interest formulas like `((principal + rate) * years)`. Before the system evaluates one, it must check the **brackets are balanced** — every `(` has a matching `)`. An unbalanced formula should be rejected.

**Your task.**
1. Write `is_balanced(formula)` that returns `True` if the parentheses are balanced, `False` otherwise.
2. Test it on `"((a + b) * c)"`, `"(a + b))"`, and `"(a + (b * c)"`.

**Expected output.**
```
((a + b) * c)   -> True
(a + b))        -> False
(a + (b * c)    -> False
```

**Hint.** Push every `(` onto a stack (a list). On every `)`, pop one. If you ever pop from an empty stack, it's unbalanced; if the stack isn't empty at the end, it's unbalanced.

---

## Assignment 4 — The loan application desk (Queue)

**Story.** Loan applications must be processed strictly in the order received — first come, first served. A few "priority" applications from premier customers must jump to the **front** of the line, though.

**Your task.**
1. Use `collections.deque` as the queue.
2. Enqueue `APP-1`, `APP-2`, `APP-3` at the back (normal arrivals).
3. A premier application `APP-PRIORITY` arrives and must go to the **front**.
4. Process (dequeue) everything and print the processing order.

**Expected output.**
```
processing order: ['APP-PRIORITY', 'APP-1', 'APP-2', 'APP-3']
```

**Hint.** `deque` has `append()` (back), `appendleft()` (front), and `popleft()` (process from front).

---

## Assignment 5 — A fast account index (Binary Search Tree)

**Story.** A branch has account numbers scattered in no particular order. You need an index that can (a) answer "does this account exist?" quickly and (b) print all accounts in sorted order for the daily report.

**Your task.**
1. Insert these account numbers into a BST: `4200, 1500, 9800, 320, 6000`.
2. Search for `9800` (present) and `5000` (absent), printing both results.
3. Print all accounts in sorted order using in-order traversal.

**Expected output.**
```
9800 present? True
5000 present? False
sorted accounts: [320, 1500, 4200, 6000, 9800]
```

**Hint.** Smaller keys go left, larger keys go right. In-order traversal (left, node, right) yields sorted output.

---

## Assignment 6 — Tracing the money trail (Graph traversal)

**Story.** Compliance has flagged account **A**. They need the list of every account reachable from A through a chain of transfers — the potential "ring" around the flagged account.

**Your task.** Given this transfer network (an edge `X -> Y` means money flowed from X to Y):
```python
transfers = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": [],
    "E": ["A"],   # note: E loops back to A
}
```
1. Write a function that returns every account reachable from a starting account (use BFS or DFS).
2. Run it from `"A"` and print the reachable accounts.

**Expected output (order may vary by method).**
```
reachable from A: ['A', 'B', 'C', 'D', 'E']
```

**Hint.** Keep a `visited` set so the `E -> A` loop doesn't make you go round forever. BFS uses a queue (`deque`); DFS uses a stack (a list) or recursion.

---

## Assignment 7 — Rank the branch's top accounts (Sorting)

**Story.** At month-end, the branch wants its accounts ranked by balance, highest first, to identify top relationships.

**Your task.** Given:
```python
accounts = [("Riya", 4200), ("Amit", 9800), ("Neha", 320), ("Vikram", 6000)]
```
1. Sort the accounts by balance, **highest first**.
2. Print the ranked list.
3. (Optional) Do it once with Python's built-in `sorted()` and once with your own simple sort, and confirm they match.

**Expected output.**
```
1. Amit     9800
2. Vikram   6000
3. Riya     4200
4. Neha      320
```

**Hint.** `sorted(accounts, key=lambda pair: pair[1], reverse=True)` sorts by the second item descending.

---

## Assignment 8 — The in-memory customer directory (Hashing)

**Story.** A small service keeps a directory of customers keyed by account number, in a fixed-size table of 7 slots. Two of the accounts will collide (land in the same slot) — the directory must still store and retrieve both correctly.

**Your task.**
1. Build a tiny hash table of size 7 using **separate chaining** (each slot is a list).
2. Insert: `4200 -> "Savings"`, `75 -> "Loan"`, `320 -> "Current"`. (Note `75 % 7 == 5` and `320 % 7 == 5` — a collision.)
3. Print the buckets, then retrieve account `320`.

**Expected output.**
```
buckets: [[[4200, 'Savings']], [], [], [], [], [[75, 'Loan'], [320, 'Current']], []]
get 320 -> Current
```

**Hint.** Slot index is `key % 7`. Each slot starts as `[]`; on insert, append `[key, value]` to that slot's list. To retrieve, scan only that one slot's list.

---

## Assignment 9 (stretch) — End-of-day batch

**Story.** Tie three structures together. At end of day the branch must: take applications in arrival order (queue), rank approved loan amounts (sort), and keep a quick lookup of approved accounts (dict).

**Your task.**
1. Start with a queue of applications: `[("APP-1", 4200), ("APP-2", 9800), ("APP-3", 320)]` (id, amount).
2. Process them in arrival order; build a `dict` mapping id → amount as you go.
3. After processing, print the applications **ranked by amount, highest first**, and show a single O(1) lookup of `"APP-2"`'s amount from your dict.

**Expected output.**
```
processed in order: APP-1, APP-2, APP-3
ranked: [('APP-2', 9800), ('APP-1', 4200), ('APP-3', 320)]
lookup APP-2 -> 9800
```

**Hint.** Dequeue with `popleft()`; build the dict during processing; rank with `sorted(..., key=..., reverse=True)`; look up with `directory["APP-2"]`.

---

*End of assignments. Aim for clear, working code — and check each output against the expected result.*
