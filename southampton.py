from datetime import datetime
import os
import sys
import json
import urlparse

def do_stats(base_path):
	default_profile_stat = dict()
	protected_user_stat = dict()
	protected_user_list = list()
	user_stat = 0
	
	# result of analysis
	result = dict()

	for filename in os.listdir(base_path):
		f = open(base_path + filename)
		
		while True:
			header = f.readline()
			if (header == ""):
				break
			content = f.readline()
			
			# parse the header
#			print "header: " + header.strip()
			temp = header.split('###')
			temp = temp[2].split(' ')
			uid = temp[2]							# uid
			
			# parse the json
			data = eval(content)				# content in dictionary format
			
			protected = unicode(data['protected'])
			try:
				default_img = unicode(data['default_profile_image'])
			except KeyError:
				default_img = 'True'
			
			# analyze protected
			if not protected_user_stat.has_key(protected):
				protected_user_stat[protected] = 0
			protected_user_stat[protected] += 1
			
			# save the uid of protected user
			if protected:
				protected_user_list.append(uid)
			
			# analyze default profile image
			if not default_profile_stat.has_key(default_img):
				default_profile_stat[default_img] = 0
			default_profile_stat[default_img] += 1
			
			# count user
			user_stat += 1
			if (user_stat % 10000) == 0:
				print "processed %d th user" % user_stat
	
	result['protected_stat'] = protected_user_stat
	result['protected_list'] = protected_user_list
	result['default_profile_stat'] = default_profile_stat
	result['user_count'] = user_stat	
	
	return result
		
def do_stats2(base_path):
	default_profile_stat = dict()
	protected_user_stat = dict()
	protected_user_list = list()
	user_stat = 0
	
	result = dict()
	
	for filename in os.listdir(base_path):
		print filename
		
		f = open(base_path + filename)
		
		while True:
			header = f.readline()
			if (header == ""):
				break
			content = f.readline()
			
			# parse the header
#			print "header: " + header.strip()
			temp = header.split('###')
			temp = temp[2].split(' ')
			uid = temp[2]							# uid
			
			# parse the json
			data = eval(content)				# content in dictionary format
			
			protected = unicode(data['protected'])
			try:
				default_img = unicode(data['default_profile_image'])
			except KeyError:
				default_img = True
			
			# analyze protected
			if not protected_user_stat.has_key(protected):
				protected_user_stat[protected] = 0
			protected_user_stat[protected] += 1
			
			# save the uid of protected user
			if protected:
				protected_user_list.append(uid)
			
			# analyze default profile image
			if not default_profile_stat.has_key(default_img):
				default_profile_stat[default_img] = 0
			default_profile_stat[default_img] += 1
			
			user_stat += 1
			if (user_stat % 50000) == 0:
				print "processed %d th user" % user_stat
			
		result['protected_stat'] = protected_user_stat
		result['protected_list'] = protected_user_list
		result['default_profile_stat'] = default_profile_stat
		result['user_count'] = user_stat
		
		return result

if __name__ == '__main__':
	base_path = './data/'

	result = do_stats(base_path);
	result_file = open('result_2nd', 'w')
	result_file.write(str(result))
	result_file.close()
	
	print "processing finished!"
