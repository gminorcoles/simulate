# -*- coding: utf-8 -*-
### Portfolio Optiimization
# Finds an optimal allocation of stocks in a portfolio,
# satisfying a minimum expected return.
# The problem is posed as a Quadratic Program, and solved
# using the cvxopt library.
# Uses actual past stock data, obtained using the stocks module.

from cvxopt import matrix, solvers, spmatrix, sparse
import numpy
import pandas as pd
import numpy as np
from datetime import datetime

solvers.options['show_progress'] = False
# solves the QP, where x is the allocation of the portfolio:
# minimize   x'Px + q'x
# subject to Gx <= h
#            Ax == b
#
# Input:  n       - # of assets
#         avg_ret - nx1 matrix of average returns
#         covs    - nxn matrix of return covariance
#         r_min   - the minimum expected return that you'd
#                   like to achieve
# Output: sol - cvxopt solution object
""" 模拟输入信息 """
dates = pd.date_range('2000-01-01', periods=6)
industry = ['industry', 'industry', 'utility', 'utility', 'consumer']
symbols = ['A', 'B', 'C', 'D', 'E']
zipped = list(zip(industry, symbols))
index = pd.MultiIndex.from_tuples(zipped)

noa = len(symbols)

data = np.array([[10, 11, 12, 13, 14, 10],
                 [10, 11, 10, 13, 14, 9],
                 [10, 10, 12, 13, 9, 11],
                 [10, 11, 12, 13, 14, 8],
                 [10, 9, 12, 13, 14, 9]])

market_to_market_price = pd.DataFrame(data.T, index=dates, columns=index)
rets = market_to_market_price / market_to_market_price.shift(1) - 1.0
rets = rets.dropna(axis=0, how='all')

# covariance of asset returns
covs    = matrix(rets.cov().values)

# average yearly return for each stock
rets_mean = rets.mean()
avg_ret = matrix(rets_mean.values)
n = len(symbols)


def statistics(weights):
    ''' Return portfolio statistics.

    Parameters
    ----------
    weights : array-like
        weights for different securities in portfolio

    Returns
    -------
    pret : float
        expected portfolio return
    pvol : float
        expected portfolio volatility
    prisk : float
        expected portfolio total risk
    pret / pvol : float
        Sharpe ratio for rf=0
    '''
    weights = np.array(weights)
    pret = np.dot(weights.T, rets_mean)
    pvol = np.sqrt(np.dot(weights.T, np.dot(covs, weights)))
    # prisk = calculate_total_risk(weights, cov_matrix_V)

    return np.array([pret, pvol, pret / pvol])


def minimum_risk_subject_to_target_return():

    # minimum expected return threshold
    r_min = 0.04

    P = covs
    q = matrix(numpy.zeros((n, 1)), tc='d')
    # inequality constraints Gx <= h
    # captures the constraints (avg_ret'x >= r_min) and (x >= 0)
    G = matrix(-numpy.transpose(numpy.array(avg_ret)))
    h = matrix(-numpy.ones((1,1))*r_min)

    # equality constraint Ax = b; captures the constraint sum(x) == 1
    A = matrix(1.0, (1,n))
    b = matrix(1.0)

    groups = rets.groupby(axis=1, level=0, sort=False, group_keys=False).count().ix[-1].values
    num_group = len(groups)
    num_asset = numpy.sum(groups)
    G_sparse_list = []
    for i in range(num_group):
        for j in range(groups[i]):
            G_sparse_list.append(i)
    Group_sub = spmatrix(1.0, G_sparse_list, range(num_asset))
    asset_sub = matrix(np.eye(n))
    G = matrix(sparse([G, asset_sub, -asset_sub, Group_sub, -Group_sub]))

    b_asset = tuple((0.01, 1.0) for i in rets.columns)
    b_asset_upper_bound = np.array([x[-1] for x in b_asset])
    b_asset_lower_bound = np.array([x[0] for x in b_asset])
    b_asset_matrix = matrix(numpy.concatenate((b_asset_upper_bound,
                                               -b_asset_lower_bound), 0))
    b_group = [(.05,.41), (.2,.66), (0.01,.16)]
    b_group_upper_bound = np.array([x[-1] for x in b_group])
    b_group_lower_bound = np.array([x[0] for x in b_group])
    b_group_matrix = matrix(numpy.concatenate((b_group_upper_bound,
                                               -b_group_lower_bound), 0))
    h = matrix(sparse([h, b_asset_matrix, b_group_matrix]))

    # solve minimum risk for maximum return above target .
    sol = solvers.qp(P, q, G, h, A, b)

    print(minimum_risk_subject_to_target_return.__name__)
    print(sol['x'])
    print(statistics(sol['x']))


#def maximum_return_subject_to_target_risk():

def maximum_return():

    P = matrix(np.zeros((n, n)))
    q = -avg_ret
    G = matrix(-np.eye(n))
    h = matrix(-numpy.zeros((n,1)))

    # equality constraint Ax = b; captures the constraint sum(x) == 1
    A = matrix(1.0, (1,n))
    b = matrix(1.0)

    sol = solvers.qp(P, q, G, h, A, b)

    print(maximum_return.__name__)
    print(sol['x'])
    print(statistics(sol['x']))


def minimum_risk():

    P = covs
    q = matrix(numpy.zeros((n, 1)), tc='d')
    G = matrix(-np.eye(n))
    h = matrix(-numpy.zeros((n,1)))

    # equality constraint Ax = b; captures the constraint sum(x) == 1
    A = matrix(1.0, (1,n))
    b = matrix(1.0)

    sol = solvers.qp(P, q, G, h, A, b)

    print(minimum_risk.__name__)
    print(sol['x'])
    print(statistics(sol['x']))


# solve for maximum return and under control risk.



#minimum_risk_subject_to_target_return()
maximum_return()
minimum_risk()
