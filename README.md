# Page Replacement Algorithm Simulator

A Python-based Operating Systems Lab project that simulates FIFO, LRU, and Optimal page replacement algorithms.

## Features

- User input for page reference string and number of frames
- Step-by-step frame tables
- HIT and FAULT identification
- Total page hits and page faults
- Hit ratio and fault ratio calculations
- Performance comparison of all three algorithms
- Input validation
- No external Python libraries required

## Algorithms

- **FIFO:** Replaces the page that entered memory first.
- **LRU:** Replaces the page that has not been used for the longest time.
- **Optimal:** Replaces the page whose next use is farthest in the future.

## Requirements

- Python 3
- Visual Studio Code or another Python editor

## How to Run

Clone or download this repository.

Open the project folder in your terminal and run:

```bash
python page_replacement.py
```

Example input:

```text
1 2 3 1 4 2 5
3
```

The program displays each algorithm's frame states, page hits, page faults, ratios, and a final comparison table.

## Sample Performance Results

For reference string `1 2 3 1 4 2 5` with three frames:

| Algorithm | Hits | Faults |
|---|---:|---:|
| FIFO | 2 | 5 |
| LRU | 1 | 6 |
| Optimal | 2 | 5 |

Results depend on the reference string and frame capacity.

## Project Structure

```text
Page-Replacement-Simulator/
├── page_replacement.py
├── Project_Report.
├── manual_tracing
├── README.md

└── screenshots/


## Learning Outcomes

- Understanding virtual memory and page replacement
- Implementing algorithms in Python
- Calculating performance metrics
- Analysing algorithm behaviour
- Using GitHub for project documentation

## Author

**Shalini Sharma**  
B.Tech – Computer Science Engineering (Data Analytics)

## Academic Project

Operating Systems Lab | 2026
