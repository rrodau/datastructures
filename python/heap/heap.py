from random import randrange

class Heap:

    def __init__(self, heap_type=int) -> None:
        self.heap_list = []
        self.count = 0
        self.heap_type = heap_type

    def parent_idx(self, idx: int):
        """ 
        A function that returns the parent index of an element

        @params:
            idx -> Index of element which parent needs to be found 

        @return:
            the index of the elements parent
        """
        return idx // 2

    def left_child_idx(self, idx: int) -> int:
        """
        A function that returns the left child index of an element

        @params:
            idx -> Index of element which left child needs to be found

        @return:
            the index of the elements left child
        """
        return idx * 2 + 1

    def right_child_idx(self, idx: int) -> int:
        """
        A function that returns the right child index of an element

        @params:
            idx -> Index of element which right child needs to be found

        @return:
            the index of the elements right child
        """
        return idx * 2 + 2
    
    def add(self, element) -> None:
        """
        A function that add an element to the heap

        @params:
            element -> An element of the heap_type that needs to be added to the heap
        
        @return:
            None
        """
        if isinstance(element, self.heap_type):
            self.count += 1
            print(f"Adding {element} to {self.heap_list}")
            self.heap_list.append(element)
            self.heapify()
        else:
            raise ValueError(f"Expected {self.heap_type} but got {type(element)}")

    def heapify(self) -> None:
        """
        A function that restores the heap property that the children are smaller than the parent
        """ 
        # start at the last element of the list
        idx = self.count - 1
        # while there's a parent element available
        while self.parent_idx(idx) >= 0:
            child = self.heap_list[idx]
            parent_idx = self.parent_idx(idx)
            parent = self.heap_list[parent_idx]
            # check if parent is smaller than child if so, swap them
            if parent < child:
                print(f"swapping {parent} with {child}")
                self.heap_list[parent_idx] = child
            if parent_idx == 0:
                break
            idx = parent_idx
        print("HEAP RESTORED!")



# make an instance of MaxHeap
heap = Heap()

# populate max_heap with random numbers
random_nums = [randrange(1, 101) for _ in range(6)]
for el in random_nums:
  heap.add(el)


# test it out, is the maximum number at index 1?
print(heap.heap_list)