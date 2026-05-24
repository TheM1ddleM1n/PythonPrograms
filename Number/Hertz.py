def check_sample_rate(hz):
    if hz == 44100:
        print("CD Quality")
    elif hz < 44100:
        print("Low Quality")
    else:
        print("Studio Quality")


check_sample_rate(48000)
