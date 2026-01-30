# Bin Packing Algorithms with ZipZip Tree (O(n log n) Expected)

Experimental evaluation of classic bin packing heuristics (NF, FF, BF, FFD, BFD).
To meet the expected **O(n log n)** performance requirement for FF/BF (and decreasing variants),
this project implements a **ZipZip Tree** (balanced randomized BST) from scratch and uses it
as the core data structure for efficient bin selection and updates.

---

## Overview
Bin packing is the problem of placing items (sizes in (0, 1]) into the minimum number of unit-capacity bins.
This repository implements and benchmarks five well-known heuristics:

- Next Fit (NF)
- First Fit (FF)
- Best Fit (BF)
- First Fit Decreasing (FFD)
- Best Fit Decreasing (BFD)

The key engineering constraint is that FF/BF/FFD/BFD must run in **expected O(n log n)** time.
To achieve this, the implementation uses a custom ZipZip Tree for logarithmic-time operations
during packing (rather than a naive linear scan across bins).

---

## Key Ideas
### Why ZipZip Tree?
Naive FF/BF implementations can degrade to **O(n²)** because each item may scan many bins.
This project maintains bin state in a ZipZip Tree to support expected **O(log n)** operations,
enabling FF/BF and their decreasing variants to scale to large input sizes.

### How it’s used (high-level)
- Each bin is represented by its **remaining capacity** (and an identifier).
- For **First Fit**: find the first bin that can accommodate an item efficiently (log-time search + updates).
- For **Best Fit**: find the tightest bin that still fits (predecessor/successor-style query).
- After placing an item: update the bin’s remaining capacity in the tree (delete + reinsert or key update).

*(Exact details depend on your internal representation; adjust the bullet wording if needed.)*

---

## Implementation Notes
- **ZipZip Tree** is implemented from scratch (no external balanced-tree libraries).
- Packing algorithms are implemented as separate functions/modules for clarity.
- Experimental results (raw) are stored under `data/`.

---

## Project Structure
```text
.
├── src/
│   ├── best-fit.py        # Best Fit bin packing implementation (uses ZipZip Tree)
│   ├── first_fit.py       # First Fit bin packing implementation (uses ZipZip Tree)
│   └── next_fit.py        # Next Fit bin packing implementation
│   └── zipzip_tree.py     # ZipZip Tree (balanced randomized BST) implementation
├── data/
│   └── results.xlsx       # Raw experiment results
├── README.md
└── .gitignore

```

```md
Each bin packing heuristic is implemented as an independent module under `src/`
to keep algorithm logic isolated and easy to compare.

- `next_fit.py` implements the baseline Next Fit algorithm.
- `first_fit.py` and `best_fit.py` implement First Fit and Best Fit using a ZipZip Tree
  to achieve expected O(n log n) performance.
- `zipzip_tree.py` provides a custom balanced randomized binary search tree
  used for efficient bin selection and updates.
