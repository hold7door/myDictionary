import requests
import json
try:
	import MySQLdb

	database = MySQLdb.connect(user = "" , passwd = "" , db = "")               #Provide username, password and database name
	db = database.cursor()
	nodb = False
except ImportError as e:
		print ("MySQL client is not installed. Database access is not possible.")
		nodb = True

app_id = ""                                                                     # Provide API key and id
app_key = ""
language = 'en'



def lemmatron(word1):
	url1 =  'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + word1.lower()
	try:
		r = requests.get(url1 , headers = {'app_id' : app_id , 'app_key' : app_key})
		json_data = json.dumps(r.json())
		json_dic = json.loads(json_data)
		res = json_dic['results']
		return res[0]['lexicalEntries'][0]['inflectionOf'][0]['id']
		
	except ValueError :
		print ("Word not found.")
		return ''

def meaning(result_dic , wrd):
	global nodb
	res = result_dic['results']
	defin = res[0]['lexicalEntries'][0]['entries'][0]['senses'][0]
	word_type = res[0]['lexicalEntries'][0]['lexicalCategory']
	examples = []
	print ("Type: {0}".format(word_type))
	print ("Meaning : {0} ".format(defin['meanings'][0]))
	print ("Examples :")
	if nodb == False:
		db.execute(""" insert into words (word , meaning ,type) values (%s , %s , %s)""" , (wrd , defin['meanings'][0] , word_type))
		database.commit()
	for example in defin['examples']:
		examples.append(example['text'])
		print (example['text'])
	if nodb == False:
		db.execute(""" update words set example = %s where word = %s """ , (examples[0] , wrd))
		database.commit()
if __name__  == "__main__":
	while True:
		word = str(input("Enter Word: "))
		try:
			word_id = lemmatron(word)
			if len(word_id) == 0:
				print ("Check Word and try again.")
			else:
				if nodb == False:
					db.execute("""Select * from words where word = %s""" , (word_id,));
					word = db.fetchall()
				else:
					word = ""
				if len(word):
					print ("[*]Fetching from database")
					print ("Meaning : {0}" . format(word[0][1]))
					print ("Examples : {0} ".format(word[0][2]))
					print ("Type : {0}".format(word[0][3]))
				else:	
					print ("[*]Sending Get for word")
					url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
					r = requests.get(url , headers = {'app_id' : app_id , 'app_key' : app_key})
					json_data = json.dumps(r.json())
					json_dic = json.loads(json_data)
					meaning(json_dic , word_id)
			
		except Exception as e:
			print (e)
