def format_names(names):
    if len(names) == 0:
        return ""
    
    if len(names) == 1:
        return names[0]

    string = names[0]
    for name in names[1:-1]:
        string += ", " + name
    
    string += " & " + names[-1]

    return string
    