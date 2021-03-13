from news import getNews
from flask import Flask, render_template, request 

# import json to load JSON data to a python dictionary 
import json 

# urllib.request to make a request to api 
import urllib.request 


app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/city', methods =['POST', 'GET']) 
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'mumbai'
    api = 'dcf3d7d0f1a4ec2f74db52f75aedfa41'
    try:
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city + '&appid=' + api).read() 
    except:
        city = 'mumbai'
        
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city + '&appid=' + api).read() 
        list_of_data = json.loads(source)
        data = { 
		"country_code": str(list_of_data['sys']['country']), 
		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']), 
		"temp": str(list_of_data['main']['temp']) + 'k', 
		"pressure": str(list_of_data['main']['pressure']), 
		"humidity": str(list_of_data['main']['humidity']), 
        "cityname": city,
        "temp_cel": str(round(list_of_data['main']['temp']-273.15,2))+'C'
	}
        return render_template('city.html', msg='City name invalid!', data=data)
    list_of_data = json.loads(source)
    data = { 
		"country_code": str(list_of_data['sys']['country']), 
		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']), 
		"temp": str(list_of_data['main']['temp']) + 'k', 
		"pressure": str(list_of_data['main']['pressure']), 
		"humidity": str(list_of_data['main']['humidity']), 
        "cityname": city,
        "temp_cel": str(round(list_of_data['main']['temp']-273.15,2))+'C'
	}
    print(data) 
    return render_template('city.html', data = data) 
@app.route('/news')
def news():
    titles,content,url,image,time=getNews()
    return render_template('news.html',titles=titles,content=content,url=url,image=image,time=time)
@app.route('/maps')
def maps():
    return render_template('maps.html')
@app.route('/temp_anomaly')
def temp_anomaly():
    return render_template('temp_anomaly.html')
@app.route('/air')
def air():
    return render_template('air.html')
@app.route('/rain')
def rain():
    return render_template('rain.html')
if __name__ == '__main__':
    app.run(debug = True)