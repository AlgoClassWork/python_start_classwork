<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Банковские карты</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1>Банковские карты</h1>

    <div class="form">
        <h2>Добавить карту</h2>
        <label> Номер карты: </label>
        <input type="text" id="cardNumber" placeholder="4166 7099 6433 7822">
        <label> ФИО: </label>
        <input type="text" id="fullName" placeholder="Иван Иванов Иванович"> 
        <button id="addCardButton"> Добавить карту </button>
    </div>

    <div id="cardList">
        <h2>Ваши карты</h2>
    </div>

    <div class="transfer">
        <h2>Перевод между картами</h2>
        <label>С карты:</label>
        <select id="fromCard">
            <option value=""> Выберите карту </option>
        </select>
        <label>На карту:</label>
        <select id="toCard">
            <option value=""> Выберите карту </option>
        </select>
        <label>Сумма перевода:</label>
        <input type="number" id="transferAmount" placeholder="100">
        <button id="transferButton"> Перевести </button>
    </div>
    
    <script src="main.js"></script>
</body>
</html>
