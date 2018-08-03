"""
Solution to Codewar's 'Ziggurat Ride of Fortune' problem by docgunthrop. A full problem description is found at:
https://www.codewars.com/kata/ziggurat-ride-of-fortune
"""

from typing import List, Tuple, Dict, Union


class Explorer:
    """Explorer object which 'moves' about in the artifact"""
    
    def __init__(self, y: int, x: int = 0, direction: str = "E"):
        """
        :param y: The vertical start coordinate.
        :param x: The horizontal start coordinate.
        :param direction: The initial explorer direction.
        """
        self._x = x
        self._y = y
        self._dir = direction
    
    def move(self) -> None:
        """Moves the explorer by 1 unit given their current direction"""
        east_west_movement = {"E": 1, "W": -1}
        north_south_movement = {"N": -1, "S": 1}
        if self._dir in east_west_movement:
            self._x += east_west_movement[self._dir]
        else:
            self._y += north_south_movement[self._dir]

    @property
    def get_dir(self) -> str:
        return self._dir

    @property
    def get_x(self):
        return self._x

    @property
    def get_y(self):
        return self._y

    def change_dir(self, direction) -> None:
        self._dir = direction
               

class Switch(object):
    """Switch object which has two states: A or B. An Explorer will change direction upon entering a Switch"""

    def __init__(self, state: str, x: int, y: int):
        """
        :param state: Current Switch state. Must be either 'A' or 'B'
        :param x: Switch x coordinate.
        :param y: Switch y coordinate.
        """
        self.state = state
        self.x = x
        self.y = y
    
    def state_change(self) -> None:
        """Changes the artifact's state from A to B or from B to A"""

        state_dict = {"A": "B", "B": "A"}
        self.state = state_dict[self.state]
    
    def operation(self, explorer: Explorer) -> None:
        """This method changes the explorer's direction based on
        the artifact's current state, and then changes the Switch's state"""

        direction_dict = {"A": {"W": "N", "E": "S", "S": "E", "N": "W"},
                          "B": {"W": "S", "E": "N", "S": "W", "N": "E"}}
        explorer.change_dir(direction_dict[self.state][explorer.get_dir])
        self.state_change()
    
    def __repr__(self):
        return "state: {}, x: {}, y: {}".format(self.state, self.x, self.y)


def ride(explorer_list: List[int], switch_list: List[List[str]], switch_coordinates: Dict[Tuple[int, int], Switch]) \
        -> List[Union[None, List[int]]]:
    """Determines the explorer's final destination"""
    result = [] 
    exit_north_south = {"N": 0, "S": len(switch_list) - 1}
    exit_east_west = {"E": len(switch_list[0]) - 1, "W": 0}
    for y_position in explorer_list:
        explorer = Explorer(y_position)
        # While explorer is still in the artifact and has not exited it
        while True:                              
            if (explorer.get_x, explorer.get_y) in switch_coordinates:
                switch = switch_coordinates[(explorer.get_x, explorer.get_y)]
                switch.operation(explorer)
            if explorer.get_x == 0 and explorer.get_dir == "W":
                result.append(None)
                break           
            elif explorer.get_dir in exit_east_west:
                if exit_east_west[explorer.get_dir] == explorer.get_x:
                    result.append([explorer.get_y, explorer.get_x])
                    break
            elif explorer.get_dir in exit_north_south:
                if exit_north_south[explorer.get_dir] == explorer.get_y:
                    result.append([explorer.get_y, explorer.get_x])
                    break
            explorer.move()              
    return result


def create_switch_coordinates(array: List[List[str]]) -> Dict[Tuple[int, int], Switch]:
    """Finds all Switch coordinates"""
    switch_coordinates = dict()
    for col in range(len(array)):
        for row in range(len(array)):
            value = array[col][row]
            if value != " ":
                switch_coordinates[(row, col)] = Switch(value, row, col)
    return switch_coordinates


def ride_of_fortune(matrix: List[str], explorers: List[int]) -> List[Union[None, List[int]]]:
    """Main function"""
    positions = [list(row) for row in matrix]
    artifact_coords = create_switch_coordinates(positions)
    return ride(explorers, positions, artifact_coords)
