"""
Your module documentation here

"""


class PrimeClass(object):
    """
    Your class documentation here
    """

    def is_prime(self, num_int):
        """
        Every prime number can only be divided between 1 and itself: hence,
        we check every single integer number between 2 and num_int
        to see if num_int would return an integer for any of these cases
        """

        # 1 is not a prime number, for arithmetic reasons
        if num_int == 1:
            return False
        for xyz in range(2, (num_int)):
            if num_int % xyz == 0:
                return False

            # otherwise, the number is Prime
        return True
