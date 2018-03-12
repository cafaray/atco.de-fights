def seatsInTheater(nCols, nRows, col, row):
    c = (nCols - col) + 1
    r = nRows - row
    return c * r