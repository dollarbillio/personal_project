
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
	
	

