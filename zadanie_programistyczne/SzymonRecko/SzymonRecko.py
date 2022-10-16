import numpy as np
import warnings
warnings.filterwarnings("ignore")

def AntColony(data, n_ants=100, alpha=1, beta=1, iterations=100, evap=0.5):

    # mapping letters to indexes: 'A', 'B', 'C'... -> 0, 1, 2... 
    mapped_data = dict(zip(map(lambda x: ((ord(x[0])-65,ord(x[1])-65)),data),data.values()))

    # finding max index 
    max_V = max(max(mapped_data.keys(), key=lambda x:max(x[0],x[1])))+1

    # creating adjacency matrix
    weights = np.zeros((max_V, max_V))
    for i,j in mapped_data.keys():
        weights[i][j] = mapped_data[(i,j)]
        weights[j][i] = mapped_data[(i,j)]

    # creating attractivness matrix
    attractiveness = 1/weights
    attractiveness[attractiveness == np.inf] = 0

    # creating pheromone matrix
    pheromone = 0.1*np.ones_like(weights)

    # list of invalid routes
    invalid = set()

    # looping over diffrent start points
    for start in range(0,max_V):

        # creating routes matrix
        routes = np.zeros((n_ants,max_V))

        for iter in range(iterations):

            # initialize start point
            routes[:,0] = start
            
            for i in range(n_ants):
                
                temp_attractivness = np.array(attractiveness)

                for j in range(max_V-2):
                    combine_feature = np.zeros(max_V)
                    cum_prob = np.zeros(max_V)

                    # current location
                    cur_loc = int(routes[i,j])

                    # set current location as not available
                    temp_attractivness[:,cur_loc] = 0
                    
                    # calculating pheromone feature: τ^α
                    p_feature = np.power(pheromone[cur_loc,:],beta)

                    # calculating attractivness feature: η^β
                    a_feature = np.power(temp_attractivness[cur_loc,:],alpha)
                    
                    p_feature = p_feature[:,np.newaxis]
                    a_feature = a_feature[:,np.newaxis]

                    # calculating combined features: (τ^α)*(η^β)
                    combine_feature = np.multiply(p_feature,a_feature)

                    # check for invalid route
                    if sum(combine_feature)==0:
                        invalid.add(start)
                        break

                    # sum of combined features
                    total = np.sum(combine_feature)

                    # probability of going to each vertice
                    prob = combine_feature/total

                    # cummulative probability
                    cum_prob = np.cumsum(prob)
                    r = np.random.random_sample()

                    # finding next vertice having probability higher then r
                    next_V = np.nonzero(cum_prob>r)[0][0]
                         
                    
                    # adding vertice to routes 
                    routes[i,j+1] = next_V 

                # last untraversed vertice in routes
                last = list(set(range(0,max_V))-set(routes[i,:-1]))[0]
                routes[i,-1] = last

            # vector of routes costs
            dist_cost = np.zeros((n_ants,1))
            
            # calculating costs
            for i in range(n_ants):
                s = 0
                for j in range(max_V-1):
                    s = s + weights[int(routes[i,j]),int(routes[i,j+1])]

                dist_cost[i]=s

            dist_min_loc = np.argmin(dist_cost)
            dist_min_cost = dist_cost[dist_min_loc]
            best_route = routes[dist_min_loc,:]

            # evaporation
            pheromone = (1-evap)*pheromone    
                            
            # updating pheromone
            for i in range(n_ants):
                for j in range(max_V-1):
                    dt = 1/dist_cost[i]
                    pheromone[int(routes[i,j]),int(routes[i,j+1])] = pheromone[int(routes[i,j]),int(routes[i,j+1])] + dt   
        
        # mapping indexes to letters:  0, 1, 2... -> 'A', 'B', 'C'...
        def map_back(n):
            return chr(int(n)+65)
            
        if start not in invalid:
            print(f'Best path starting from {chr(start+65)}: {list(map(map_back,best_route))}')
            print(f'Cost of this path {int(dist_min_cost[0])}\n')

def main():
    data = {
    ("B", "D"): 2,
    ("D", "A"): 1,
    ("B", "A"): 4,
    ("A", "C"): 2,
    ("B", "E"): 3,
    ("C", "D"): 7,
    ("E", "C"): 3
    }

    # HYPERPARAMETERS
    # number of ants
    ants = 10
    # pheromone
    alpha = 1
    # attractivness
    beta = 1
    # iterations
    iters = 100
    # evaporation
    evap = 0.3

    AntColony(data, ants, alpha, beta, iters, evap)

if __name__ == "__main__":
    main()