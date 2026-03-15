from Automata import Automata


"""
AUTOMATA 1: 
STRINGS WHERE 'a's ARE BEFORE 'b's
"""

automata_1: Automata = Automata(
	Q = ["q0", "q1", "q2"],
	
	sigma=["a", "b"],
	
	delta={
		("q0", "a"): "q0",
		("q0", "b"): "q1",
		("q1", "a"): "q2",
		("q1", "b"): "q1",
		("q2", "a"): "q2",
		("q2", "b"): "q2",
	},
	
	q0="q0",
	
	F=["q0", "q1"]
)

# automata_1.flood(4)


"""
AUTOMATA 2: 
todos os strings que começam com 1 e que quando interpretado como um inteiro binário é um múltiplo de 5
"""

automata_2: Automata = Automata(
	Q=["q_inicial", "q_morto",  # garantir que não começa com 0
	   "q0", "q1", "q2", "q3", "q4"],  # um estado para cada 'n mod 5 = k'

	sigma=["0", "1"],

	delta={
		("q_inicial", "0"): "q_morto",
		("q_inicial", "1"): "q1",

		("q_morto", "0"): "q_morto",
		("q_morto", "1"): "q_morto",

		("q0", "0"): "q0",
		("q0", "1"): "q1",

		("q1", "0"): "q2",
		("q1", "1"): "q3",

		("q2", "0"): "q4",
		("q2", "1"): "q0",

		("q3", "0"): "q1",
		("q3", "1"): "q2",

		("q4", "0"): "q3",
		("q4", "1"): "q4",
	},

	q0="q_inicial",

	F=["q0"]
)

automata_2.flood(5)
