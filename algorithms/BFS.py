def bfs(s,adj):
	level = {s:0}
	parent = {s:None}
	i = 1
	frontier = [s]
	while(frontier):
		next = []
		for u in frontier:
			for v in adj[u]:
				if v not in level:
					level[v] = i
					parent[v] = u
					next.append(v)
		frontier = next
		i += 1
	print(level)
	print(parent)
if __name__ == '__main__':
	adj = {1:[2,3],2:[1],3:[1,4],4:[3]}
	bfs(1,adj)