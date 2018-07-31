from unittest import TestCase, main as unittest_main
from ride_of_fortune import Explorer, Switch, create_switch_coordinates, ride_of_fortune
 
 
class TestExplorer(TestCase):
    
    def setUp(self):
        self.explorer = Explorer(3, 3)
        
    def test_first_movement(self):
        self.explorer.change_dir("N")
        self.explorer.move()
        self.assertEqual(self.explorer.get_y, 2)
        self.assertEqual(self.explorer.get_x, 3)
    
        self.explorer.change_dir("W")
        self.explorer.move()
        self.assertEqual(self.explorer.get_y, 2)
        self.assertEqual(self.explorer.get_x, 2)


class TestSwitch(TestCase):
    
    def setUp(self):
        self.explorer = Explorer(4)
        self.artifact = Switch("B", 4, 4)
    
    def test_artifact_operation(self):
        self.artifact.operation(self.explorer)
        self.assertEqual(self.explorer._dir, "N")
        self.assertEqual(self.artifact.state, "A")
        
        self.artifact.operation(self.explorer)
        self.assertEqual(self.explorer._dir, "W")
        self.assertEqual(self.artifact.state, "B")


class TestCreateArtifactCoordinatesFunction(TestCase):

    def test_artifact_return_dict(self):
        artifact_list = [
            [' ', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'A', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'A', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ']
        ] 
        artifact_coords = create_switch_coordinates(artifact_list)
        coords = [(2, 0), (4, 1), (1, 4), (3, 5)]
        self.assertEqual(len(artifact_coords), 4)
        for coord in coords:
            self.assertIn(coord, artifact_coords)
            self.assertEqual(
                artifact_coords[coord].state, 
                artifact_list[coord[1]][coord[0]]
            )


class TestMain(TestCase):
    
    def test_main(self):
        # artifact_list = [
        #     [' ', ' ', 'B', 'A', ' ', ' '],
        #     [' ', ' ', ' ', ' ', 'A', 'B'],
        #     [' ', ' ', ' ', ' ', ' ', ' '],
        #     [' ', 'A', ' ', ' ', ' ', ' '],
        #     [' ', 'B', ' ', ' ', ' ', ' '],
        #     [' ', ' ', ' ', ' ', 'A', 'A']
        # ]
        artifact_list = [
            '  BA  ',
            '    AB',
            '      ',
            ' A    ',
            ' B    ',
            '    AA'
            ]
        final_destination = ride_of_fortune(artifact_list, [0, 1, 3, 2, 5])
        self.assertEqual(
            final_destination,
            [[0, 2], [5, 5], None, [2, 5], [0, 5]]
        )


if __name__ == "__main__":
    unittest_main()
