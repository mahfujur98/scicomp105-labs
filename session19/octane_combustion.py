#!/usr/bin/env python3
# octane_combustion.py


import pulp


def init_prob(terms):
    # The goal is to minimize total atom count (POAC)
    # https://www.quantumstudy.com/chemistry/stoichiometry
    prob = pulp.LpProblem(sense=pulp.LpMinimize)

    # Create decision variables (terms in chemical equation, +1 if ionic)
    # Each term coefficient must ultimately be an integer > 1
    x0, x1, x2, x3, x4, x5 = ((None),) * 6
    if terms >= 4:
        x0 = pulp.LpVariable(name='x0', lowBound=1, cat='Integer')
        x1 = pulp.LpVariable(name='x1', lowBound=1, cat='Integer')
        x2 = pulp.LpVariable(name='x2', lowBound=1, cat='Integer')
        x3 = pulp.LpVariable(name='x3', lowBound=1, cat='Integer')
    if terms >= 5:
        x4 = pulp.LpVariable(name='x4', lowBound=1, cat='Integer')
    if terms >= 6:
        x5 = pulp.LpVariable(name='x5', lowBound=1, cat='Integer')

    # Define objective function based upon number of terms
    if terms == 4:
        prob += x0 + x1 + x2 + x3
        return prob, x0, x1, x2, x3
    elif terms == 5:
        prob += x0 + x1 + x2 + x3 + x4
        return prob, x0, x1, x2, x3, x4
    elif terms == 6:
        prob += x0 + x1 + x2 + x3 + x4 + x5
        return prob, x0, x1, x2, x3, x4, x5


def solve_prob(prob, *x):
    # Use PuLP's default COIN "Branch and Cut solver" (CBC) MIP solver
    # COIN-OR = Computational Infrastructure for Operations Research
    # https://www.coin-or.org
    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

    # Display if solution found is optimal, feasible, or infeasible
    print(pulp.LpStatus[status])

    # Display the final value of the decision variables
    if len(x[0]) >= 4:
        print(f"x0 = {int(pulp.value(x[0][0]))}")
        print(f"x1 = {int(pulp.value(x[0][1]))}")
        print(f"x2 = {int(pulp.value(x[0][2]))}")
        print(f"x3 = {int(pulp.value(x[0][3]))}")
    if len(x[0]) >= 5:
        print(f"x4 = {int(pulp.value(x[0][4]))}")
    if len(x[0]) >= 6:
        print(f"x5 = {int(pulp.value(x[0][5]))}")


def octane_combustion():
    prob, *x = init_prob(terms=4)

    # TODO: Edit these three constraint equations
    prob += x[0] == x[0]                            # Carbon (C)
    prob += x[1] == x[1]                            # Hydrogen (H)
    prob += x[2] == x[2]                            # Oxygen (O)

    solve_prob(prob, x)


def main():
    octane_combustion()
    return


if __name__ == "__main__":
    main()
