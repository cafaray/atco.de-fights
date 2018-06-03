def whoseMove(lastPlayer, win):
    if win and lastPlayer=="black": return "black"
    if win and lastPlayer=="white": return "white"
    return "white" if lastPlayer == "black" else "black"