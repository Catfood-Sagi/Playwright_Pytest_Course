from utilis import utils

def test_root():
    root_25 = utils.root(25)
    assert root_25 == 5

    '''
    Hinting  a the type of the argument

    you can hint on boot the argument and the return type 
    to hint a type you can use the following syntax:
    variable_name: type
    or in a function definition:
    def function_name(arg_name: type) -> return_type:
    '''