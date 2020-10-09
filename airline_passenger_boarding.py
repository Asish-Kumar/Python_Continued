# ======== Task is Described at the end ========

# ======== Uncomment and use the below two lines in place of line number 7 ========
# file_name = input("Enter the input file name: ")
# with open(file_name, 'r') as sample_file:

with open("sample_airplane_passenger_boarding.txt", 'r') as sample_file:
    # server1 is for business class, server0 is for tourist class
    no_of_server1, no_of_server0 = [int(x) for x in sample_file.readline().strip().split()]  # read first line from sample_file
    server1_time_list = [0.0 * no_of_server1]
    server0_time_list = [0.0 * no_of_server0]
    read_list = list(sample_file.readlines())  # this list contains all the remaining data from the sample_file
    read_list.pop(-1)  # remove the dummy data from the last
    p_list = []
    for x in read_list:  # iterating through every elements of read_list
        x.strip()
        x1, x2, x3 = x.split()
        p_list.append((float(x1), int(x2), float(x3)))  # this list contains data type casted to correct data type

    q_server1 = []
    len_q_server1 = 0
    q_server0 = []
    len_q_server0 = 0

    for x in p_list:
        if x[1] == 1:
            q_server1.append(x)
            len_q_server1 += 1
        else:
            q_server0.append(x)
            len_q_server0 += 1

    q1_passenger_wait_time = 0
    q0_passenger_wait_time = 0
    server1_idle_time = 0
    server0_idle_time = 0
    # ======== Round 1: Serve only the respective passengers ========
    # serve business class passengers in server 1
    i = 0
    while i < len_q_server1:
        min_server1_time = min(server1_time_list)
        min_server1_time_index = server1_time_list.index(min_server1_time)

        if q_server1[i][0] <= min_server1_time:
            q1_passenger_wait_time += min_server1_time - q_server1[i][0]
            server1_time_list[min_server1_time_index] += q_server1[i][2]  # scheduled passenger i
        else:
            server1_idle_time += q_server1[i][0] - min_server1_time
            server1_time_list[min_server1_time_index] = q_server1[i][0] + q_server1[i][2]  # scheduled passenger i
        i += 1

    time_last_service_completed_server1 = max(server1_time_list)
    server1_people_served = len_q_server1

    # serve tourist class passengers in server 0 until all server 1 are free (end of round 1)
    i = 0
    while i < len_q_server0 and q_server0[i][0] < time_last_service_completed_server1:
        min_server0_time = min(server0_time_list)
        min_server0_time_index = server0_time_list.index(min_server0_time)

        if q_server0[i][0] <= min_server0_time:
            q0_passenger_wait_time += min_server0_time - q_server0[i][0]
            server0_time_list[min_server0_time_index] += q_server0[i][2]  # scheduled passenger i
        else:
            server0_idle_time += q_server0[i][0] - min_server0_time
            server0_time_list[min_server0_time_index] = q_server0[i][0] + q_server0[i][2]  # scheduled passenger i
        i += 1

    time_last_service_completed_server0 = max(server0_time_list)
    server0_people_served = i

    round1_people_served = server1_people_served + server0_people_served
    time_last_service_completed = max(time_last_service_completed_server1, time_last_service_completed_server0)
    print("Total number of people served in round 1:", round1_people_served)
    print("Time last service request is completed:", time_last_service_completed)

    # ======== Round 2: Serve all the passengers in any available server ========
    j = i
    while i < len_q_server0:
        min_server0_time = min(server0_time_list)
        min_server1_time = min(server1_time_list)
        if min_server0_time < min_server1_time:  # serve current passenger through class 0 server
            min_server0_time_index = server0_time_list.index(min_server0_time)
            if q_server0[i][0] <= min_server0_time:
                q0_passenger_wait_time += min_server0_time - q_server0[i][0]
                server0_time_list[min_server0_time_index] += q_server0[i][2]  # scheduled passenger i
            else:
                server0_idle_time += q_server0[i][0] - min_server0_time
                server0_time_list[min_server0_time_index] = q_server0[i][0] + q_server0[i][2]  # scheduled passenger i

        else:  # serve current passenger through class 1 server
            min_server1_time_index = server1_time_list.index(min_server1_time)
            if q_server0[i][0] <= min_server1_time:
                q1_passenger_wait_time += min_server1_time - q_server0[i][0]
                server1_time_list[min_server1_time_index] += q_server0[i][2]  # scheduled passenger i
            else:
                server1_idle_time += q_server0[i][0] - min_server1_time
                server1_time_list[min_server1_time_index] = q_server0[i][0] + q_server0[i][2]  # scheduled passenger i
        i += 1

    time_last_service_completed_server0 = max(server0_time_list)
    time_last_service_completed_server1 = max(server1_time_list)

    round2_people_served = i-j
    time_last_service_completed = max(time_last_service_completed_server1, time_last_service_completed_server0)

    print("Total number of people served in round 2:", round2_people_served)
    print("Time last service request is completed:", time_last_service_completed)

    print("Total idle time for server 1:", server1_idle_time)
    print("Total idle time for server 0:", server0_idle_time)

    print("Average wait time for tourist class passengers:", q0_passenger_wait_time / len_q_server0)
    print("Average wait time for business class passengers:", q1_passenger_wait_time / len_q_server1)

    # ============== Following outputs smajh nhi aaye mujhe ==============
    #  Average total service time (this includes time spent in a queue).
    #  Average total time in queue(s). Both overall and separate.
    #  Average length of queue. For each queue and overall.
    #  Maximum Length of queue. For each queue and overall.




















# Your task for this assignment is to investigate some of the properties of queues and their
# management.
# You should write a program which simulates the queuing and service of airline passengers.
# Your program should first read in a file name from standard input and then open this file and
# read data from the named file.
# The input file will contain the following data:
#  The number of first/business class servers in the system
#  The number of tourist class servers in the system
#  A set of passengers, each consisting of an arrival time, a class and a service time.
# o Class is an integer where 0 indicates a tourist class passenger and 1 indicates
# a first/business class passenger.
#  This set is terminated by a dummy record with arrival time and service times all equal
# to 0.
#  Note: the arrival times are sorted in ascending order.
# The simulation is to be of an airline check in system with two sets of servers, first/business
# class and tourist class, with a single queue associated with each set. Customers arrive in the
# system and are served by a server of the appropriate class. If all servers of a particular type
# are busy, the customer will enter either the first/business or tourist class queue as appropriate.
# The simulation should be run until the last customer has left the system.
# The simulation will run twice, in the first run each server will only serve passengers of the
# appropriate class. In the second run the first/business class servers will be able to serve
# passengers in the tourist class queue if no first/business class customers are waiting.
# Output, to standard output will consist of the following data for each run:
#      Number of people served.
#  Time last service request is completed.
#  Average total service time (this includes time spent in a queue).
#  Average total time in queue(s). Both overall and separate.
#  Average length of queue. For each queue and overall.
#  Maximum Length of queue. For each queue and overall.
#  Total idle time for each server.
#     Notes: Do not use classes – structs are ok but no function pointers in them.
# Do not use the STL
# There will be no more than twenty servers of each type (40 total)
# Each of the two queues will never have more than 500 people in them
# The simulation should be discrete, i.e. event driven. There should not be a fixed
# length ‘tick’.
# Programs may be written in any of C, C++, Java and Python. Programs which do not compile
# and run will receive no marks.
# Programs should be appropriately documented with comments.
#     Programs should be submitted via moodle as ass2.ext where ext is one of c, cpp, java or py.