# Using variables and constants

# Subroutine to calculate flow rate of the heart
def FlowRate(Volume, Time):
    return Volume / Time


# Main program

Volume = 330

Time = 4

Heart = FlowRate(Volume, Time)

print("The flow rate of the human heart is", Heart, "ml/s")
