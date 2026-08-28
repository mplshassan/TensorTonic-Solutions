def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    target_mean = {}
    count = {}
    encoded = []

    for i, category in enumerate(categories):
        if category in target_mean:
            target_mean[category] += targets[i]
            count[category] += 1
        else:
            target_mean[category] = targets[i]
            count[category] = 1

    for category in target_mean:
        target_mean[category] = target_mean[category] / count[category]

    for category in categories:
        encoded.append(target_mean[category])

    return encoded