from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')                                             
@app.route('/content')
def content_page() -> 'html':
    return render_template('content.html',
                           the_title='Конструкция Титаника')
                               
@app.route('/deck')                    
def deck() -> 'html':
    return render_template('deck.html',
                           the_title='Палуба')

@app.route('/bulkheads')                    
def bulkheads() -> 'html':
    return render_template('bulkheads.html',
                           the_title='Переборки')

@app.route('/double_buttom')                    
def double_buttom() -> 'html':
    return render_template('double_buttom.html',
                           the_title='Двойное дно')

@app.route('/office_space')                    
def office_space() -> 'html':
    return render_template('office_space.html',
                           the_title='Служебные помещения')

@app.route('/pipes')                    
def pipes() -> 'html':
    return render_template('pipes.html',
                           the_title='Трубы')

@app.route('/masts')                    
def masts() -> 'html':
    return render_template('masts.html',
                           the_title='Мачты')

if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

