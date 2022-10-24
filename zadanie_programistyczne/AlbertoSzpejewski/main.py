from dijkstra import print_answer

if __name__ == "__main__":
    graph = {
        ("B", "D"): 2,
        ("D", "A"): 1,
        ("B", "A"): 4,
        ("A", "C"): 2,
        ("B", "E"): 3,
        ("C", "D"): 7,
        ("E", "C"): 3
    }

    print_answer("E", "D", graph)
