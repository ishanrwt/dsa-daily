self.k=k 
self.pk=[]
for num in nums:
    self.add(num)
def add(self,val:int)->int:
    if len(self.pk)<self.k or val>self.pk[0]:
        heapq.heappush[]