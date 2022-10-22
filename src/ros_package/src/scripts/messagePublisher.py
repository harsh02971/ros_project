import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
#Callback function to print the subscribed data on the terminal
def callback_str(subscribedData):
     
     rospy.loginfo(subscribedData.data)

#Subscriber node function which will subscribe the messages from the Topic
def messageSubscriber():
    topic = "chatter"
    #initialize the subscriber node called 'messageSubNode'
    rospy.init_node('listener', anonymous=False)
    #This is to subscribe to the messages from the topic named 'messageTopic'
    rospy.Subscriber(topic, Int16, callback_str)
    #rospy.spin() stops the node from exitind until the node has been shut down
    rospy.spin()
if __name__ == '__main__':
    try:
        messageSubscriber()
    except rospy.ROSInterruptException:
        pass
