def main_and_max(arr): 
	if len(arr) <= 0: 
		return None, None 

	if len(arr) == 1: 
		return arr[0], arr[0]

	else if len(arr) == 2: 
		return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
	else: 
		n = len(arr) // 2 
		lmin, lmax = min_and_max(arr[:n]) 
		rmin, rmax = min_and_max(arr[n:]) 
		
		return min(lmin,rmin), max(lmax, rmax) 

