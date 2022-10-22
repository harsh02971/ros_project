# coding: utf-8
# #import the rospy package and the String message type
import rospy
from std_msgs.msg import String, Int16
#function to publish messages at the rate of 2 messages per second
def messagePublisher():
    #define a topic to which the messages will be published
    topic = "chatter"
    message_publisher = rospy.Publisher(topic, Int16, queue_size=10)
    #initialize the Publisher node.
    #Setting anonymous=True will append random integers at the end of our publisher node
    rospy.init_node('generator', anonymous=True)
    rospy.loginfo("I will publish to the topic %s", topic)
    #publishes at a rate of 2 messages per second
    rate = rospy.Rate(2)
    message = 1
    #Keep publishing the messages until the user interrupts
    while not rospy.is_shutdown():
        message += 1
        #display the message on the terminal
        rospy.loginfo(message)
        #publish the message to the topic
        message_publisher.publish(message)
        #rate.sleep() will wait enough until the node publishes the     message to the topic
        rate.sleep()
if __name__ == "__main__":
    try:
        messagePublisher()
    #capture the Interrupt signals
    except rospy.ROSInterruptException:
        pass
