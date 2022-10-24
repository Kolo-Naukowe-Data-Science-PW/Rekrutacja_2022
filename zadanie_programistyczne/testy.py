from skrypt import najkrotsza_sciezka

# przykladowy graf
G = {
  ("B", "D"): 2,
  ("D", "A"): 1,
  ("B", "A"): 4,
  ("A", "C"): 2,
  ("B", "E"): 3,
  ("C", "D"): 7,
  ("E", "C"): 3
} 
# przykladowe wywolanie funkcji
najkrotsza_sciezka(G, "D", "B")



