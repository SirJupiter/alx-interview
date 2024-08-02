#!/usr/bin/python3
"""Lockboxes"""

def canUnlockAll(boxes):
    """
    Method that determines if all boxes can be opened

    Args:
        boxes: list of list of integers

    Returns:
        True if all boxes can be opened
        False if otherwise
    """

    # Initialize visited list to keep track of opened boxes
    visited = [False] * len(boxes)
    visited[0] = True  # Start with the first box
    keys = boxes[0]  # Keys from the first box
    queue = [0]  # Queue to hold boxes to explore

    while queue:
        box_index = queue.pop(0)  # Get the next box to explore

        # Loop through keys in the current box
        for key in boxes[box_index]:
            # Check if the key corresponds to an unopened box
            if key < len(boxes) and not visited[key]:
                visited[key] = True  # Mark the box as opened
                queue.append(key)  # Add the box to the queue for exploration

    # Check if all boxes were visited
    return all(visited)
