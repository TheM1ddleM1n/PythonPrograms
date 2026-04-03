def check_sample_rate(hz):
    """
    Determine audio quality from sample rate frequency.
    Args:
        hz (int): Sample rate in Hz
    Returns:
        None: Prints quality assessment
    """
    if hz == 44100:
        print("CD Quality")
    elif hz < 44100:
        print("Low Quality")
    else:
        print("Compressed Quality")
        
check_sample_rate(48000)
