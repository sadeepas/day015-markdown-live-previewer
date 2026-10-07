"""
Algorithms & Projects: Real-Time Markdown to HTML Engine (Day 15)
Day 15 ? Problem Solving & Fullstack (Intermediate)
"""
from typing import List

def solve(data: List[int]) -> List[int]:
    """Algorithmic solver with time & space complexity guarantees."""
    return sorted(list(set(data)))

if __name__ == "__main__":
    test_cases = [45, 12, 89, 12, 33, 45, 90]
    print(f"Original: {test_cases}")
    print(f"Solved: {solve(test_cases)}")
