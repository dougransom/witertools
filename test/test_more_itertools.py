import witertools.more_itertools as mi
#only limited testing for more_itertools as 
#itertools tests and the wrapping are tested.  
#just make sure at least one function is working

def test_single_function():
    #copied from https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.locate
    it_1 = range(3)
    it_2 = iter('abc')
    l=mi.zip_equal(it_1, it_2)
    assert l == [(0, 'a'), (1, 'b'), (2, 'c')]