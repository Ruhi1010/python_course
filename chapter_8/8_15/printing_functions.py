def print_models(unprinted, completed):
    while unprinted:
        model = unprinted.pop()
        print("Printing:", model)
        completed.append(model)

