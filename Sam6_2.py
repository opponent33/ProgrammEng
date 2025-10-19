def delete_elem(elem, *tuple):
    if elem not in tuple:
        return tuple
    temp_list = list(tuple)
    index_remove = temp_list.index(elem)
    temp_list.pop(index_remove)
    return temp_list

if __name__ == '__main__':
    print(delete_elem(5, (5, 3, 1,), 9))
