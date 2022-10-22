#! /usr/bin/env python
import unittest
import rospy
from std_msgs.msg import String, Int16
from time import sleep
import rostest

class testCase(unittest.TestCase):
    talker_ok = False
    def callback(self, data):
        self.talker_ok = True
        rospy.loginfo(data.data)

    def test_if_publishes(self):
        topic = "chatter"
        rospy.init_node('tester')
        rospy.Subscriber(topic, Int16, self.callback)
        counter = 0

        while not rospy.is_shutdown() and counter < 5 and (not self.talker_ok):
            sleep(1)
            counter += 1

        self.assertTrue(self.talker_ok)
if __name__ == "__main__":
    rostest.rosrun('ros_package', 'tester', testCase)
