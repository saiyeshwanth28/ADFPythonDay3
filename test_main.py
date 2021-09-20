import pytest
from main import Task
from main import StringOperations

@pytest.mark.parametrize("input_file, result",[("text1",4),("file",25)])
def test_read_file(input_file, result):
    x=Task(input_file)
    x.read()
    assert len(x.words) == result

def test_palindrome():
    k=['mom']
    x=StringOperations('file')
    words=x.palindrome()
    assert len(words)==len(k)
def test_unique_list():
    k=len(['classes', 'a', 'quick', 'object', 'welcome', 'to', 'as', 'madam', 'all', 'programming', 'secure', 'objects', 'simple', 'is', 'adf', 'and', 'with', 'very', 'hi', 'python', 'mom', 'hello', 'oriented'])
    x=Task('file')
    y=StringOperations(x.read())
    l=len(y.unique_list())
    assert k==l
def test_counter_index():
    k=len({0: 'hi', 1: 'hello', 2: 'all', 3: 'welcome', 4: 'to', 5: 'adf', 6: 'madam', 7: 'as', 8: 'a', 9: 'mom', 10: 'python', 11: 'programming', 12: 'with', 13: 'simple', 14: 'classes', 15: 'and', 16: 'objects', 17: 'object', 18: 'oriented', 19: 'programming', 20: 'is', 21: 'very', 22: 'secure', 23: 'and', 24: 'quick'})
    x=StringOperations('file')
    l=x.counter_index()
    assert len(l)==len(k)
def test_max_repeated():
    s="programming"
    x=StringOperations('file')
    l=x.maximum_repeated()
    assert l==s
