class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)):
            if i == len(triangle) - 1:
                return min(triangle[i])
            triangle[i + 1] = self.shortest_path_conversion(triangle[i],
                    triangle[i + 1])

    
    def shortest_path_conversion(parent, child):
        parent_len = len(parent)
        converted_array = []
        for i in range(parent_len):
            parent_node = parent[i]
            left_node = child[i]
            right_node = child[i + 1]

            if not converted_array:
                converted_array.append(left_node + parent_node)
            else:
                converted_array[i] = min(converted_array[i], parent_node +
                        left_node)
            converted_array.append(right_node + parent_node)

        return converted_array

        

