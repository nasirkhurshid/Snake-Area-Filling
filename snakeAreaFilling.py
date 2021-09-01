'''
Created on Sep 1, 2021
@author: Nasir Khurshid
All rights reserved.
'''

def snakeFill(n):
    area = n*n
    size = 1
    count = 0
    while True:
        if size > area:
            return count-1
        size += size
        count += 1
    
area = 24
print("How many times can snake move? : ", snakeFill(area))
        
        
