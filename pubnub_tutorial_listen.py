from pubnub import Pubnub

pubnub = Pubnub(
	publish_key = "pub-c-e58be9c3-c466-4efa-9da8-5382cd64792d",
	subscribe_key = "sub-c-c0bdecde-e682-11e6-a85c-0619f8945a4f")

channel = "nhan_channel"

def callback(message, channel):
	print('[' + channel + ']: ' + str(message))

pubnub.subscribe(
	channel,
	callback = callback)