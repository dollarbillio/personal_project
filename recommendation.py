# USING EUCLIDEAN DISTANCE
 # THEORY: compare 2 people one at a time, using axes. How many axes depends on 
  # how many movies they've all seen. Each person will be represented by a dot in the n-dimension
   # corresponding to their scores on each movie. People whose' dots are near(Euclidean distance) 
    # are likely to have same taste
 # DISADVANTAGES: when there is a 'grade inflation' (one person consistenly assigning too higher point) 
  # or 'grade deflation'(consistentlyassigning lower point) -> distance point is large even though they may have same taste
 # MATH: sqrt(sum ((x1 - x2)**2 + (y1 - y2)**2 + ...)) 

from math import sqrt

def similar_taste (prefs, person_1, person_2):
	"""Return a score btw 0 and 1. Higher = more similar"""
	
	# check how many movies they've seen together
	similar_movie = {}
	for movie in prefs[person_1]:
		if movie in prefs[person_2]:
			similar_movie[movie] = 1
	
	# there is no movie, return 0
	# it check this condition first, if True, the below 'return' will not be executed
	if len(similar_movie) == 0:
		return 0
	
	# Calc Euclidean distance
	sum_square = sum([pow(prefs[person_1][movie] - prefs[person_2][movie], 2) for movie in similar_movie])
	return 1/(1 + sqrt(sum_square))
=========================================================================================================================================
# USING PEARSON CORRELATION COEFFICIENT:
 # THEORY: compare 2 people at a time, using only 2D axes to represent 2 people
  # the dots will be movies. We use 'Pearson correlation coefficent' to see how easily can we fit those dots into a line
   # the more the corr_coeff is near -1(negative) or 1(positive), the better the relation of their taste
 # ADVANTAGES: solving the problem of 'consistent grade inflation' or 'consistent grade deflation'
 # MATH: nominator = n(∑xy) - (∑x)(∑y) / denominator = sqrt([n(∑x^2) - (∑x)^2][n(∑y^2) - (∑y)^2])

from math import sqrt

def pearson_corrcoef(data, p1, p2):
	"""Return the value of PEARSON Corr_coeff"""
	
	# Determine shared_items
	shared_items = {}
	for item in data[p1]:
		if item in data[p2]:
			shared_items[item] = 1
	n = len(shared_items)
	if n == 0:
		return 0
	
	sum1 = sum([data[p1][item] for item in shared_items])
	sum2 = sum([data[p2][item] for item in shared_items])
	sum_product = sum([data[p1][item] * data[p1][item] for item in shared_items])
	sumSq1 = sum([pow(data[p1][item], 2) for item in shared_items])
	sumSq2 = sum([pow(data[p2][item], 2) for item in shared_items])
	
	nom = n * sum_product - sum1 * sum2
	denom = sqrt((n * sumSq1 - pow(sum1, 2)) * (n * sumSq2 - pow(sum2, 2)))
	
	return nom/demon
=========================================================================================================================================
# RETURN THE WHOLE LIST WITH SIMILARITY POINT
# THEORY: return a list with each element being a tuple containing a similarity point (depending on which function choosen from above)
 # and the each person's name

def topMatches(data, p1, similarity = pearson_corrcoef):
	# similarity can now be a function as pearson_corrcoef
    
	scores = [(similarity(data, p1, other), other) for other in data if other != p1]
	while True:
		n = int(input("How many top match do you want to display? "))
		if n > len (scores):
			print("Out of range please try again!")
		else:
			break
	scores.sort(reverse = True)
	return scores[0:n]
=========================================================================================================================================
# RETURN THE UNSEEN MOVIES AND THE CORRESPONDING SCORE BASED ON WEIGHTED AVERAGE REVIEWS FROM OTHER USERS
# Theory: After calculating similarity point based on Pearson_Corr_Coeff, we give weight to unseen movie reviews by other critics by 
 # multiplying the similarity by others's score. Then we take the sum of all critics related to that movie and come up with the final
  # score by dividing the total by the total_sim_score

def unseen_movies(data, person, similarity):
	
	# create empty lists to store total_score and total_sum_score
	total_score = {}
	total_sim_score = {}
	
	# Loop through other people
	for other in data:
		# skip the person
		if other == person:
			continue
		sim_score = similarity(data, person, other)
		# skip if sim_score is zero or negative
		if sim_score <= 0:
			continue
		
		# Loop through movies
		for movie in data[other]:
			# choose unseen movie only 
			if movie not in data[person]:
				# total weighted score for each movie
				total_score.setdefault(movie, 0)
				total_score[movie] += data[other][movie] * sim_score
				# total sim_score for each movie
				total_sim_score.setdefault(movie, 0)
				total_sim_score[movie] += sim_score
	# Calculating score for each movie
	final_score = [(total / total_sim_score[movie]) for movie, total in total_score.items()]
	final_score.sort(reverse = True)
	return final_score
	
	

