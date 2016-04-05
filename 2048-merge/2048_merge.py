"""
Merge function for 2048 game.
first half of building 2048 game

"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line_length = len(line)
    merge_line_result = []
    zero_list_holder = []

    for count in line:
        if count != 0:
            merge_line_result.append(count)        
        else:
            zero_list_holder.append(count)
            
    merge_line_result.extend(zero_list_holder)

        
    for index in range(line_length-1):
        if merge_line_result[index] == merge_line_result[index+1]:
            merge_line_result[index] = merge_line_result[index] * 2
            merge_line_result.pop(index+1)
            merge_line_result.append(0)
    return merge_line_result   