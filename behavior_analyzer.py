def detect_learning_mode(read_time, repeats, scroll_speed):

    # If student spends too long → confused
    if read_time > 30 and repeats > 1:
        return "visual"

    # If scrolling too fast → attention issue
    if scroll_speed > 100:
        return "adhd"

    # If student revisits multiple times → revision
    if repeats > 3:
        return "exam"

    # default
    return "dyslexia"