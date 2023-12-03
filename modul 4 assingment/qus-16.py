Que-16 : Can one block of except statements handle multiple exception?
ans :- Yes, a single block of except statements in Python can handle multiple exceptions. 
	
	 Example:--
		try:
		   x = 10 / 0
		   y = int("abc")

		except (ZeroDivisionError, ValueError) as e:
		   print("An error occurred:", str(e))
