def find(search_list, value):
    sorted_list = sorted(search_list)
    while sorted_list:
        middle_index = len(sorted_list) // 2
        middle_element = sorted_list[middle_index]
        
        if middle_element == value:
            return search_list.index(value)
        elif value < middle_element:
            del sorted_list[middle_index:]
        else:
            del sorted_list[:middle_index + 1]
    raise ValueError("value not in array")