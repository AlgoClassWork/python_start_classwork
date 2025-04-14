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








/* Общие стили */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f2f4f8;
    margin: 0;
    padding: 20px;
    color: #333;
}

/* Заголовок */
h1 {
    text-align: center;
    color: #2a2a2a;
    margin-bottom: 30px;
}

/* Универсальный блок */
.form, .transfer, #cardList {
    background: #fff;
    padding: 25px;
    margin: 20px auto;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    max-width: 600px;
}

/* Заголовки секций */
.form h2, .transfer h2, #cardList h2 {
    margin-top: 0;
    color: #3a3a3a;
}

/* Метки и инпуты */
label {
    display: block;
    margin-top: 15px;
    margin-bottom: 5px;
    font-weight: 500;
}

input, select {
    width: 100%;
    padding: 12px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 16px;
    box-sizing: border-box;
}

input:focus, select:focus {
    border-color: #5a9cf2;
    outline: none;
    box-shadow: 0 0 0 3px rgba(90, 156, 242, 0.2);
}

/* Кнопки */
button {
    background-color: #5a9cf2;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.2s ease;
    margin-top: 10px;
}

button:hover {
    background-color: #3f82db;
}

/* Список карт (будешь добавлять сюда карточки) */
#cardList .card {
    background-color: #eaf0f7;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

