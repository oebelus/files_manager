def get_extension(file):
    indexes = []
    count = 0
    for char in file:
        if '.' == char:
            indexes.append(count)
        count+=1
    return file[indexes[-1]:len(file)]