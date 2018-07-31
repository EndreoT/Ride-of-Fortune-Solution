# Ride-of-Fortune-Solution
Solution to Codewar's 'Ziggurat Ride of Fortune' problem by docgunthrop. Please see the full problem description at:
https://www.codewars.com/kata/ziggurat-ride-of-fortune

******** The following description is taken directly from https://www.codewars.com/kata/ziggurat-ride-of-fortune**********

You and a group of explorers have found a legendary ziggurat hidden in an obscure jungle. According to legend, the ancient structure houses portals to other worlds.

The outer west wall of the ziggurat consists of a series of entrance doors. When an explorer enters through a door, they sit in a mobile cart that moves in a straight path until it reaches a "switch" or hits a wall.

A switch re-routes the cart either left or right, depending on the state of the switch and the cart's movement direction.

Interdimensional portals line the entire north, east, and south walls inside the ziggurat. If a cart hits one of these walls, the occupying explorer exits through the portal before them. If a cart ends at the west wall, the explorer exits through a door and returns back outside.

The expedition leader has assigned to you the task of keeping track of the exit points of each explorer. You are given an artifact that provides you with a map of the ziggurat's inner chamber.

Switch Mechanics

Above is a representation of a switch. It exists in one of two states A or B.

If a switch is in the A state and and a cart enters by moving:
west, they are routed north
east, they are routed south
south, they are routed east
north, they are routed west
If the switch were in the B state, the cart would be routed in the orthogonal direction opposite to that for the A state.
Immediately after a cart passes through a switch, the switch changes state by rotating 90 degrees.
Cart Pathing

Above left is an example ziggurat with four switches in their initial states. The S in the green arrow represents the initial position of the explorer who enters the structure through door 1.
The switches at [1,1], [1,4], and [4,1] begin in state A, while the switch at [4,4] begins in state B.

The left image shows the path followed by the cart (in sequence, denoted by the white dashed arrows labeled 1, 2, and 3). First it travels through the switch at [1,1], then [4,1], and then [4,4].
The right image shows the remainder of the cart's path, up to the explorer's exit (marked by the red arrow).
By step 4 (after exiting the switch at [1,4]), the state of all four switches have changed, as shown above.
The end state for the switch at [1,4] is B, while the rest end in state A.
If the next explorer in sequence were also to enter through door 1, they would exit through the portal at [5,4].
Input
Your function will receive two arguments:

An n x n matrix representing the layout of the ziggurat interior.
An array/list of the doors (rows) entered by each explorer in sequence. Assume each following explorer enters immediately after the preceding explorer has exited.
Output
Your function should return an array of the exit points of explorers who exit through portals and null/None for those who return back outside.

Test Example
artifact = [
    '      ',
    ' A  A ',
    '      ',
    '      ',
    ' A  B ',
    '      ']
explorers = [1,1,0,3,4,4,2,5,1,4]
ride_of_fortune(artifact,explorers) #[None,[5,4],[0,5],[3,5],[0,4],[5,1],[2,5],[5,5],None,[5,1]]
Technical Constraints
Ziggurat size n range: 40 >= n >= 6
Final Test Suite: 15 fixed tests, 100 random tests
JavaScript: prototypes have been frozen and require has been disabled
Inputs will always be valid
