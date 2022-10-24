from data_structures import Graph
from search_algorithm import convert_txt_to_graph_dict, create_solution

if __name__ == '__main__':

    # DATA DIRECTLY FROM DICT
    graph_dict = {('a', 'b'): 7,
                  ('a', 'd'): 13,
                  ('d', 'b'): 8,
                  ('d', 'f'): 7,
                  ('b', 'f'): 4}

    create_solution(initial='a', final='f', data_source=graph_dict)

    # DATA INDIRECTLY FROM TXT FILE

    create_solution(initial='a', final='f', data_source='data/data.txt')

    create_solution(initial='a', final='d', data_source='data/data.txt')

    create_solution(initial='e', final='b', data_source='data/data.txt')


