"""Tower of Hanoi module"""


class TowerOfHanoi:
    """Allows solving the Towers of Hanoi problem"""

    def solve(self, number_of_disc):
        """Solve the Towers of Hanoi Problem"""
        self._move(number_of_disc, "A", "B", "C")

    def _move(self, number, source, temp, destination):
        """Recursive call to solve Tower of Hanoi"""

        # This is the base case.  Nothing to move beyond one disc.
        # So, print the one step out.
        if number == 1:
            print(f"Move disc from tower {source} to tower {destination}")
        # Else, not the base case, so, recursively move discs around.
        else:
            # Make recursive call to move number-1 discs from the source peg to
            # the temp peg.
            self._move(number - 1, source, destination, temp)

            # Move a recursive call to move the 1 disc (bottom) from the source
            # to the destination.
            self._move(1, source, temp, destination)

            # Make a recursive call to move number-1 discs from temp to
            # destination.
            self._move(number - 1, temp, source, destination)
