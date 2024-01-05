#!/usr/bin env python2

import rospy
from std_msgs.msg import Int32MultiArray

def callback(data):
    global pub
    pub = rospy.Publisher("uc_controls", type, queue_size=10)
    pub.publish(data.data)

def main():
    rospy.init_node('science_control', anonymous=True)
    rospy.Subscriber('commands', Int32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    main()