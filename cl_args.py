import argparse

def command_line_args():
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS,
    description='''Welcome to the Text2Learn Data CLI. A command
    line interface for data entry, parsing and storage''')
    parser.add_argument('-t', '-type', nargs=1)
    # subparsers = parser.add_subparsers(help='sub-command help')
    #
    #
    #
    #
    #
    #
    #
    #
    # # Add subparsers for the 4 question types
    # parser_mc = subparsers.add_parser('mc')
    # parser_fib = subparsers.add_parser('fib')
    # parser_bool = subparsers.add_parser('bool')
    # parser_bc = subparsers.add_parser('bc')
    #
    # # Subparser for Multiple Choice
    # parser_mc.add_argument('question_type', action='store_const', const='mc')
    # parser_mc.add_argument("-nic", "--number_incorrect_choices", nargs='?', type=int, const=3)
    # # parser_mc.add_argument("-i", "--image", help='''Image Flag.  Default is False, when flagged for
    # # True you will automatically be prompted for image file entry''',
    # # default=False, action='store_true')
    # parser_mc.add_argument('-c', '--category')
    # # Subparser for Fill-In-Blank
    # parser_fib.add_argument('question_type', action='store_const', const='fib')
    # # parser_fib.add_argument("-i", "--image", help='''Image Flag.  Default is False, when flagged for
    # # True you will automatically be prompted for image file entry''',
    # # default=False, action='store_true')
    # parser_fib.add_argument('-c', '--category')
    # # Subparser for True or False
    # parser_bool.add_argument('question_type', action='store_const', const='bool')
    # # parser_bool.add_argument("-i", "--image", help='''Image Flag.  Default is False, when flagged for
    # # True you will automatically be prompted for image file entry''',
    # # default=False, action='store_true')
    # parser_bool.add_argument('-c', '--category')
    # # Subparser for Best Choices
    # parser_bc.add_argument('question_type', action='store_const', const='bc')
    # # parser_bc.add_argument("-i", "--image", help='''Image Flag.  Default is False, when flagged for
    # # True you will automatically be prompted for image file entry''',
    # # default=False, action='store_true')
    # parser_bc.add_argument('-c', '--category')
    # parser_bc.add_argument("-nic", "--number_incorrect_choices", nargs='?', type=int, const=3)
    # parser_bc.add_argument("-ncc", "--number_correct_choices", type=int)
    #
    # args = parser.parse_args()
    # return args

def command_line_args_parse(kwargs):
    kwargs = {key: value for key, value in kwargs.items() if value != None}
    return kwargs
