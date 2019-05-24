def get_itinerary(flights, current_it): 
	if not flights: 
		return current_it
	
	last_stop = current_it[-1]
	for i, (origin, destination) in enumerate(flights): 
		flights_minus_current = flights[:i] + flights[i+1:]
		current_it.append(destination) 

		if origin == last_stop: 
			return get_itinerary(flights_minus_current, current_it)
		current_it.pop()
	
	return None 

flights = [('SFO', 'HKO'), ('YYZ','SFO'), ('YUL','YYZ'), ('HKO','ORD')] 
current_it = ['YUL'] 

print(flights) 
print(get_itinerary(flights, current_it)) 
 
