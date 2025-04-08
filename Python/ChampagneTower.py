def champagneTower(poured, query_row, query_glass):
    glasses = [[0] * k for k in range(1, 102)]  # initialize the glasses with 0 champagne
    glasses[0][0] = poured  # pour the champagne into the top glass

    # simulate the pouring process
    for i in range(query_row + 1):
        for j in range(i + 1):
            # if the current glass has more than 1 unit of champagne
            if glasses[i][j] > 1:
                # pour the excess champagne equally to the glasses below
                overflow = (glasses[i][j] - 1) / 2.0
                glasses[i+1][j] += overflow
                glasses[i+1][j+1] += overflow
                glasses[i][j] = 1

    return glasses[query_row][query_glass]
