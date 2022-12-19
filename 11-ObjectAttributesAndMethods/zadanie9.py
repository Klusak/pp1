class Arrays():
    @staticmethod
    def create_array(number_of_array_elements, value_of_array_elements):
        lista=[]
        for i in range(number_of_array_elements):
            lista.append(value_of_array_elements)
        return lista
    @staticmethod
    def create_array_with_random(number_of_array_elements, value_from, value_to):
        lista=[]
        import random
        for i in range(number_of_array_elements):
            lista.append(random.randint(value_from,value_to))
        return lista
    
arr1=Arrays.create_array(10,4)
print(arr1)