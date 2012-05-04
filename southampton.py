from datetime import datetime
import os
import sys
import json
import urlparse

base_path = './data/'

def do_stats():
	prot_stat = dict()
	geo_stat = dict()
#	created_stat = dict()
	url_stat = dict()
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
			
			# extract fields
			protected = unicode(data['protected'])
			geo_enabled = unicode(data['geo_enabled'])
#			created_at = unicode(data['created_at'])
			location = unicode(data['location'])
			url_base = urlparse.urlparse(unicode(data['url'])).netloc
			
			# analyze protected
			if not prot_stat.has_key(protected):
				prot_stat[protected] = 0
			prot_stat[protected] += 1

			# analyze geo_enabled
			if not geo_stat.has_key(geo_enabled):
				geo_stat[geo_enabled] = 0
			geo_stat[geo_enabled] += 1

			# analyze location
#			if not loc_stat.has_key(location):
#				loc_stat[location] = 0
#			loc_stat[location] += 1
			
			# analyze url
			if not url_stat.has_key(url_base):
				url_stat[url_base] = 0
			url_stat[url_base] += 1
			
			# count user
			user_stat += 1
			if (user_stat % 10000) == 0:
				print "processed %d th user" % user_stat
			
	result['protected'] = prot_stat
	result['geo_enabled'] = geo_stat
#	result['created_at'] = created_stat
#	result['location'] = loc_stat
	result['url'] = url_stat
	result['user_count'] = user_stat
	
	return result
		
if __name__ == '__main__':
	result = do_stats();
	
	result_file = open('result', 'w')
	result_file.write(str(result))
	result_file.close()
	
	print "processing finished!"
