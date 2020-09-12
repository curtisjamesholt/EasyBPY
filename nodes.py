#region NODES
def set_material_use_nodes(matref, value):
    if value is True:
        matref.use_nodes = True
    else:
        matref.use_nodes = False


def get_node_tree(matref):
    matref.use_nodes = True
    return matref.node_tree.nodes


def create_node(nodes, nodetype):
    return nodes.new(type=nodetype)


def get_node_links(matref):
    return matref.node_tree.links


def create_node_link(matref, point1, point2):
    links = matref.node_tree.links
    return links.new(point1, point2)
#endregion
