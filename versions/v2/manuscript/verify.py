import argparse
import json
from math import gcd
from pathlib import Path

import sympy as sp


def branch_weights(order, loop):
    left = loop
    right = order - 1 - loop
    weights = [1] * (order - 1)
    if left and right:
        length = left if left % 2 == 0 else right
        start = 0 if left % 2 == 0 else left
        for edge in range(start, start + length):
            weights[edge] = length + 1
    return weights


def path_matrix(order, weights, diagonal):
    matrix = sp.zeros(order)
    for edge, weight in enumerate(weights):
        matrix[edge, edge + 1] = weight
        matrix[edge + 1, edge] = weight
    for vertex, value in enumerate(diagonal):
        matrix[vertex, vertex] = value
    return matrix


def commutator_rank(matrix):
    order = matrix.rows
    coordinates = [(row, column) for row in range(order)
                   for column in range(order) if matrix[row, column] == 0]
    constraint = sp.zeros(order * order, len(coordinates))
    for variable, (row, column) in enumerate(coordinates):
        for index in range(order):
            constraint[index * order + row, variable] += matrix[index, column]
            constraint[column * order + index, variable] -= matrix[row, index]
    rank = constraint.to_DM().rank()
    return rank, len(coordinates)


def allowing_witness(order, loops):
    loop = next(vertex for vertex in loops
                if order % 2 == 0 or vertex % 2 == 0)
    weights = branch_weights(order, loop)
    for exponent in range(65):
        denominator = 2 ** exponent
        scaled_weights = [denominator * weight for weight in weights]
        diagonal = [denominator if vertex == loop else int(vertex in loops)
                    for vertex in range(order)]
        matrix = path_matrix(order, scaled_weights, diagonal)
        rank, columns = commutator_rank(matrix)
        if rank == columns:
            expected = {(row, column) for row in range(order)
                        for column in range(order)
                        if abs(row - column) == 1
                        or row == column and row in loops}
            actual = {(row, column) for row in range(order)
                      for column in range(order) if matrix[row, column] != 0}
            assert expected == actual
            assert matrix == matrix.T
            assert all(value > 0 for value in matrix if value != 0)
            return {'order': order, 'loops': [vertex + 1 for vertex in loops],
                    'edge_weights': scaled_weights, 'diagonal': diagonal,
                    'complement_coordinates': columns, 'commutator_rank': rank,
                    'enlargement_exponent': exponent}
    raise AssertionError((order, loops, 'No full-rank witness in the bounded search'))


def obstruction_example(order, loops):
    matrix = path_matrix(order, [1] * (order - 1),
                         [int(vertex in loops) for vertex in range(order)])
    if not loops:
        test = sp.eye(order)
    else:
        odd = list(range(0, order, 2))
        even = list(range(1, order, 2))
        upper = matrix.extract(odd, even)
        lower = matrix.extract(even, odd)
        right = lower.nullspace()[0]
        left = upper.T.nullspace()[0]
        test = sp.zeros(order)
        for row_index, row in enumerate(odd):
            for column_index, column in enumerate(odd):
                test[row, column] = left[row_index] * right[column_index]
    assert test != sp.zeros(order)
    assert matrix.multiply_elementwise(test) == sp.zeros(order)
    assert matrix * test.T - test.T * matrix == sp.zeros(order)
    rank, columns = commutator_rank(matrix)
    assert rank < columns
    return {'order': order, 'loops': [vertex + 1 for vertex in loops],
            'commutator_rank': rank, 'complement_coordinates': columns,
            'nonzero_test_matrix': [[str(value) for value in test.row(row)]
                                    for row in range(order)]}


def continuants(parameters, directions, variable):
    values = [sp.Poly(1, variable), sp.Poly(variable, variable)]
    derivatives = [sp.Poly(0, variable), sp.Poly(0, variable)]
    for index, parameter in enumerate(parameters):
        values.append(values[-1] * variable - parameter * values[-2])
        derivatives.append(derivatives[-1] * variable
                           - directions[index] * values[-3]
                           - parameter * derivatives[-2])
    return values, derivatives


