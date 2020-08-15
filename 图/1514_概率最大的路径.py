'''
此为Leetcode197场周赛题，详细解析可见
https://zhuanlan.zhihu.com/p/163316436
'''
from typing import List
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        pro = [0] * n
        pro[start] = 1
        adj = [[] for _ in range(n)]
        for i,e in enumerate(edges):
            adj[e[0]].append([e[1],succProb[i]])
            adj[e[1]].append([e[0],succProb[i]])
        queue = [(-1,start)]
        s = set()
        while queue:
            p, index = heapq.heappop(queue)
            if index == end:
                return -p
            if index in s:
                continue
            s.add(index)
            for e, prob in adj[index]:
                if e not in s:
                    heapq.heappush(queue,(min(p * prob, -pro[e]), e))
                    pro[e] = max(-p * prob, pro[e])
            #print(queue)
        return pro[end]
        '''
        以下为未使用优先队列的代码，未超时
        '''
        queue = [start]
        s = set()
        while queue:
            m = 0
            pos = -1
            for e in queue:
                if pro[e] > m:
                    m = pro[e]
                    pos = e
            if pos == end:
                return pro[pos]
            s.add(pos)
            queue.remove(pos)
            for e in adj[pos]:
                if e[0] not in s:
                    pro[e[0]] = max(pro[e[0]],pro[pos]*e[1])
                    if e[0] not in queue:
                        queue.append(e[0])  
        return pro[end]
        '''
