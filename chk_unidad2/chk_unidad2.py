from flask import Flask, render_template, request, redirect
from formulas import presion, caudal

app = Flask(__name__)


@app.route('/')
def hello_world() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Calcular')


@app.route('/formulas', methods=['POST'])
def con() -> 'html':
    l = int(request.form['l'])
    m = int(request.form['m'])
    t = int(request.form['t'])
    title = 'Aqui esta el resultado'
    result = float(presion(l, m, t))
    return render_template('result.html',
                           the_title=title,
                           the_l=l,
                           the_m=m,
                           the_t=t,
                           the_result=result, )


if __name__ == '__main__':
    app.run()
