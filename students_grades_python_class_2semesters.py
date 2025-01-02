#How do students in a python class compare to students from a prior semester? 
#Write a program that reads in the csv file linked above and outputs the mean,
#median, and standard deviation for the fall & spring semesters. Make sure to write
#at least two functions in your final solution. The more generalizable you make
#your code, the more you may be able to reuse it for your own project later.
#To receive feedback, please submit a screenshot of your program & its output.
#
#Kevin assist
import statistics

def read_file(filename: str) -> list:
    """""
    Reads a file and returns a list of strings.
    """
    with open(filename, "r") as f:
        return f.readlines()

def main():
    fall_grades = []
    spring_grades = []
    #read in formatted data line by line, stripping them of white space & placing them into quotations w/ commas separating (three fields)
    for line in read_file("grades.csv"):
        line = line.strip()
        line_list = line.split(",")
        #make spring and fall lists of grades
        if line_list[1] == "Spring 2016":
            spring_grades.append(line_list[2])
        if line_list[1] == "Fall 2016":
            fall_grades.append(line_list[2])
    
    #convert list to integers and sum them up
    spring_ints = [int(grade) for grade in spring_grades]
    spring_sum_tot = sum(spring_ints)
    fall_ints = [int(gradef) for gradef in fall_grades]
    fall_sum_tot = sum(fall_ints)
    
    #utilize the python built in "statistics" module
    spring_med = statistics.median(spring_ints)
    fall_med = statistics.median(fall_ints)
    spring_std_dev = statistics.stdev(spring_ints)
    fall_std_dev = statistics.stdev(fall_ints)
    
    #manually formatted the ouput table
    print(f"  Spring Mean: {spring_sum_tot / len(spring_ints): .2f}, "
          f"              Fall Mean: {fall_sum_tot / len(fall_ints): .2f},\n "
          f" Spring Median: {spring_med: .2f}, "
          f"            Fall Median: {fall_med: .2f},\n "
          f" Spring Standard Deviation: {spring_std_dev: .2f}, "
          f"Fall Standard Deviation: {fall_std_dev: .2f}"
    )
main()






