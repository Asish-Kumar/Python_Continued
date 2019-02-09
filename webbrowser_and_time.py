# Author: Asish Kumar
# import webbrowser

# webbrowser.open("http://youtube.com")  # opens the url in the default browser
# help(webbrowser)
# ########################----UNDERSTANDING PRINT STATEMENT----##################################################
# print(1, 3, 4, 5, 6)  # default separator is ' ', i.e., space
# print(1, 3, 4, 5, 6, sep="--Pyth--", flush=True)  # here we have --Pyth-- as our new separator
# print(end="jack")  # by default empty print statement prints the end parameterq
# ########################----UNDERSTANDING TIME MODULE----######################################################
# import time
#
# print(time.gmtime(45))  # this returns a named tuple from 1 jan 1970 + 45 sec
# print(time.localtime())  # this returns a named tuple from current UTC time
# print(time.time())  # this returns float, the number of seconds from epoch to now
# # epoch = 1 jan 1970, 00:00:00
#
# curr_time = time.localtime()
# print(curr_time)
# print("Year: ", curr_time.tm_year, ", Year: ", curr_time[0])  # curr_time[0] method is not preferred
# print("Month: ", curr_time.tm_mon, ", Month: ", curr_time[1])
# print("Day: ", curr_time.tm_mday, ", Day: ", curr_time[2])
# ########################----USING TIME MODULE----###############################################################
# import time
# from time import time as my_timer
# # from time import perf_counter as my_timer  # more precise than time and best to use
# # from time import monotonic as my_timer  #
# import random
#
# input("Please enter to start")
#
# wait_time = random.randint(0, 5)
# time.sleep(wait_time)
# start_time = my_timer()
# input("Please enter to stop")
# end_time = my_timer()
#
# print("Started at " + time.strftime("%X", time.localtime(start_time)))
# print("Ended at " + time.strftime("%X", time.localtime(end_time)))
# print("Your response time is {} sec".format(end_time - start_time))
# ########################----DIFFERENCE BETWEEN FOLLOWING----#####################################################
import time

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t", time.get_clock_info('perf_counter'))
print("monotonic():\t", time.get_clock_info('monotonic'))
print("process_time():\t", time.get_clock_info('process_time'))

