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
let ballSpeedX = 2
let ballSpeedY = 2

// Параметры блоков
const brickRowCount = 3
const brickColumnCount = 5
const brickWidth = 80
const brickHeight = 20
const brickPadding = 10
const brickOffsetTop = 30
const brickOffsetLeft = 30

// Массив блоков
const bricks = [] 
for (let c = 0; c < brickColumnCount; c++) {
    bricks[c] = []
    for (let r = 0; r < brickRowCount; r++) {
        bricks[c][r] = {x : 0, y : 0, status: 1}
    }
}

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

function updateBallPosition() {
    if (ballX > canvas.width || ballX < 0) {
        ballSpeedX = -ballSpeedX
    }
    if (ballY < 0) {
        ballSpeedY = -ballSpeedY
    }
    if (ballY > canvas.height - ballRadius - platformHeight && ballX > platformX && ballX < platformX + platformWidth) {
        ballSpeedY = -ballSpeedY
    }
    ballX += ballSpeedX
    ballY += ballSpeedY
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

function drawBricks () {
    for (let c = 0; c < brickColumnCount; c++) {
        for (let r = 0; r < brickRowCount; r++) {
            if (bricks[c][r].status == 1) {
                const brickX = (c * (brickWidth + brickPadding)) + brickOffsetLeft
                const brickY = (r * (brickHeight + brickPadding)) + brickOffsetTop
                bricks[c][r].x = brickX
                bricks[c][r].y = brickY
                ctx.beginPath()
                ctx.rect(brickX, brickY, brickWidth, brickHeight)
                ctx.fillStyle = 'green'
                ctx.fill()
                ctx.closePath()
            }
        }
    }
}

function draw() {
    ctx.clearRect(0, 0 , canvas.width, canvas.height)
    drawPlatform()
    drawBall()
    drawBricks()
    updatePlatformPosition()
    updateBallPosition()
}

setInterval(draw, 10)
