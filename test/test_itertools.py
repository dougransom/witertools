import witertools.itertools as i
import pytest 
p=pytest
finite_iterators = [ 'accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'dropwhile', 'filterfalse', 
'groupby', 'islice', 'permutations', 'product',  'starmap', 'takewhile', 'tee', 'zip_longest']

infinite_iterators = ['count', 'cycle', 'repeat']
exluded_functions=infinite_iterators

#test we didn't accidently include functions that can not produce finite iterators.
@p.mark.parametrize("excluded_function",exluded_functions)
def test_load_nonexistant_package(excluded_function):
    assert not hasattr(i,excluded_function)

def test_chain():
    l=i.chain(iter([1,2]),iter([3,4]))
    assert l==[1,2,3,4]

#@p.mark.parametrize("included_function",finite_iterators)
#def test_included_functions(included_function):
#    assert  hasattr(i,included_function)

if __name__ == "__main__":
    pytest.main(['test_itertools.py'])