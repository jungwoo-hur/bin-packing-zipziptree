# Example file: next_fit.py
# explanations for member functions are provided in requirements.py

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):

	c_b_index = 0
	c_b_size = 0

	for i in range(0, len(items)):

		if c_b_size + items[i] <= 1:	
			assignment[i] = c_b_index
			c_b_size += items[i]

			if i == (len(items) - 1):
					free_space.append(1 - c_b_size)

					
		else:
			c_b_size = items[i]
			free_space.append(1 - c_b_size) 


			assignment[i] = c_b_index
			c_b_index += 1

			if i == (len(items) - 1):
					free_space.append(1 - c_b_size)
