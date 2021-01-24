import path4gmns as pg
from time import time


if __name__=="__main__":
    network = pg.read_network()
    print('shortest path (external node sequence) from node 1 to node 2 is '
          +str(pg.find_shortest_path(network, 1, 2)))
    
    st = time()
    pg.find_path_for_agents(network)
    print('processing time of finding shortest paths for all agents:{0: .2f}'
          .format(time()-st)+ 's')

    agent_no = 300
    agent = network.agent_list[agent_no]
    print('orig node id of agent is '+str(agent.o_node_id))
    print('dest node id of agent is '+str(agent.d_node_id))
    print('shortest path (internal node sequence) of agent is ' 
          + str(agent.path_node_seq_no_list))
    print('shortest path (internal link sequence) of agent is ' 
          + str(agent.path_link_seq_no_list))

    pg.do_network_assignment(1, 1, 1, network)