import utils
import networkx as nx

#loads the file and constructs snap and networkX graphs
fname_extended = './dataset/0222/1.txt'
fname = './dataset/0222/0.txt'
video_dict_list = utils.load_file(fname)
video_dict_list_extended = utils.load_file(fname_extended)
G_snap, dict_to_graph, graph_to_dict = utils.load_graph_undirected(video_dict_list)
fname = 'youtube_graph.txt'
G = utils.load_graph_networkX(fname)

#prints graph info and plots the Graph
# print('Graph info', nx.info(G))
print('Number of nodes', len(G.nodes))
print('Number of edges', len(G.edges))
print('Average degree', sum(dict(G.degree).values()) / len(G.nodes))
print('Graph clustering coefficient', nx.average_clustering(G))
utils.plot_graph_networkX(G, graph_to_dict, video_dict_list_extended)
