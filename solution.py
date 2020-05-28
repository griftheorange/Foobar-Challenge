import math

# find the sub-squares of an area
def solution1(area):
    square_array = []
    while(area > 0):
        for i in range(area, 0, -1):
            if area > 3:
                root = math.sqrt(i)
                if int(root + 0.5) ** 2 == i:
                    square_array.append(i)
                    area -= i
                    break
            elif area > 0:
                square_array.append(1)
                area -= 1
    return square_array
    

def solution2(xs):
    if(len(xs) == 1):
        return str(xs[0])
    
    pos_nums = []
    neg_nums = []
    exclusions = []
    max_neg_index = None

    # sort numbers into appropriate bins, tracks index of max negative value encountered
    for i in range(len(xs)):
        if(xs[i] > 0):
            pos_nums.append(xs[i])
        elif(xs[i] < 0):
            if(max_neg_index == None):
                max_neg_index = len(neg_nums)
            else:
                if(xs[i] > neg_nums[max_neg_index]):
                    max_neg_index = len(neg_nums)
            neg_nums.append(xs[i])
        else:
            exclusions.append(xs[i])
        
    # if no positive values and less than two negative values, handles edge cases
    if(len(pos_nums) == 0 and len(neg_nums) <= 1):
        if(len(neg_nums) == 0):
            return '0'
        else:
            if(len(exclusions) > 0):
                return '0'
            else:
                return str(neg_nums[0])

    # deletes max negative value if sign switch is needed
    if(len(neg_nums)%2 != 0):
        del neg_nums[max_neg_index]
    
    #second traversal calculates product
    product = 1
    for i in range(len(pos_nums)):
        product *= pos_nums[i]
    for i in range(len(neg_nums)):
        product *= neg_nums[i]
        

    return str(product)

def solution3(n, b):
    
    # support function for generating new minion id from existing id, calls sort_digits and str_base
    def get_new_id(n, base):
        vars = sort_digits(n)
        str_length = len(n)
        z = int(vars['x'], base) - int(vars['y'], base)
        base_converted_value = str_base(z, base)
        while(len(base_converted_value) < str_length):
            base_converted_value = '0'+base_converted_value
        return base_converted_value

    # support function for sorting the digits of an id and storing the values
    def sort_digits(string):
        int_arr = []
        for i in range(len(string)):
            int_arr.append(string[i])
        int_arr.sort()
        var_hash = {}
        var_hash['y'] = "".join(list(int_arr))
        var_hash['x'] = "".join(list(reversed(int_arr)))
        return var_hash

    # support function for converting numbers to strings in the provided base
    def str_base(number,base):
        if number < 0:
            return '-' + str_base(-number,base)
        else:
            (d,m) = divmod(number,base)
            if d:
                return str_base(d,base) + chr(ord('0') + m)
            else:
                return chr(ord('0') + m)
    
    id_arr = [n]
    # endlessly gets new minion id, reverses through list to find a previous number equal to new id, increments distance
    # if a match is found, loop broken and distance returned
    while True:
        n = get_new_id(n, b)
        id_arr.append(n)
        distance = 0
        for j in reversed(range(len(id_arr)-1)):
            distance += 1
            if(id_arr[j] == n):
                return distance
    
        


    

print(solution3('1211', 10))
print(solution3('210022', 3))

# print(solution2([2, 0, 2, 2, 0]))
# print(solution2([-2, -3, 4, -5]))
# print(solution2([2, -3, 1, 0, -5]))
# print(solution2([0]))
# print(solution2([-1]))
# print(solution2([-1, 1, 0]))
# print(solution2([-1, 1, 2, 0]))
# print(solution2([-1, 0]))
# print(solution2([-5, -5, -5, -5]))
# print(solution2([-5, -5, -5, -5, -5]))
# print(solution2([-5, -5, -5, -5, -5, -5]))
# print(solution2([0, 0, 0, 0, 0]))