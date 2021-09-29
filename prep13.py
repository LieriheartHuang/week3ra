def count_characters(str_1, str_2, str_3):
	cnt = 0
	for c in str_1:
		if c == str_2[0] or c == str_3[0]:
			cnt += 1
	print("'%s' and '%s' appeared %d times in the string '%s'" % (str_2, str_3, cnt, str_1))
