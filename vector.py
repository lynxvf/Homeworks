def is_valid_length(function):
    def wrapper(self, other):
        if len(self.vector) == len(other.vector):
            return function(self, other)
        else:
            raise TypeError("Unsupported operands error - Vectors must be the same dimension")
    return wrapper


class Vector:
    def __init__(self, *args):
        self.vector = list(*args)

    @is_valid_length
    def __add__(self, other):
        vector_sum_result = []
        for i in zip(self.vector, other.vector):
            vector_sum_result.append(sum(i))
        return vector_sum_result

    @is_valid_length
    def __sub__(self, other):
        vector_sub_result = []
        for i in zip(self.vector, other.vector):
            vector_sub_result.append(i[0] - i[1])
        return vector_sub_result
    
    @is_valid_length
    def __matmul__(self, other):
        vector_matmul_result = 0
        for coordinate in zip(self.vector, other.vector):
            vector_matmul_result += coordinate[0] * coordinate[1]
        return vector_matmul_result


    def __mul__(self, other):
        vector_multiple_result = []
        if isinstance(other, int):
            for coordinate in self.vector:
                vector_multiple_result.append(coordinate * other)
        else:
            self_vector = self.vector
            other_vector = other.vector
            if len(self_vector) == 3 and len(other_vector) == 3:
                vector_multiple_result = [
                    self_vector[1] * other_vector[2] - self_vector[2] * other_vector[1],
                    self_vector[0] * other_vector[2] - self_vector[2] * other_vector[0],
                    self_vector[0] * other_vector[1] - self_vector[1] * other_vector[0],
                ]
        return vector_multiple_result


if __name__ == "__main__":
    first_vector = Vector([1, 2, 5])
    second_vector = Vector([9, 2, 4])

    add_res = first_vector + second_vector
    sub_res = first_vector - second_vector
    scalar_mul_res = first_vector @ second_vector
    vector_mul_res = first_vector * second_vector
    number_for_mul = 3
    mul_on_scalar_res = first_vector * number_for_mul

    print("vector add result: ", add_res)
    print("vector sub result: ", sub_res)
    print("scalar mul result: ", scalar_mul_res)
    print("vector mul result: ", vector_mul_res)
    print("vector on scalar mul result: ", mul_on_scalar_res)

