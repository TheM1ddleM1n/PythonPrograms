"""Year group to Key Stage converter."""


def get_key_stage(year):
    """
    Determine UK Key Stage from year group.
    
    Args:
        year (int): Year group (1-11)
        
    Returns:
        None: Prints Key Stage information
    """
    if 1 <= year < 11:
        print("You are in Key Stage 1-3!")
    else:
        print("You are in Key Stage 4!")


# Main program
get_key_stage(11)
