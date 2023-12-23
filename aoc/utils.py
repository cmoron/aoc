def get_neighbors(matrix, row, col):
    """
    Get the neighboring cells of a given cell in a matrix.

    Parameters:
    matrix (list of list of int): The matrix in which to find neighbors.
    row (int): The row index of the cell.
    col (int): The column index of the cell.

    Returns:
    dict: A dictionary with keys as cardinal directions and values as neighboring cells.
          Missing neighbors (for edge cells) will not be included in the dictionary.
    """
    rows, cols = len(matrix), len(matrix[0])
    directions = {"N": (-1, 0), "NE": (-1, 1), "E": (0, 1), "SE": (1, 1), 
                  "S": (1, 0), "SW": (1, -1), "W": (0, -1), "NW": (-1, -1)
    }

    neighbors = {}
    for direction, (d_row, d_col) in directions.items():
        n_row, n_col = row + d_row, col + d_col
        if 0 <= n_row < rows and 0 <= n_col < cols:
            neighbors[direction] = matrix[n_row][n_col]

    return neighbors

def extract_columns(matrix):
    """
    Extracts columns from a given matrix.

    This function iterates over each column index of the matrix and collects elements
    from each row at that column index, effectively transposing the rows to columns.

    Parameters:
    matrix (list of lists): A 2D list representing the matrix from which columns are to be extracted. 
                             Assumes that all rows in the matrix are of the same length.

    Returns:
    list of lists: A list where each element is a list representing a column of the input matrix.

    Example:
    >>> extract_columns([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    Note:
    This function does not handle cases where rows in the matrix have different lengths.
    """

    return [[row[col_index] for row in matrix] for col_index in range(len(matrix[0]))]

def picks_theorem(area, boundaries):
    """
    Calculate the number of interior points in a simple polygon using Pick's Theorem.

    Pick's Theorem is used to relate the area of a simple polygon to the number of its interior and boundary points.
    The theorem states that the area of the polygon (A) can be calculated using the formula: A = i + b/2 - 1,
    where i is the number of interior points and b is the number of boundary points.

    Parameters:
    area (float or int): The area of the polygon. The total space within the boundary of the polygon.
    boundaries (int): The number of boundary points of the polygon. Points that lie on the perimeter of the polygon.

    Returns:
    int: The number of interior points within the polygon calculated using the formula: i = A - b/2 + 1,
         where i is the number of interior points, A is the area, and b is the number of boundary points.

    Example:
    >>> picks_theorem(20.5, 14)
    13.75

    Note:
    - Assumes the polygon is simple (does not intersect itself).
    - The area should be provided in a unit consistent with the boundary points.
    - Boundary points are considered as points lying exactly on the edge of the polygon.
    - Result accuracy depends on the accuracy of the input values for area and boundary points.
    """
    return area - boundaries / 2 + 1

def shoelace_formula(vertex):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.

    The Shoelace formula, also known as Gauss's area formula, computes the area of a simple polygon whose vertices are described in a sequence. The formula is given by: A = 1/2 * ∑(x_i * (y_(i+1) - y_(i-1))), for i = 1 to n, where A is the area of the polygon and n is the number of vertices.

    Parameters:
    vertex (list of tuples): A list of tuples representing the vertices of the polygon. Each tuple should contain two values (x, y), representing the coordinates of each vertex.

    Returns:
    float: The area of the polygon. The result is always non-negative.

    Example:
    >>> shoelace_formula([(0,0), (4,0), (4,4), (0,4)])
    16.0

    Note:
    - Assumes the polygon is simple (does not self-intersect).
    - The vertices should be provided in a consistent order (either clockwise or counterclockwise).
    - The first vertex does not need to be repeated at the end of the list.
    - The function is sensitive to the order of the vertices. Reversing the order will give the same area.
    """
    n = len(vertex)
    area = 0
    for i in range(n):
        x = vertex[i][0]
        j = (i + 1) % n
        area += x * (vertex[i-1][1] - vertex[j][1])
    return abs(area) / 2
