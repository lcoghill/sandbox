from ete2 import Tree
import networkx as nx


def build_edges(G, t, node):
    children_list = []
    if node.is_root():
	children_list = node.get_children()
	## create edges between root and children
    elif node.is_leaf():
        print "%s is leaf." % node
    else:
        path_list = [] 
        children_list = node.get_children()
        for child in children_list:
            temp_list = []
            temp_list.append(node.name)
            temp_list.append(child.name)
	    path_list.append(temp_list)
	## create edges here with list
        G.add_edges_from(path_list)
                    


print "Loading taxonomy newick..."
t = Tree("ncbi_taxonomy.newick", format=8)
print "Complete."

G=nx.Graph()
node_list = []
print "Building node name list..."
for node in t.traverse():
    if node.name == 'NoName':
        node_list.append('Root')
    else:
        node_list.append(node.name)
print "Complete."
print "Building graph nodes..."
for n in node_list:
    G.add_node(n)
print "Complete."
print "Building graph edges..."
for node in t.traverse():
	build_edges(G, t, node)


print "Complete."
print "Number of nodes: %s" % G.number_of_nodes()
print "Number of edges: %s" % G.number_of_edges()

print "Writing to GraphML file..."
nx.write_graphml(G, "ncbi.gml")
print "Complete."
