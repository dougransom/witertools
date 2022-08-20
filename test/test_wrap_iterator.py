import itertools as i
import pytest as p
import witertools as l

sample_int_list = [-7,8,3,37,12]
def sample_int_iterator():
    return iter(sample_int_list)

def sample_kw_iterator(*args,**kwargs):
    #return an interator that untiples args, kwargs and appends them all together.
    return i.chain(iter(args),iter(kwargs.items()))

def test_list_iterator_to_list():

    #simple case - no arguments to the iterator
    assert l.iterator_to_list_function(sample_int_iterator)() == sample_int_list
    
def test_iter_with_argument_to_list():
    #case where iterator takes one argument
    fn=l.iterator_to_list_function(iter,sample_int_list)
    output_list = fn()
    assert output_list == sample_int_list


def test_iter_with_multiple_arguments_to_list():
    #case where iterator takes multiple arguments
    n=60  #number of arguments to pass
    fn=l.iterator_to_list_function(i.chain,(sample_int_list)*n)
    output_list=fn()
    assert output_list == sample_int_list*60

def test_iter_with_kwargs():
    fn=l.iterator_to_list_function(sample_kw_iterator,"dog","chicken",snacks="kibble", age=103)    
    output_list=fn()
    assert output_list[0:2]==["dog","chicken"]
    #order of kwargs will be undefined.
    assert ('age',103) in output_list
    assert ('snacks',"kibble") in output_list
