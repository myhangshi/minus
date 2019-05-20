import functools
import string

@functools.total_ordering
class ReverseCompare(object):
    def __init__(self, obj):
        self.obj = obj
    def __eq__(self, other):
        return isinstance(other, ReverseCompare) and self.obj == other.obj
    def __le__(self, other):
        return isinstance(other, ReverseCompare) and self.obj >= other.obj
    def __str__(self):
        return str(self.obj)
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.obj)

import heapq
letters = 'axuebizjmf'

heap = list(map(ReverseCompare, letters))
print(heap)

heapq.heapify(heap)
print(heapq.heappop(heap)) # prints z

ll = 'axuebizjmf'
heapq.heapify(list(ll))
print(ll)
