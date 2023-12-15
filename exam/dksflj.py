# kmadsftr = {"1": 1, "2": 2}
#
# print(**kmadsftr)
#
#
# which of the following descriptions refer to arguments packing (args) in python?:
# 1 breaking down a collection to its components
# 2 collecting arguments to a single variable (list)
# 3 collecting arguments to a single variable (dictionary)
# 3 collecting arguments to a single variable (tuple)

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, 4)