def differential_example(order, loop):
    variable = sp.Symbol('x')
    weights = branch_weights(order, loop)
    left_parameters = [weight ** 2 for weight in weights[:loop]]
    right_parameters = [weight ** 2 for weight in reversed(weights[loop:])]
    left_length = len(left_parameters)
    right_length = len(right_parameters)
    left, _ = continuants(left_parameters, [0] * left_length, variable)
    right, _ = continuants(right_parameters, [0] * right_length, variable)
    left_polynomial = left[left_length]
    right_polynomial = right[right_length]
    assert sp.gcd(left_polynomial, right_polynomial).degree() == 0
    joined = (left[left_length + 1] * right_polynomial
              + left_polynomial * right[right_length + 1]
              - (variable + 1) * left_polynomial * right_polynomial)
    diagonal = [int(vertex == loop) for vertex in range(order)]
    matrix = path_matrix(order, weights, diagonal)
    assert joined == sp.Poly(matrix.charpoly(variable).as_expr(), variable)
    columns = [-left_polynomial * right_polynomial]
    for edge in range(order - 1):
        left_direction = [int(index == edge) for index in range(left_length)]
        right_direction = [int(index == order - 2 - edge)
                           for index in range(right_length)]
        _, left_derivatives = continuants(left_parameters, left_direction, variable)
        _, right_derivatives = continuants(right_parameters, right_direction, variable)
        derivative = (left_derivatives[left_length + 1] * right_polynomial
                      + left[left_length + 1] * right_derivatives[right_length]
                      + left_derivatives[left_length] * right[right_length + 1]
                      + left_polynomial * right_derivatives[right_length + 1]
                      - (variable + 1) *
                      (left_derivatives[left_length] * right_polynomial
                       + left_polynomial * right_derivatives[right_length]))
        columns.append(derivative)
    jacobian = sp.Matrix(order, order, lambda row, column:
                         columns[column].nth(row))
    determinant = jacobian.det(method='domain-ge')
    assert determinant != 0
    return {'order': order, 'loop': loop + 1,
            'coefficient_differential_determinant': str(determinant),
            'rank': order, 'coprime_branches': True,
            'characteristic_identity': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('verification.json'))
    args = parser.parse_args()
    witnesses = []
    obstructions = []
    differentials = []
    unit_edges = []
    interior_failures = []
    for order in range(1, 9):
        for mask in range(2 ** order):
            loops = [vertex for vertex in range(order) if mask & (1 << vertex)]
            allowing = bool(loops) and (order % 2 == 0
                                       or any(vertex % 2 == 0 for vertex in loops))
            if allowing:
                witnesses.append(allowing_witness(order, loops))
            else:
                obstructions.append(obstruction_example(order, loops))
    for order in range(1, 11):
        for loop in range(order):
            if order % 2 == 0 or loop % 2 == 0:
                differentials.append(differential_example(order, loop))
    for order in range(1, 13):
        for loop in range(order):
            diagonal = [int(vertex == loop) for vertex in range(order)]
            matrix = path_matrix(order, [1] * (order - 1), diagonal)
            rank, columns = commutator_rank(matrix)
            divisor = gcd(loop + 1, order + 1)
            assert (rank == columns) == (divisor == 1)
            unit_edges.append({'order': order, 'loop': loop + 1,
                               'gcd': divisor, 'commutator_rank': rank,
                               'complement_coordinates': columns,
                               'has_nssp': rank == columns})
    for order in range(3, 13):
        endpoint_diagonal = [int(vertex in {0, order - 1})
                             for vertex in range(order)]
        endpoint = path_matrix(order, [1] * (order - 1), endpoint_diagonal)
        matrix = sp.eye(order) - endpoint
        test = sp.eye(order) - sp.ones(order) + endpoint
        assert test != sp.zeros(order)
        assert matrix.multiply_elementwise(test) == sp.zeros(order)
        assert matrix * test.T == test.T * matrix
        rank, columns = commutator_rank(matrix)
        assert rank < columns
        interior_failures.append({'order': order,
                                  'commutator_rank': rank,
                                  'complement_coordinates': columns,
                                  'nonzero_test_matrix': [[int(value) for value in test.row(row)]
                                                          for row in range(order)]})
    result = {
        'schema_version': 1,
        'arithmetic': 'Exact integer polynomial and rational linear algebra',
        'sympy_version': sp.__version__,
        'loop_set_orders': [1, 8],
        'loop_sets_checked': len(witnesses) + len(obstructions),
        'allowing_witnesses': len(witnesses),
        'obstruction_examples': len(obstructions),
        'differential_orders': [1, 10],
        'differentials_checked': len(differentials),
        'unit_edge_orders': [1, 12],
        'unit_edge_positions_checked': len(unit_edges),
        'interior_failure_orders': [3, 12],
        'interior_failures_checked': len(interior_failures),
        'all_checks_passed': True,
        'witnesses': witnesses,
        'obstructions': obstructions,
        'differentials': differentials,
        'unit_edges': unit_edges,
        'interior_failures': interior_failures,
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items()
                      if key not in {'witnesses', 'obstructions', 'differentials',
                                     'unit_edges', 'interior_failures'}},
                     indent=2))


if __name__ == '__main__':
    main()
