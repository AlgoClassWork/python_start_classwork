from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler,
                          MessageHandler, ContextTypes, filters)

board = [ '⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜','⬜' ] 


def format_bord():
    return f'{board[0]}   {board[1]}   {board[2]}\n' \
           f'\n' \
           f'{board[3]}   {board[4]}   {board[5]}\n' \
           f'\n' \
           f'{board[6]}   {board[7]}   {board[8]}\n' 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_player
    current_player = '❌'
    await update.message.reply_text('Игра началась! Ходит ❌. Пиши номер клетки (0-8):')
    await update.message.reply_text( format_bord() )

async def move(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_player
    pos = int(update.message.text) 
    if 0 <= pos <= 8 and board[pos] == '⬜':
        board[pos] = current_player
        await update.message.reply_text( format_bord() )

    current_player = '⭕' if current_player == '❌' else '❌'

app = ApplicationBuilder().token('ВАШ ТОКЕН').build()
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT, move))
app.run_polling()
