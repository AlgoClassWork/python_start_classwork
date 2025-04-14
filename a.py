from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler,
                          MessageHandler, ContextTypes, filters)

board = [ '⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜' ] 

def check_winner():
    win_combo = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #Горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8], #Вертикали
        [0, 4, 8], [2, 4, 6], #Диагонали
    ]
    for combo in win_combo:
        a, b, c = combo 
        if board[a] == board[b] == board[c] and board[a] != '⬜':
            return board[a]
    return None

def check_draw():
    return all(cell != '⬜' for cell in board)
        
def format_bord():
    return f'{board[0]}   {board[1]}   {board[2]}\n' \
           f'\n' \
           f'{board[3]}   {board[4]}   {board[5]}\n' \
           f'\n' \
           f'{board[6]}   {board[7]}   {board[8]}\n' 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_player, board
    current_player = '❌'
    board = [ '⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜' ] 
    await update.message.reply_text('Игра началась! Ходит ❌. Пиши номер клетки (0-8):')
    await update.message.reply_text( format_bord() )

async def move(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_player
    try:
        pos = int(update.message.text) 

        if 0 <= pos <= 8 and board[pos] == '⬜':
            board[pos] = current_player
            await update.message.reply_text( format_bord() )

            winner = check_winner()
            if winner:
                await update.message.reply_text(f'{winner} победил! Напиши /start для новой игры')

            if check_draw():
                await update.message.reply_text('Ничья напиши /start для новой игры')

            current_player = '⭕' if current_player == '❌' else '❌'
        else:
            await update.message.reply_text('Клетка занята или вы написали неккоректное число')
    except:
        await update.message.reply_text('Пиши числа от 0 до 8')

app = ApplicationBuilder().token('7137462050:AAHh2d2TVPe3xS88xQ1vkZ23jax9usVgqIQ').build()
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT, move))
app.run_polling()
