class Automata:

	Q: list[str]  # states
	sigma: list[str]  # alphabet
	delta: dict[(str, str), str]  # transition function
	q0: str  # initial state
	F: list[str]  # final states

	def __init__(
			self,
			Q: list[str],
			sigma: list[str],
			delta: dict[(str, str), str],
			q0: str,
			F: list[str]
	):
		self.Q = Q
		self.sigma = sigma
		self.delta = delta
		self.q0 = q0
		self.F = F

	def accepts(self, word: str) -> bool:
		"""
		check if instance recognizes word
		"""

		q = self.q0

		for symbol in word:
			assert symbol in self.sigma

			q = self.delta[(q, symbol)]

		return q in self.F

	def flood(self, n: int, visibility: bool = None) -> None:
		"""
		check every word with length<=n in alfabet*

		"""

		if visibility is None:
			for word in self.span_sigma(n):
				accepts = self.accepts(word)
				print(f"{accepts if accepts else "    "} {word}")

		if visibility is not None:
			for word in self.span_sigma(n):
				accepts = self.accepts(word)
				if accepts==visibility:
					print(f"{accepts} {word}")

	def span_sigma(self, n) -> list[str]:
		return self.span_sigma_aux([""], n)

	def span_sigma_aux(self, words: list[str], n: int) -> list[str]:
		if len(words[-1]) == n:
			return []

		new_words = [w+i for w in words for i in self.sigma]

		return new_words + self.span_sigma_aux(new_words, n)
