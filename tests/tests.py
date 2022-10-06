import unittest

class TestInitialiseGrid(unittest.TestCase):
    def test_valid_equal_rows_columns(self):
        rows = 3
        columns = 3
        result = initialiseGrid(rows, columns)
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_valid_unequal_rows_columns(self):
        rows = 4
        columns = 3
        result = initialiseGrid(rows, columns)
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_valid_no_rows_columns(self):
        rows = 0
        columns = 0
        result = initialiseGrid(rows, columns)
        self.assertEqual(result, [])


class TestRandomiseGrid(unittest.TestCase):
    def test_valid_equal_rows_columns(self):
        rows = 3
        columns = 3
        result = randomiseGrid(rows, columns)
        numberOfRows = len(result)
        numberOfColumns = len(result[0])
        self.assertEqual(rows, numberOfRows)
        self.assertEqual(columns, numberOfColumns)

    def test_valid_unequal_rows_columns(self):
        rows = 4
        columns = 3
        result = randomiseGrid(rows, columns)
        numberOfRows = len(result)
        numberOfColumns = len(result[0])
        self.assertEqual(rows, numberOfRows)
        self.assertEqual(columns, numberOfColumns)

    def test_valid_no_rows_columns(self):
        rows = 0
        columns = 0
        result = randomiseGrid(rows, columns)
        self.assertEqual(result, [])


class TestNextGenerationGridDeadCells(unittest.TestCase):
    def test_dead_cells_no_live_neighbours_dies(self):
        initialGrid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
        expectedNextGenGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        actualGrid = nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_dead_cells_3_live_neighbours_alive(self):
        initialGrid = [[0, 0, 1], [0, 1, 1], [0, 0, 0]]
        expectedNextGenGrid = [[0, 1, 1], [0, 1, 1], [0, 0, 0]]
        actualGrid = nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)


class TestNextGenerationGridLiveCells(unittest.TestCase):
    def test_live_cells_0_live_neighbours_dies(self):
        initialGrid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        expectedNextGenGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        actualGrid = nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_live_cells_1_live_neighbours_dies(self):
        initialGrid = [[1, 0, 0], [1, 0, 0], [0, 0, 0]]
        expectedNextGenGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        actualGrid = nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_live_cells_2_live_neighbours_stay_alive(self):
        initialGrid = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
        expectedNextGenGrid = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        actualGrid = nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_live_cells_3_live_neighbours_stay_alive(self):
        initialGrid = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        expectedNextGenGrid = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        actualGrid = nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)

    def test_live_cells_4_live_neighbours_dies(self):
        initialGrid = [[1, 1, 1], [1, 1, 0], [0, 0, 0]]
        expectedNextGenGrid = [[1, 0, 1], [1, 0, 1], [0, 0, 0]]
        actualGrid = nextGenerationGrid(initialGrid)
        self.assertEqual(expectedNextGenGrid, actualGrid)


class TestNextGenerationValue(unittest.TestCase):
    def test_next_generation_value(self):
        rows = 3
        columns = 3
        grid = [[0, 0, 1], [1, 0, 0], [1, 1, 1]]
        expectedResult = [[0, 0, 0], [1, 0, 1], [1, 1, 0]]

        for i in range(0, rows):
            for j in range(0, columns):
                value = nextGenerationValue(i, j, rows, columns, grid)
                self.assertEqual(value, expectedResult[i][j])


class TestRunGameOfLife(unittest.TestCase):
    def test_incorrect_option(self):
        rows = 3
        columns = 3
        option = 3
        self.assertEqual("Test", runGameOfLife(rows, columns, option))


if __name__ == '__main__':
    unittest.main()
