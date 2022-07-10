class Array():
    
    def __init__(self, size, dtype):
        self.size = size
        self.dtype = dtype
        self.last_ind = 0

        self.arr = [None] * self.size
    
            
    def __shift_right__(self, start_index):
        for i in range(self.size - 1, start_index, -1):
            if self.arr[i] == None:
                pass
            else:
                self.arr[i - 1] = self.arr[i]

    def __isfull__(self):
        return self.last_ind == self.size
    
    def insert(self, val, index):
        assert isinstance(val, self.dtype)
        
        if self.last_ind == self.size:
            print("The array is full.")
            return
        
        self.__shift_right__(index)
        self.arr[index] = val
        self.last_ind += 1

    # class Vector:

    #     def __init__(self, x, y, z) -> None:
    #         a = Array(3, int)
    #         a.insert(x ,0)
    #         a.insert(y, 1)
    #         a.insert(z, 2)
    #         self.vec = a.arr

    #     def 
            
            


numbers_arr = Array(6, int)
print(numbers_arr.arr)
print(len(numbers_arr.arr))
numbers_arr.insert(1, 0)
numbers_arr.insert(2, 1)
numbers_arr.insert(3, 5)
numbers_arr.insert(4, 3)
numbers_arr.insert(2, 4)
numbers_arr.insert(6, 4)
print(numbers_arr.arr)
