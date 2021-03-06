# WORD FREQUENCY ANALYSIS
 # Create a frequency dictionary for each word in the lyric
def freq_analysis(lyric):
	
	# split the string into list of characters
	updated_lyric = lyric.split()
	word_freq = {}
	for w in updated_lyrics.keys():
		if w in word_freq:
			word_freq[w] += 1
		else:
			word_freq.setdefault(w, 0)
	return word_freq

# WORD WITH MOST FREQUENCY
 # Create an array with 1st element being a list and 2nd element being the highest frequency
def highest_freq_word(freq_dict):
	
	list_song = []
	highest_freq = max(freq_dict.values())
	for w in freq_dict.values():
		if w == highest_freq:
			list_song.append(w)
	return (list_song, highest_freq)

# WORD WITH AT LEAST N FREQUENCY
def most_often_words(freq_dict):
	pref = int(input("What is your preference? "))
	list_of_words = []
	while True:
		# Create a temporaty value to analyze
		curr_analysis = high_freq_word(freq_dict)	
							
		if curr_analysis[1] >= pref:
			# add the whole array to the result
			list_of_words.append(curr_analysis)	
			for w in curr_analysis[0]:
				# directly mutate the freq_dict for the next loop
				del(freq_dict[w])	 
		else:
			break
	return list_of_words
		
			
	
