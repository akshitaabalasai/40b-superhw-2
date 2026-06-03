def learn_theta(data, colors):
    best = None
    for i in range(len(data)):
        if colors[i] == 'blue':
            if best is None or data[i] > best:
                best = data[i]
    return best


def compute_ell(data, colors, theta):
    loss = 0
    for i in range(len(data)):
        if colors[i] == 'red' and data[i] <= theta:
            loss += 1
        elif colors[i] == 'blue' and data[i] > theta:
            loss += 1
    return float(loss)


def minimize_ell(data, colors):
    best_theta = None
    best_loss = None
    for i in range(len(data)):
        loss = compute_ell(data, colors, data[i])
        if best_loss is None or loss < best_loss:
            best_loss = loss
            best_theta = data[i]
    return float(best_theta)


def minimize_ell_sorted(data, colors):

    n = len(data)
    blue_gt_theta = sum(1 for c in colors if c == 'blue') - 1  # all blues except data[0]

    red_lte_theta = 0  

    best_theta = data[0]
    best_loss = blue_gt_theta 

    for alpha in range(1, n):
        if colors[alpha - 1] == 'red':
            red_lte_theta += 1
        else:
            blue_gt_theta -= 1

        loss = red_lte_theta + blue_gt_theta
        if loss < best_loss:
            best_loss = loss
            best_theta = data[alpha]

    return float(best_theta)
