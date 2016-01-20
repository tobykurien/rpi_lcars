"""
interpolator.py
 
Perform a simple interpolation between two points of any dimention, without
the use of Numeric.
2007 Michael Thomas Greer
 
Released to the Public Domain
 
"""


class Interpolator(object):
    """
    The line actor. Returns successive points along a line until completely
    traversed. Once traversed this class can do nothing more.

    Care has been taken to fix errors due to floating-point arithmetic.

    implementation notes

      Following the docs, some simple math must be done to get the movement
      desired. The first thing to remember is that we cannot change the FPS,
      which is to say, we cannot change the speed of the program. So all our
      manipulations work by modifying the step size between the start and
      stop vectors (which, in other words, is the apparent speed of line
      traversal).

      For the default linear interpolation, the step size remains constant:

        step = dx *( 1.0 /FPS ) /seconds

      where dx represents the total distance to traverse for each dimention.

      For non-linear interpolations, we must factor in our shape, which is
      specified relative to the linear interpolation speed. The shape is a
      simple power function which gives us a nice, spikey curve with a
      vertical asymptote at the midpoint. The function is:

        factor = shape *(closeness_to_asymptote **(shape -1.0))

      where closeness_to_asymptote is a number in the range [0.0, 1.0]; 0.0
      being at either end of the line and 1.0 being at the asymptote. (The
      location of the asymptote, or "middle", is modifiable.)

      The final calculation is to modify each vector position by (step *factor).

    """

    #-------------------------------------------------------------------------
    def __init__(
        self,
        start=None,
        stop=None,
        seconds=None,
        fps=None,
        shape=1.0,
        middle=0.5
    ):
        R"""
        Create a new interpolator to produce timed vectors along a line.

        arguments
          start   - The initial vector. If no vectors are specified the object is
                    treated as a placeholder object and does absolutely nothing
                    but return the two-dimentional vector (0, 0).

          stop    - The final vector. If no final vector is specified the object
                    is treated as a placeholder object and does absolutely nothing
                    but return the 'start' vector.

          seconds - The number of seconds you wish the interpolation to take.

          fps     - The current number of frames per second. If you specify
                    seconds you must specify the FPS, otherwise a ValueError
                    exception is raised with the message "You must specify both
                    'seconds' and 'fps'."

          shape   - Modify the interpolation as non-linear.

                    First some quick information to explain:
                     - The total time to traverse the line is constant (in other
                       words, this function cannot take more or less 'seconds'
                       worth of vectors than you specify).
                     - For the same reason, the number of vectors produced by this
                       function (for a given value of 'seconds') is constant.
                     - Hence, the -speed- of a vector is defined wholly by the
                       distance between it the previously produced vector.
                     - In a linear interpolation, the distance between vectors (or
                       again, the speed of each vector) is constant; every vector
                       has the same speed.
                     - In a shaped interpolation, the speed of individual vectors
                       is modified: some are faster and some are slower.

                    The shape is the number of times greater than linear speed the
                    middle vector travels.

                    A shape of 1.0 is a linear interpolation. A shape of 2.0 has
                    slower vectors at the end and a vector in the middle traveling
                    twice as fast as it would in a linear interpolation. A shape
                    of 0.5 travels half as fast. There really isn't any upper-
                    limit, but zero is the lower. You'll get a ValueError if you
                    try any value less-than or equal-to zero.

          middle  - The location of the "middle vector" along the line, expressed
                    as a value from 0.0 (at 'start') to 1.0 (at 'stop').

        """
        self._sec = -1
        self._length = 0

        if start is None:
            start = (0, 0)
        if stop is None:
            self.stop = start

        else:
            if (seconds is None) or (fps is None):
                raise ValueError("You must specify both 'seconds' and 'fps'")
            if shape <= 0.0:
                raise ValueError("The 'shape' argument must have value > 0.0")
            if not (0.0 <= middle <= 1.0):
                raise ValueError(
                    "The 'middle' argument must be in range [0.0, 1.0]")

            self.stop = stop
            self.diff = [b - a for a, b in zip(start, stop)]
            self.inc = 1.0 / fps
            self.step = [a * self.inc / seconds for a in self.diff]
            self._pos = start
            self._sec = seconds
            self.seconds = seconds
            self.shape = shape
            self.mid = middle
            self.maxs = [max(a, b) for a, b in zip(start, stop)]
            self.mins = [min(a, b) for a, b in zip(start, stop)]
            self._length = None

    #-------------------------------------------------------------------------
    def next(self):
        R"""
        Calculate the location of the next vector in the line.

        The 'start' vector cannot be a "next" vector. (This is actually rather
        convenient if you think about it.) That said, if your interpolation is set
        up right, the first "next" vector might actually be in the same location
        as the 'start' vector...

        Care is taken that the 'stop' vector is always the final vector.

        returns
          The next vector or None if all done.

        """

        def d(a, b, c):
            if b == 0.0:
                return c
            else:
                return a / b

        if self._sec >= 0.0:

            if self.shape == 1.0:
                factor = 1.0
            else:
                percent = 1.0 - (self._sec / self.seconds)  # percent complete

                if percent < 0.95:
                    if percent > self.mid:
                        k = d((1.0 - percent), (1.0 - self.mid), 1.0)
                    else:
                        k = d(percent,        self.mid,  0.0)

                    if k in [0.0, 1.0]:
                        factor = k * self.shape
                    else:
                        factor = pow(k, self.shape - 1.0) * self.shape

                else:
                    # The final 5% of the line is calculated linearly to avoid any
                    # 'jump' or 'snap' artifacts caused by FPU arithmetic errors.
                    if self.mid is not None:
                        self.diff = [
                            b - a for a, b in zip(self._pos, self.stop)]
                        self.step = [
                            a * self.inc / self._sec for a in self.diff]
                        self.mid = None
                    factor = 1.0

            self._pos = tuple(
                [min(max(

                    a + (step * factor),

                    mina), maxa)
                 for a, step, mina, maxa in
                 zip(self._pos, self.step, self.mins, self.maxs)
                 ]
            )

            self._sec -= self.inc
            return self._pos

        else:
            self._pos = self.stop
            return None

    #-------------------------------------------------------------------------
    def _get_pos(self):
        R"""Return the current vector's location."""
        return self._pos

    #-------------------------------------------------------------------------
    def _get_length(self):
        R"""
        Returns the length of the line. The line's length is not calculated
        until first required.

        """
        from math import sqrt

        if self._length is None:
            sum1 = 0
            for a in self.diff:
                sum1 += a * a
            self._length = sqrt(sum1)
        return self._length

    #-------------------------------------------------------------------------
    pos = property(
        _get_pos,    doc='The location of the current vector. Read-only.')
    length = property(_get_length, doc='The length of the line. Read-only.')

# end interpolator
