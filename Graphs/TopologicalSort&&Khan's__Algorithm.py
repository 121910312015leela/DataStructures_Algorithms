
# question reference --- 210. Course Schedule II (Leet Code)
'''

Kahn's algorithm works by deleting nodes as you go and keeping track of how many incoming edges each vertex has. When a vertex reaches 0 incoming edges, add it to 
the queue and continue processing until the queue is empty. Start with the vertices with no incoming edges in a queue and keep a list of vertices and the total number 
of incoming edges. While the queue is not empty, pop an element off of it that contains a vertex with no edges, each time decrementing the "degree" of each neighboring 
vertex by 1. If any of those neighbors reach a degree of 0 (meaning after removal, they have no incoming edges), add it to the queue.
If at the end of the loop, the size of the topological ordered list is not equal to the total number of courses, it means there is a cycle or a course is not listed 
in the prerequisites list.
Both algorithms take O(V + E) time and O(V + E) space, where V = # of vertices and E = # of edges. Kahn's performs better in leetcode (>90% time) vs DFS (>50% time) 
but it's the same big O time complexity.

Kahn's Algorithm

https://www.youtube.com/watch?v=cIBFEhD77b4
'''

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Kahn's algorithm"""
        courses = defaultdict(list)
        indegree = defaultdict(int) # could also use collections.Counter here
        for course, prereq in prerequisites:
            courses[prereq].append(course)
            indegree[course] += 1

        q = deque(i for i in range(numCourses) if i not in indegree)
        
        order, visited = [], set()
        
        # queue will store vertices with no incoming edges
        while q:
            course = q.popleft()
            order.append(course)
            visited.add(course)
            
            for next_course in courses[course]:
                if next_course in indegree:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0 and next_course not in visited:
                        q.append(next_course)
                        
		# check if there is a cycle or a course is not listed
       return order if len(order) == numCourses else []

''' 
The DFS solution is the traditional topological sort algorithm using recursion. It's important to check for cycles by keeping track of what is currently being visited.
If at any point during the callstack, we are visiting a node that has already been visited, that means there is a cycle and the DAG is invalid for topological sorting.
DFS
'''

from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        order = []
        
        def dfs(course: int, visited: List[int], order: List[int]) -> bool:
            if visited[course] == -1:
                return False
            elif visited[course] == 1:
                return True
            
            # visiting
            visited[course] = -1
            for next_course in courses[course]:
                if not dfs(next_course, visited, order):
                    return False
                
            # visited
            visited[course] = 1
            order.append(course)
            
            return True
        
        for course, prereq in prerequisites:
            courses[prereq].append(course)
            
        return order[::-1] if all(dfs(course, visited, order) for course in range(numCourses)) else []
