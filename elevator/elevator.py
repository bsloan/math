__author__ = "bsloan"

from sys import argv

def input_parser(filename):
    # parse input file and return a list of lists, in this format:
    # [7, (11, 6), (10, 5), (6, 8), (7, 4), (12, 7), (8, 9)]
    # [3, (7, 9), (3, 7), (5, 8), (7, 11), (11, 1)]
    # ...

    result = []
    with open(filename, "r") as inp:
        for line in inp:
            line_result = []

            if line == "":
                continue
            parts = line.strip("\n").split(":")
            line_result.append(int(parts[0]))

            requests = parts[1].split(",")
            for request in requests:
                request = request.split("-")
                line_result.append((int(request[0]), int(request[1])))

            result.append(line_result)
    return result

def print_path(path):
    # print out the elevator's path while calculating distance travelled
    distance = 0
    for p in range(len(path)):
        if p == 0:
            print path[p],
        elif path[p - 1] != path[p]:
            print path[p],
            distance += abs(path[p] - path[p - 1])
    print "(" + str(distance) + ")"

def path_mode_A(requests):
    # trivial solution for mode A
    final_path = []
    final_path.append(requests[0]) # starting floor
    for request in requests[1:]:
        final_path.append(request[0])
        final_path.append(request[1])
    print_path(final_path)

def path_mode_B(requests):
    # directional constants
    GOING_DOWN = 0
    GOING_UP = 1

    # initialize list of completed requests
    completed = []
    for i in range(0, len(requests)):
        completed.append(False)

    # list to hold the final path sequence travelled by the elevator
    final_path = []

    # initialize loop vars and the starting floor level
    i = 1
    next_i = 1
    final_path.append(requests[0])

    # iterate each request in the sequence
    while next_i < len(requests):
        path = []
        request = requests[i]

        # if we haven't already completed this request, add it to our path
        if not completed[i]:
            path.append(request[0])
            path.append(request[1])
            completed[i] = True

        # determine which direction we're going
        direction = (GOING_UP if request[0] < request[1] else GOING_DOWN)

        # iterate all consecutive requests to move in the same direction
        next_i = i + 1
        for j in range(next_i, len(requests)):
            next_direction = (GOING_UP if requests[j][0] < requests[j][1] else GOING_DOWN)

            # advance cursor to the next request in the sequence
            i = j

            # break loop if we've switched direction
            if next_direction != direction:
                break

            # otherwise, merge this request in on our current path
            else:
                if not completed[i]:
                    path.append(requests[j][0])
                    path.append(requests[j][1])
                    completed[i] = True

        # sort low to high all requests on this path if going up
        if direction == GOING_UP:
            path.sort()
        # otherwise, we're going down: sort high to low
        else:
            path.sort(reverse=True)

        # append this segment to the final path
        final_path += path

    print_path(final_path)

def main():
    # test routine for elevator
    if len(argv) != 3:
        print "usage: elevator.py <filename> <A|B>"
        print "example: python elevator.py testdata.txt B"
        exit()

    try:
        testdata = input_parser(argv[1])
    except:
        print "error parsing input file:", argv[1]
        exit(-1)

    if argv[2] == "A":
        print "elevator path using Mode A:"
        for requests in testdata:
            path_mode_A(requests)

    elif argv[2] == "B":
        print "elevator path using Mode B:"
        for requests in testdata:
            path_mode_B(requests)

    else:
        print "unrecognized mode for elevator:", argv[2]

if __name__ == "__main__":
    main()
