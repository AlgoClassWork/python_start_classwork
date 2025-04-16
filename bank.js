<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Банк</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="form">
        <h3>Добавить</h3>
        <input id="name" placeholder="Имя">
        <button class="button">Добавить</button>
    </div>

    <div class="transfer">
        <h3>Перевод</h3>
        <input id="from" placeholder="От кого">
        <input id="to" placeholder="Кому">
        <input id="sum" placeholder="Сумма">
        <button class="btn">Перевести</button>
    </div>

    <div class="client">
        <h3>Клиенты</h3>
    </div>

    <script src="main.js"></script>
    
</body>
</html>


body {
    font-family: sans-serif;
}

.form, .transfer {
    border: 1px solid lightgray;
    padding: 10px;
    margin: 10px 0;
}

input, button {
    padding: 5px;
    margin: 5px;
}


class Client {
    constructor(name) {
        this.name = name
        this.balance = 1000
    }

    card() {
        return '<div class="card">' + this.name + ' ' + this.balance + '</div>'
    }
}

let clients = []

function add() {
    let name = document.getElementById('name').value
    clients.push( new Client(name) )
    show()
}

function show() {
    let list = '<h3>Клиенты</h3>'
    for ( let client of clients ) {
        list += client.card()
    }
    document.querySelector('.client').innerHTML = list
}

function transfer() {
    let client_from = document.getElementById('from').value 
    let client_to = document.getElementById('to').value 
    let client_sum = document.getElementById('sum').value 
    let otpravitel, poluchatel
    for (let client of clients) {
        if (client.name == client_from) otpravitel = client
        if (client.name == client_to) poluchatel = client
    }
    otpravitel.balance -= client_sum 
    poluchatel.balance += +client_sum
    show()
}

let button = document.querySelector('.button')
let btn = document.querySelector('.btn')
button.addEventListener('click', add)
btn.addEventListener('click', transfer)
