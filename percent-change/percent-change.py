def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    N = len(series)

    percent_change = []

    for i in range(1, N):
        if series[i - 1] == 0:
            percent_change.append(0.0)
        else:
            pc = (series[i] - series[i - 1]) / series[i - 1]
            percent_change.append(pc)

    return percent_change
    