

def get_num_user_input(min_: int, max_: int) -> int:
	user_input = ''
	while True:
		user_input = input('>> ')

		if not user_input.isdigit():
			print('Invalid Input')
			continue

		selection = int(user_input)

		if selection < min_ or selection >= max_:
			print('Invalid Input')
			continue

		return selection
