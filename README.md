# Cooperative Slider Puzzle for oTree

![Image of the puzzle](puzzle.png)

## Overview
This app implements a simple 3x3 slider puzzle. There are two variants: A two player cooperative game and a single player variant. 

 In the single player variant, the goal is to solve puzzles until time runs out.
 
 In the two player game, the players of a group take turns to move one tile at a time. The goal is to solve the puzzle in a given time limit. Interaction takes place in real time. See the installation section below on how to set the app up correctly.

In the two-player version, moves are stored (in a very crude fashion). This can be added to the single player variant as well.

## Installation
1. Download or clone the project and copy the apps into your oTree project folder, next to your other app folders. 

For the two-player variant:
2. Add ``slider_puzzle`` to your ``EXTENSION_APPS`` section of ``settings.py``:
```python
EXTENSION_APPS  = ['slider_puzzle'].
```
