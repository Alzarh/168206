'''图'''
tu = {}
tu["yuepu"] = {}
tu["yuepu"]["chang"] = 5
tu["yuepu"]["haibao"] = 0
tu["chang"] = {}
tu["chang"]["jita"] = 15
tu["chang"]["jiazigu"] = 20
tu["haibao"] = {}
tu["haibao"]["jita"] = 30
tu["haibao"]["jiazigu"] = 35
tu["jita"] = {}
tu["jita"]["piano"] = 20
tu["jiazigu"] = {}
tu["jiazigu"]["piano"] = 10
tu["piano"] = {}

"""路长"""
infinity = float("inf")#定义infinity为无穷'''
lc = {}
lc["chang"] = 5
lc["haibao"] = 0
lc["jita"] = infinity
lc["jiazigu"] = infinity
lc["piano"] = infinity

"""前缀"""
qz = {}
qz['chang'] = 'yuepu' 
qz['haibao'] = 'yuepu'
qz['jita'] = None 
qz['jiazigu'] = None
qz['piano'] = None  

processed = []
lists = []
def find_lowest_cost_node(lc):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in lc:
		cost = lc[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

node = find_lowest_cost_node(lc)
while node is not None:
	cost = lc[node]
	neighbors =tu[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if lc[n] > new_cost:
			lc[n] = new_cost
			qz[n] =node
	processed.append(node)
	node = find_lowest_cost_node(lc)

for n,m in lc.items():
	print(n + " : " + str(m))
print("\n\n")

"""----------------------------------------------"""
print("换钢琴最好路劲：")
m = "piano"
while 1:
	if m is "yuepu":
		break
	else:
		lists.append(qz[m] + " -> ") 
		m = qz[m]
while len(lists):
	l = lists.pop()
	print(l)
print("piano ")
"""-----------------------------------------------"""
