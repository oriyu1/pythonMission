import os
import pytest
import numpy as np
import filecmp
from eostools.core.trajRW import read_traj, write_traj


from pkg_resources import resource_filename




@pytest.mark.ci
def test_read_traj():
    read_path_str= resource_filename("eostools.core", "tests/K_test.txt") 
    header, data = read_traj(read_path_str)
    assert header == ['t', 'x', 'y', 'z', 'h', 'p', 'r', '\n'], "header test failed"
    expected_data = ([[ 0.00000e+00,  0.00000e+00,  0.00000e+00,  5.00000e+00,
        -0.00000e+00,  1.40000e+00,  4.50000e+01],
       [ 1.00000e-02,  6.31964e-01, -4.80000e-05,  5.01500e+00,
         4.37600e-03,  1.40209e+00,  8.03964e+01],
       [ 2.00000e-02,  1.27704e+00, -9.70000e-05,  5.02934e+00,
         4.40300e-03,  1.40153e+00,  1.16069e+02]])
    assert np.alltrue(data == expected_data), "data test failed"


@pytest.mark.ci
def test_write_traj():
    tested_file = "tests/new_K_test.txt"
    header = ['t', 'x', 'y', 'z', 'h', 'p', 'r', '\n']
    data = ([[ 0.00000e+00,  0.00000e+00,  0.00000e+00,  5.00000e+00,
        -0.00000e+00,  1.40000e+00,  4.50000e+01],
       [ 1.00000e-02,  6.31964e-01, -4.80000e-05,  5.01500e+00,
         4.37600e-03,  1.40209e+00,  8.03964e+01],
       [ 2.00000e-02,  1.27704e+00, -9.70000e-05,  5.02934e+00,
         4.40300e-03,  1.40153e+00,  1.16069e+02]])
    write_traj(write_path_str, header, data)
    ref_file = "tests/K_test.txt"
    tested_file = "tests/new_K_test.txt"
    assert filecmp.cmp(ref_file, tested_file), "file write test failed"
