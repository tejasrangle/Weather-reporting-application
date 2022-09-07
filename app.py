from flask import *
app = Flask(__name__)

@app.route("/")
def weather_info():
    return render_template("weather.html")

@app.route("/find",methods=["POST"])
def weather_info_find():
    city=request.form["city"]
    city1=city+"+weather"
    import requests
    from bs4 import BeautifulSoup
    headers = {'User-Agent': 'Mo|zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r=requests.get(f"https://www.google.com/search?q={city1}&hl=en&sxsrf=ALiCzsbNreZq8gddk3FEHU1IuV39st4qKQ%3A1657693604994&source=hp&ei=pGXOYuKSOf3x4-EPtJeJEA&iflsig=AJiK0e8AAAAAYs5ztKn8kAzaFJnelxCeUrZ4cElPImKV&oq=m&gs_lcp=Cgdnd3Mtd2l6EAEYADIMCCMQJxCdAhBGEIACMgQIIxAnMgQIIxAnMgUILhCRAjILCAAQgAQQsQMQgwEyBAguEEMyCwguEIAEELEDEIMBMhEILhCABBCxAxCDARDHARDRAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBOgcIIxDqAhAnUPQKWPQKYIcaaABwAHgBgAHhBogBkRCSAQU1LTIuMZgBAKABAbABCg&sclient=gws-wiz",headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")
    location = soup.find_all('div',attrs={'class':"wob_loc q8U8x"})[0].getText().strip()
    time = soup.find_all('div',attrs={'class':"wob_dts"})[0].getText().strip()
    info = soup.find_all('div',attrs={'class':"wob_dcp"})[0].getText().strip()
    temperature = soup.find_all('div',attrs={'class':"vk_bk TylWce SGNhVe"})[0]
    temperature1=temperature.find("span").getText()
    t=[location,time,info,temperature1]
    return render_template("show.html",res=t)

if __name__ =="__main__":
    app.run(debug=True)
