import pystats as ps


def choices(selection):
	if selection <= 10:
		if not (selection == 4 or selection == 5 or selection == 9):
			print("\nPlease Separate List Elements Using a Comma (,)")
			v = [int(num) for num in list(input("Input List: ").split(","))]
			if selection == 1:
				print(f"Mean: {ps.mean(v)}")
			elif selection == 2:
				print(f"Mode: {ps.mode(v)}")
			elif selection == 3:
				print(f"Median: {ps.median(v)}")
			elif selection == 6:
				print(f"Range: {ps.rang(v)}")
			elif selection == 7:
				print(f"Variance: {ps.var(v)}")
			elif selection == 8:
				print(f"Standard Deviation: {ps.std(v)}")
			elif selection == 10:
				print(f"Interquartile Range: {ps.iqr(v)}")
		else:
			if selection == 4:
				print("\nPlease Separate Inputs Using a Comma(,)")
				N, n = input("Input N and n: ").split(",")
				print(f"Skip Number: {ps.skip_number(int(N), int(n))}")
			if selection == 5:
				print("\nPlease Separate Inputs Using a Comma(,)")
				class_freq, total_freq = input("Input Class Frequency and Total Frequency: ").split(",")
				print(f"Relative Frequency: {ps.relative_frequency(int(class_freq), int(total_freq))}")
			if selection == 9:
				x = input("Input Score: ")
				print("\nPlease Separate Inputs Using a Comma(,)")
				v = [int(num) for num in list(input("Input List (Population or Sample): ").split(","))]
				print(f"Z-score {ps.z_score(int(x), v)}")
				
				
def main():
	print("MyStats v.1")
	
	print("\nMethods for Describing Sets of Data")
	print("\n(1) Mean"
	"\n(2) Mode"
	"\n(3) Median"
	"\n(4) Skip Number (Systematic Sampling)"
	"\n(5) Relative Frequency"
	"\n(6) Range"
	"\n(7) Variance"
	"\n(8) Standard Deviation"
	"\n(9) Z-score (Population or Sample)"
	"\n(10) Interquartile Range")
	
	selection = 0
	is_int = False
	while is_int is False or int(selection) > 10:
		selection = input("\nSelect a Number: ")
		is_int = selection.isdigit()
		if is_int is False:
			print("*Please Input a Number*")
		elif int(selection) > 10:
			print("*Please Input a Number Less Than 10")
			
	choices(int(selection))
	
if __name__ == '__main__':
	main()
