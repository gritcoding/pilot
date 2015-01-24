import web
import datetime

# run with sudo to run on port 80 and use GPIO

urls = ('/', 'index', '/survey', 'survey')
render = web.template.render('templates/')

class survey:
        def GET(self):
                return render.survey()

class index:
        def GET(self):
                i = web.input(enter=None)
                #if i.enter=='allow':
                        # do something
                #elif i.enter=='deny':
                        # do something else

                date = datetime.datetime.now().ctime()
                hour = datetime.datetime.now().hour
                
                return render.index(i.enter, date, hour)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
