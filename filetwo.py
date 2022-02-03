from extraimport import lazyimport

fileone = lazyimport()
# from fileone import classone

def func_two():
    a = fileone.ClassOne()
    a.passed()

