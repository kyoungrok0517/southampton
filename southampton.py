from datetime import datetime
import os
import sys
import json
import urlparse

base_path = './data/'

def parse_data():
	for filename in os.listdir(base_path):
		f = open(base_path + filename)
		
		data_list = list()
		
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
			con_dict = eval(content)				# content in dictionary format
			data_list.append(con_dict)

		return data_list
	
# TODO: we need to normalize created_at & location
def analyze_data(data_list):
	prot_stat = dict()
	geo_stat = dict()
	created_stat = dict()
	loc_stat = dict()
	url_stat = dict()
	
	# result of analysis
	result = dict()
	
	for data in data_list:
#		description = unicode(data['description'])
		protected = unicode(data['protected'])
		geo_enabled = unicode(data['geo_enabled'])
		created_at = unicode(data['created_at'])
		location = unicode(data['location'])
		url_base = urlparse.urlparse(unicode(data['url'])).netloc
		
#		print datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")
#		print created_at
		
		# analyze protected
		if not prot_stat.has_key(protected):
			prot_stat[protected] = 0
		prot_stat[protected] += 1

		# analyze geo_enabled
		if not geo_stat.has_key(geo_enabled):
			geo_stat[geo_enabled] = 0
		geo_stat[geo_enabled] += 1
		
		# analyze created_stat
		
		# analyze location
		if not loc_stat.has_key(location):
			loc_stat[location] = 0
		loc_stat[location] += 1
		
		# analyze url
		if not url_stat.has_key(url_base):
			url_stat[url_base] = 0
		url_stat[url_base] += 1
		
	result['protected'] = prot_stat
	result['geo_enabled'] = geo_stat
	result['created_at'] = created_stat
	result['location'] = loc_stat
	result['url'] = url_stat
	result['user_count'] = len(data_list)
	
	return result
		
if __name__ == '__main__':
	data_list = parse_data();
	analysis = analyze_data(data_list)
	
	print analysis
