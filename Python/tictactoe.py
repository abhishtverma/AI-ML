from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'tic-tac-toe-secret'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Initialize or reset the board
def init_board():
    return ['' for _ in range(9)]

# Check for win conditions
def check_winner(board):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if '' not in board:
        return 'Tie'
    return None

@app.route('/')
def index():
    if 'board' not in session:
        session['board'] = init_board()
        session['turn'] = 'X'
        session['winner'] = None
    return render_template('index.html', board=session['board'], turn=session['turn'], winner=session['winner'])

@app.route('/move/<int:cell>')
def move(cell):
    if session['winner'] or session['board'][cell]:
        return redirect(url_for('index'))

    session['board'][cell] = session['turn']
    session['winner'] = check_winner(session['board'])
    if not session['winner']:
        session['turn'] = 'O' if session['turn'] == 'X' else 'X'
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
