def velocity(displacement, time):
    """
        Calculate velocity given displacement and time
        Parameters
        ----------
        displacement : float
        time: float

        Returns
        -------
        float
    """
    pass


def displacement(velocity, time, acceleration):
    """
        Calculate displacement given velocity and time
        Parameters
        ----------
        velocity : float
        time: float

        Returns
        -------
        float
    """
    pass


def average_velocity(velocity_list):
    """
        Calculate the average velocity given multiple velocities
        Parameters
        ----------
        velocity_list : list

        Returns
        -------
        float
    """
    pass


def acceleration(velocity, time):
    """
        Calculate the acceleration given velocity and time
        Parameters
        ----------
        velocity : float
        time: float

        Returns
        -------
        float
    """
    pass

def initial_velocity(final_velocity, acceleration, time):
    """
        Calculates the initial_velocity when given final_velocity, acceleration and time

        Parameters
        ----------
        final_velocity : float
        acceleration : float
        time : float

        Returns
        -------
        float
    """
    return final_velocity - acceleration * time


def final_velocity(initial_velocity, acceleration, time):
    """
        Calculates the final_velocity when given initial_velocity, acceleration and time

        Parameters
        ----------
        initial_velocity : float
        acceleration : float
        time : float

        Returns
        -------
        float
    """
    return initial_velocity + acceleration * time


def momentum(mass, velocity):
    """
        Calculates the momentum when given mass and velocity

        Parameters
        ----------
        mass : float
        velocity : float

        Returns
        -------
        float
    """
    return mass * velocity


def force(mass, acceleration):
    """
        Calculates the momentum when given mass and acceleration

        Parameters
        ----------
        mass : float
        acceleration : float

        Returns
        -------
        float
    """
    return mass * acceleration


def gravitational_force(M, m, r, G = 6.674 * ( 10 ** - 11 ) ) :
    """
        Calculates the gravitational_force when given Mass of object1 = M, Mass of object2 = m, Distance
        between center of masses = r and Gravitational constant = G

        Parameters
        ----------
        M : float
        m : float
        r : float

        Returns
        -------
        float
    """
    return  G * M * m  / r ** 2


def work():
    pass


def power():
    pass


def kinetic_energy():
    pass


def total_energy():
    pass


def centripetal_force():
    pass


def friction():
    pass


def normal_force():
    pass


