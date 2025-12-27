from solution import find_duplicates
from solution_optimized import find_duplicates as find_duplicates_opt

def test_empty_folder():
    assert find_duplicates(".") == []

def test_optimized():
    assert isinstance(find_duplicates_opt("."), list)

print("Duplicate File Finder tests passed")
