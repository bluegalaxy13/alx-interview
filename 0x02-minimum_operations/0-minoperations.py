#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    # starting no. of H's
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done # copy all
            done = done + clipboard # paste
            ops_count = ops_count + 2 # increment operatoions by 2 as copy all and paste has occured
        elif n - done > 0 and (n - done) % done == 0: # checks if there are still more H's needed to equal n and if the number of H's in clipvoard is a multiple of itself
            # copy all and paste
            clipboard = done
            done = done + clipboard
            ops_count = ops_count + 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done = done + clipboard
            ops_count = ops_count + 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return ops_count
