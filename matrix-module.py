def __init__(self, rows):
    error = TypeError(
        "Matrices must be formed from a list of zero or more lists containing at "
        "least one and the same number of values, each of which must be of type "
        "int or float."
    )
    if len(rows) != 0:
        cols = len(rows[0])
        if cols == 0:
            raise error
        for row in rows:
            if len(row) != cols:
                raise error
            for value in row:
                if not isinstance(value, (int, float)):
                    raise error
        self.rows = rows
    else:
        self.rows = []


# MATRIX INFORMATION
def columns(self):
    return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]


# 9. is_square() check if matrix is square
@property
def is_square(self):
    return self.order[0] == self.order[1]


# MATRIX MANIPULATION
def add_row(self, row, position=None):
    type_error = TypeError("Row must be a list containing all ints and/or floats")
    if not isinstance(row, list):
        raise type_error
    for value in row:
        if not isinstance(value, (int, float)):
            raise type_error
    if len(row) != self.num_columns:
        raise ValueError(
            "Row must be equal in length to the other rows in the matrix"
        )
    if position is None:
        self.rows.append(row)
    else:
        self.rows = self.rows[0:position] + [row] + self.rows[position:]


def add_column(self, column, position=None):
    type_error = TypeError(
        "Column must be a list containing all ints and/or floats"
    )
    if not isinstance(column, list):
        raise type_error
    for value in column:
        if not isinstance(value, (int, float)):
            raise type_error
    if len(column) != self.num_rows:
        raise ValueError(
            "Column must be equal in length to the other columns in the matrix"
        )
    if position is None:
        self.rows = [self.rows[i] + [column[i]] for i in range(self.num_rows)]
    else:
        self.rows = [
            self.rows[i][0:position] + [column[i]] + self.rows[i][position:]
            for i in range(self.num_rows)
        ]
