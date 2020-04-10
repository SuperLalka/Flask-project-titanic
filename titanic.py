from flask import Flask, render_template, escape
from post_iteration import post_iteration
app = Flask(__name__)

@app.route('/')                                             
@app.route('/post')
def content_page() -> 'html':
    contents = post_iteration()
    return render_template('post.html',
                           the_title='Конструкция Титаника',
                           the_contents = contents)
                               
@app.route('/post/deck')
def deck() -> 'html':
    return render_template('post/deck.html',
                           the_title='Палуба')

@app.route('/post/bulkheads')                    
def bulkheads() -> 'html':
    return render_template('post/bulkheads.html',
                           the_title='Переборки')

@app.route('/post/double_buttom')                    
def double_buttom() -> 'html':
    return render_template('post/double_buttom.html',
                           the_title='Двойное дно')

@app.route('/post/office_space')                    
def office_space() -> 'html':
    return render_template('post/office_space.html',
                           the_title='Служебные помещения')

@app.route('/post/pipes')                    
def pipes() -> 'html':
    return render_template('post/pipes.html',
                           the_title='Трубы')

@app.route('/post/masts')                    
def masts() -> 'html':
    return render_template('post/masts.html',
                           the_title='Мачты')

if __name__ == '__main__':                      #проверка на локальность
    app.run(debug=True)

