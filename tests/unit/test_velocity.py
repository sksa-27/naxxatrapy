from tests import *
from naxxatrapy.naxxatrapy import velocity


class TestAverageVelocity(unittest.TestCase):

    def test_velocity(self):
        self.assertEqual(velocity(10, 2), 5)
