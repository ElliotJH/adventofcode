import taxicab

def test_taxicab_1():
    """Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away."""
    assert taxicab.process_sequence('R2, L3') == 5

def test_taxicab_2():
    """
    R2, R2, R2 leaves you 2 blocks due South of your starting position, 
    which is 2 blocks away.
    """
    assert taxicab.process_sequence('R2, R2, R2') == 2

def test_taxicab_3():
    """R5, L5, R5, R3 leaves you 12 blocks away."""
    assert taxicab.process_sequence('R5, L5, R5, R3') == 12
