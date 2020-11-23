#!/usr/bin/env python

from __future__ import print_function
import json
import rospy
from geometry_msgs.msg import Pose

from asset_manager.srv import AppendAsset, AppendAssetResponse
from asset_manager.srv import GetAssetPosebyId, GetAssetPosebyIdResponse
from asset_manager.srv import GetNearestAsset, GetNearestAssetResponse
class AssetManager
	def __init__(self):
		self.append_asset_server_ = rospy.Service('append_asset', AppendAsset, self.AppendAssetHandle)
	    self.filename = rospy.get_param("/asset_file_name")
	    with open(self.filename) as f:
	    	self.data = json.load(f)


	def AppendAssetHandle(self,req):
		if(True):
			temp_data = {req.id, req.Pose.position.x,req.Pose.position.y,req.Pose.position.z,req.Pose.orientation}
	def LoadAsset(self,filname):
		with open(filename) as f:
			self.data = json.load(f)
if __name__ == '__main__':
	rospy.init_node('asset_manager')
    AssetManager()
    rospy.spin()
