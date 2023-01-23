from programs.count import countFunc

def test_count_zeros():
	assert countFunc([0,0,0],0)==3

def test_count_string():
	assert countFunc(["a","a","a"],"a")==3

def test_count_minus():
	assert countFunc([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert countFunc([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2

#  Create __init__.py (empty) in both 
# programs and tests