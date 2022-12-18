import math
import statistics
class Statistics():
    def __init__(self):
        self.array==[]
    def array(self,array):
        self.array=array
    def show_array(self):
        print(self.array)
    def greatest(self):
        self.greatest=max(self.array)
        print(self.greatest)
    def smallest(self):
        self.smallest=min(self.array)
        print(self.smallest)
    def arithmetic_mean(self):
        self.arithmetic_mean=sum(self.array)/len(self.array)
        print(self.arithmetic_mean)
    def median(self):
        self.median=statistics.median(self.array)
        print(self.median)
list1=Statistics()
list1.array([12, 37, 6, 9, 17])
list1.show_array()
list1.greatest()
list1.smallest()
list1.arithmetic_mean()
list1.median()