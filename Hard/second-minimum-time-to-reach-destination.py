from collections import deque


class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        graph = {i: [] for i in range(1, n + 1)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # Priority queue of (node, time)
        dq = deque([(1, 0)])
        visited = [0] * (n + 1)
        dist = [0] * (n + 1)

        while dq:
            node, curr_time = dq.popleft()

            round_of_light = curr_time // change

            if round_of_light % 2 == 0:
                time_to_next = curr_time + time
            else:
                time_to_next = (round_of_light + 1) * change + time

            for nei in graph[node]:
                if visited[nei] < 2 and dist[nei] < time_to_next:
                    dist[nei] = time_to_next
                    visited[nei] += 1
                    dq.append((nei, time_to_next))

                    if nei == n and visited[nei] == 2:
                        return time_to_next

        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5),
        (2, [[1, 2]], 3, 2),
    ]
    for te in tests:
        res = sol.secondMinimum(*te)
        print(f"{te}: --> {res}")
