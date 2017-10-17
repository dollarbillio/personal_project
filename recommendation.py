# Using Euclidean Distance Score
# Theory: compare 2 people one at a time, using axes. How many axes depends on 
	# how many movies they've all seen. Each person will be represented by a dot in the n-dimension
		# corresponding to their scores on each movie. People whose' dots are near(Euclidean distance) 
			# are likely to have same taste

# Code:
from math import sqrt

def similar_taste (prefs, person_1, person_2):
	"""Return a score btw 0 and 1. Higher = more similar"""
	
	# check how many movies they've seen together
	similar_movie = {}
	for movie in prefs[person_1]:
		if movie in prefs[person_2]:
			similar_movie[movie] = 1
	
	# there is no movie, return 0
	if len(similar_movie) == 0:
		return 0
	
	# Calc Euclidean distance
	sum_square = sum([pow(prefs[person_1][movie] - prefs[person_2][movie], 2) for movie in similar_movie])
	return 1/(1 + sqrt(sum_square))

