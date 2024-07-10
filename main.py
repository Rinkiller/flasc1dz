from flask import Flask, render_template


app = Flask(__name__)

@app.get('/')
def root():
    context = {'zagolovoc':['Это  ГЛАВНАЯ   страница  '],'poem': [
                        'эта страница идет вперед всех  ',
                        ' эту страницу в конце ждет успех ']}
    return render_template('index.html', **context)

@app.get('/page-1/')
def page1():
    context = {'zagolovoc': ['ОБУВЬ'],'poem': [
                        'бла бла бла  ',
                        ' про обувь ']}
    return render_template('index.html', **context)

@app.get('/page-2/')
def page2():
    context = {'zagolovoc': ['Одежда'],'poem': [
                        'бла бла бла  ',
                        ' про одежду ']}
    return render_template('index.html', **context)

@app.get('/page-3/')
def page3():
    context = {'zagolovoc': ['Куртка'],'poem': [
                        'бла бла бла  ',
                        ' про куртки ']}
    return render_template('index.html', **context)

if __name__=='__main__':
    app.run(debug=True)