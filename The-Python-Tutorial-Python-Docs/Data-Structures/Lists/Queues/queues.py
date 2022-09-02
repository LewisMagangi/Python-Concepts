from collections import deque

queue = deque(["Eric", "John", "Michael"])

print(queue.append("Terry"))           # Terry arrives
print(queue)
print(queue.append("Graham"))          # Graham arrives
print(queue)
print(queue.popleft())                 # The first to arrive now leaves
print(queue)
print(queue.popleft())                 # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrival
