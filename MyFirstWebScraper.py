from bs4 import BeautifulSoup
from urllib2 import urlopen

base_url="http://www.neighborhoodscout.com/"
cities=["ok/ardmore","ga/atlanta","md/baltimore","ny/buffalo","oh/cleveland",
		"mi/detroit","mo/ferguson","tx/frisco","ca/glendale","ca/irvine",
		"tn/memphis","il/naperville","ca/oakland","ca/sunnyvale"]

# Retrieve text from all "td" tags 
td_tags=soup.find_all("td")  # Alert! we would have td tags with descendant tags
data=[td_tag.string for td_tag in td_tags] 

selected_features=["POPULATION","WHITE","BLACK OR AFRICAN AMERICAN","ASIAN",
		"HISPANIC OR LATINO (OF ANY RACE)","18 TO 24","65 YEARS AND OVER",
		"MEDIAN HOUSEHOLD INCOME","PER CAPITA INCOME",
		"INDIVIDUALS BELOW POVERTY LEVEL","HIGH SCHOOL GRADUATES",
		"COLLEGE GRADUATES","FOREIGN BORN"]
testing=dict{}
testing={feature_name:[] for feature_name in selected_features}

# Pinpoint the indices of all selected features 
feature_value_indice=[data.index(feature_name)+1 for feature_name in selected_features]
# Assgin feature values
for feature_value_index in feature_value_indice:
	feature_value=data[feature_value_index]
	feature_name=data[feature_value_index-1]
	testing[feature_name].append(feature_value)

# 