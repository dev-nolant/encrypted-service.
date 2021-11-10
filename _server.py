from flask import Flask, render_template, request
from os import walk
import shutil, os
import convertName as cv
previous = ""
app = Flask(__name__)
print("request.referrer")
@app.route('/')
def home():
    return render_template('home.html')

# CR handler
@app.route('/cr')
@app.route('/cr/')
def cr_default():
    return render_template('home.html')

@app.route('/create_room/<name>/<users>',methods=['GET'])
def create_room(name=None, users=None):
    if name is None or name.startswith('home') or users is None:
        return "404", 404
    else:
        try:
            if os.path.exists("specifications\\"+name) != True:
                container = open("specifications\\"+name, "w+")
                untapped_list = cv.pcallc(name.replace(' ', ''))
                shutil.copy2("templates\chat_template.html", "templates\\"+str(untapped_list[0])+".html")
            else:
                return "400", 400
            container.write(users)
            container.close()
            return str(untapped_list[0])
        except IndexError:
            return "400", 400
        except Exception as e:
            return "nononononnoo", 418

# PAGE handler
@app.route('/cr/<name>')
def cr(name=None):
    filenames = next(walk("templates"))[2]
    if name is None or name.startswith('home'):
        return render_template('home.html')
    else:
        if str(name)+".html" in filenames:
            return render_template(str(name)+".html", share_url = "URL FOR CHAT ROOM: "+ str(request.base_url))
        else:
            return render_template('home.html')

@app.route('/cr/<name>/<uid>/<message>', methods=['GET', 'POST'])
def cr_chate(name=None, message=None, uid=None):
    if request.method == 'POST':
        if name is None or name.startswith('home') or message is None or uid is None:
            return render_template('home.html')
        else:
            reading = open("specifications\%s"%name, "r").read()
            if uid in reading.split(";"):
                if message == "dl":
                    os.remove("templates\\"+name+".html")
                    os.remove("specifications\\"+name)
                    return "done"
                else:
                    write = open("templates\\"+name+".html", "w+")
                    write.write(uid + ": " + message)
                    write.close()
                    return render_template("templates\\"+name+".html")
            else:
                return render_template('home.html')
    elif request.method == 'GET':
        if name is None or name.startswith('home') or uid is None:
            return render_template('home.html')
        else:
            string = "specifications\\"+name
            reading = open(string.replace("\\\\", "\\"),"r").read()
            if uid in reading.split(";"):
                return render_template("templates\\"+name+".html")
            else:
                return render_template('home.html')
if __name__ == '__main__':
    app.run(debug='True')
# run our Flask app