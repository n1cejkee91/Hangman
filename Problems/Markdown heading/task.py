def heading(word, mark=None):
    if mark == None:
        return "# " + word
    elif mark == 2:
        return "## " + word
    elif mark == 3:
        return "### " + word
    elif mark == 4:
        return "#### " + word
    elif mark == 5:
        return "##### " + word
    elif mark >= 6:
        return "###### " + word
    else:
        return "# " + word
