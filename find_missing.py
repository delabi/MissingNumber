def find_missing(list_a, list_b):
    
    if len(list_a) == len(list_b) == 0:
        return 0

    if not set(list_a).symmetric_difference(set(list_b)):
        return 0
    else:

        return list(set(list_a).symmetric_difference(set(list_b)))[0]

