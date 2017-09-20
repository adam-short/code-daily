from pprint import pprint
import sys
test = """@ START
> An army of zombies is approaching your house. What will you do?
- B - LEAVE FROM THE BACK DOOR - BACK_DOOR
- F - LEAVE FROM THE FRONT DOOR - FRONT_DOOR
- D - STAY AND DEFEND YOUR HOUSE - DEFEND

@ BACK_DOOR
> You exited your house from the back door. What will you do?
- R - GO RIGHT - RIGHT
- L - GO LEFT - LEFT

@ RIGHT
= DIE

@ LEFT
= DIE

@ FRONT_DOOR
> You exited your house through the front door, the zombies are everywhere!
= DIE

@ DEFEND
> How do you want to defend your home?
- K - USE A KNIFE - KNIFE
- S - USE A SHOTGUN - SHOTGUN

@ KNIFE
> The zombies are too many.
= DIE

@ SHOTGUN
> You take the shotgun.
= DIE

@ DIE
> You die."""

FUNCTIONS = {}

##### LINE PARSING
def parse_filestr(filestr):
    return filestr.split("\n\n")

def parse_function_block(block):
    components = block.split('\n')
    name = components[0][2:]
    print_statement = components[1][2:] if components[1][0] == ">" else None
    if len(components) > 2:
        execution = components[2][2:] if components[2][0] == "=" else None
    else:
        execution = components[1][2:] if components[1][0] == "=" else None

    if len(components) == 2:
        return name, print_statement, None, execution

    option_list_str = components[2:] if not execution else None
    if option_list_str:
        options_list = [create_option(s[2:]) for s in option_list_str]
        options = {s[0]: s[1] for s in options_list}
    else:
        options = None
    return name, print_statement, options, execution


def create_option(optionstr):
    components = optionstr.split(' - ')
    return components[0], tuple(components[1:])

def list_options(options):
    for letter, action_set in options.iteritems():
        print("[{}] : {}".format(letter, action_set[0]))

def execute(function_name):
    return FUNCTIONS[function_name]()

def execution_from_options(options, option_chosen):
    return FUNCTIONS[options[option_chosen][1]]

def build_function(print_statement, options, execution):
    def temp():
        if print_statement:
            print(print_statement)
        if options:
            list_options(options)
            return execution_from_options(options, raw_input(">  "))()
        if execution:
            return execute(execution)
        else:
            sys.exit()
    return temp

def assign_new_function(name, print_statement, options, execution):
    new_function = build_function(print_statement, options, execution)
    FUNCTIONS[name] = new_function


def run_engine(filestr):
    blocks = parse_filestr(filestr)
    function_blocks = []
    for b in blocks:
        print(b)
        function_blocks.append(parse_function_block(b))
        print("Processed.\n")
    for function in function_blocks:
        assign_new_function(*function)

    return FUNCTIONS


pprint(run_engine(test))

FUNCTIONS['START']()
