# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        not_celebrity = set()
        person = 0
        while(person < n):
            other = (person + 1) % n
            while(person != other and person not in not_celebrity):  
                if know(person, other):
                    not_celebrity.add(person)
                    break
                not_celebrity.add(other)
                other += 1
                other %= n
            if other==
