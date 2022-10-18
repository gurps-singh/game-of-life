import io
import unittest.mock

from src import gameOfLife


class TestInitialiseGrid(unittest.TestCase):
    def test_valid_equal_rows_columns(self):
        rows = 3
        columns = 3
        result = gameOfLife.initialiseGrid(rows, columns)
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_valid_unequal_rows_columns(self):
        rows = 4
        columns = 3
        result = gameOfLife.initialiseGrid(rows, columns)
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_valid_no_rows_columns(self):
        rows = 0
        columns = 0
        result = gameOfLife.initialiseGrid(rows, columns)
        self.assertEqual(result, [])


class TestRandomiseGrid(unittest.TestCase):
    def test_valid_equal_rows_columns(self):
        rows = 3
        columns = 3
        result = gameOfLife.randomiseGrid(rows, columns)
        numberOfRows = len(result)
        numberOfColumns = len(result[0])
        self.assertEqual(rows, numberOfRows)
        self.assertEqual(columns, numberOfColumns)

    def test_valid_unequal_rows_columns(self):
        rows = 4
        columns = 3
        result = gameOfLife.randomiseGrid(rows, columns)
        numberOfRows = len(result)
        numberOfColumns = len(result[0])
        self.assertEqual(rows, numberOfRows)
        self.assertEqual(columns, numberOfColumns)

    def test_valid_no_rows_columns(self):
        rows = 0
        columns = 0
        result = gameOfLife.randomiseGrid(rows, columns)
        self.assertEqual(result, [])


class TestNextGenerationGridDeadCells(unittest.TestCase):
    def test_dead_cells_no_live_neighbours_dies(self):
        initialGrid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
        expectedNextGenGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        actualGrid = gameOfLife.nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_dead_cells_3_live_neighbours_alive(self):
        initialGrid = [[0, 0, 1], [0, 1, 1], [0, 0, 0]]
        expectedNextGenGrid = [[0, 1, 1], [0, 1, 1], [0, 0, 0]]
        actualGrid = gameOfLife.nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)


class TestNextGenerationGridLiveCells(unittest.TestCase):
    def test_live_cells_0_live_neighbours_dies(self):
        initialGrid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        expectedNextGenGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        actualGrid = gameOfLife.nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_live_cells_1_live_neighbours_dies(self):
        initialGrid = [[1, 0, 0], [1, 0, 0], [0, 0, 0]]
        expectedNextGenGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        actualGrid = gameOfLife.nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_live_cells_2_live_neighbours_stay_alive(self):
        initialGrid = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
        expectedNextGenGrid = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        actualGrid = gameOfLife.nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_live_cells_3_live_neighbours_stay_alive(self):
        initialGrid = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        expectedNextGenGrid = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        actualGrid = gameOfLife.nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_live_cells_4_live_neighbours_dies(self):
        initialGrid = [[1, 1, 1], [1, 1, 0], [0, 0, 0]]
        expectedNextGenGrid = [[1, 0, 1], [1, 0, 1], [0, 0, 0]]
        actualGrid = gameOfLife.nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)


class TestNextGenerationValue(unittest.TestCase):
    def test_next_generation_value(self):
        rows = 3
        columns = 3
        grid = [[0, 0, 1], [1, 0, 0], [1, 1, 1]]
        expectedResult = [[0, 0, 0], [1, 0, 1], [1, 1, 0]]

        for i in range(0, rows):
            for j in range(0, columns):
                value = gameOfLife.nextGenerationValue(i, j, rows, columns, grid)
                self.assertEqual(value, expectedResult[i][j])


class TestRunGameOfLife(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_higher_than_limit(self, mock_stdout):
        rows = 101
        columns = 101
        option = 3
        gameOfLife.runGameOfLife(rows, columns, option)
        self.assertEqual(
            'The number of rows or columns specified is above the limit permitted, please use a lower value\n',
            mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
