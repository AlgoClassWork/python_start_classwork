const canvas = document.getElementById('gameCanvas')
const ctx = canvas.getContext('2d')

// Параметры платформы
const platformHeight = 10
const platformWidth = 80
const platformSpeed = 5
let platformX = (canvas.width - platformWidth) / 2

// Состояние клавиш
let rightPressed = false
let leftPressed = false

// Параметры мяча
const ballRadius = 10
let ballX = canvas.width / 2
let ballY = canvas.height / 2

// Обработчик событий нажатия
document.addEventListener('keydown', keyDownHandler, false)
document.addEventListener('keyup', keyUpHandler, false)

function keyDownHandler(e) {
    if (e.key == 'Right' || e.key == 'ArrowRight') {
        rightPressed = true
    } else if (e.key == 'Left' || e.key == 'ArrowLeft') {
        leftPressed = true
    }
}

function keyUpHandler(e) {
    if (e.key == 'Right' ||  e.key == 'ArrowRight') {
        rightPressed = false
    } else if (e.key == 'Left' || e.key == 'ArrowLeft') {
        leftPressed = false
    }
}

function updatePlatformPosition() {
    if (rightPressed && platformX < canvas.width - platformWidth) {
        platformX += platformSpeed
    } else if (leftPressed && platformX > 0) {
        platformX -= platformHeight
    }
}

function drawPlatform() {
    ctx.beginPath()
    ctx.rect(platformX, canvas.height - platformHeight - 10, platformWidth, platformHeight)
    ctx.fillStyle = 'black'
    ctx.fill()
    ctx.closePath()
}

function drawBall() {
    ctx.beginPath()
    ctx.arc(ballX, ballY, ballRadius, 0, Math.PI * 2)
    ctx.fillStyle = 'red'
    ctx.fill()
    ctx.closePath()
}

function draw() {
    ctx.clearRect(0, 0 , canvas.width, canvas.height)
    drawPlatform()
    drawBall()
    updatePlatformPosition()
}

setInterval(draw, 10)
