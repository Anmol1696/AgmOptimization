"""
    This script consits of all functions related to flight data
"""

def read_flights_file(flights_filename):
    """
        Return the 7 parameters mentioned in the flights file as flight_stuct list
        flight_stuct is a dict with 7 parameters
    """
    with open(flights_filename) as file_open:
        all_lines = file_open.readlines()

    flight_stuct_list = []

    for line in all_lines:
        temp_line = map(int, line.split('\n')[0].split(' '))
        
        temp_stuct = {
            'starting_time'         : temp_line[0],
            'origin'                : temp_line[1],
            'destination'           : temp_line[2],
            'speed'                 : temp_line[3],
            'trail_sepration'       : temp_line[4],
            'takeoff_land_distance' : temp_line[5],
            'priority'              : temp_line[6]
        }

        flight_stuct_list.append(temp_stuct)

    return flight_stuct_list


if __name__ == "__main__":
    file_name = 'data/mum_airport_full_flights.txt'

    flight_stuct_list = read_flights_file(file_name)

    for x in flight_stuct_list:
        print x

