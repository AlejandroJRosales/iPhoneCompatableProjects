def mean(v):
	return sum(v)/len(v)
	
	
def mode(v):
	return max(set(v), key=v.count)
	
	
def median(v):
	if not (all([v[i] <= v[i + 1] for i in range(len(v) - 1)])):
		print("List is not sorted")
		usr_input = input("Would you like to sort the list from least to greatest: ").lower()
		if "y" in usr_input:
			v.sort()
	if len(v) % 2 == 0:
		return (v[int(len(v) / 2)] - v[int(len(v) / 2 - 1)]) / 2 + v[int(len(v) / 2 - 1)]
	else:
		return v[int((len(v) + 1) / 2) - 1]
		
		
def skip_number(N, n):
	return int(N/n)
	
	
def relative_frequency(class_freq, total_freq):
	return class_freq/total_freq
	
	
def rang(v):
	return max(v) - min(v)
	
	
def var(v):
	summation = 0
	x_bar = mean(v)
	for x in v:
		summation += ((x - x_bar)**2)
	return summation/(len(v) - 1)
	
	
def std(v):
	return var(v)**0.5
	
	
def z_score(x, v):
	return (x - mean(v))/std(v)
	
	
def iqr(v):
	if not (all([v[i] <= v[i + 1] for i in range(len(v) - 1)])):
		v.sort()
	center = len(v)/2
	if len(v) % 2 == 0:
		left, right = v[:int(center)], v[int(center):]
	else:
		left, right = v[:int(center)], v[int(center) + 1:]
	return median(right) - median(left)
