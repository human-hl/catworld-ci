const API_BASE = 'http://127.0.0.1:5000/api';

function openTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    document.querySelectorAll('.tab-button').forEach(button => {
        button.classList.remove('active');
    });
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
}

function displayError(elementId, error) {
    document.getElementById(elementId).innerHTML = `<p style="color: red;">Ошибка: ${error}</p>`;
}

// ================== ФУНКЦИИ ДЛЯ КОТИКОВ ==================
async function loadCats() {
    try {
        const response = await fetch(`${API_BASE}/cats`);
        if (!response.ok) {
            throw new Error(`Ошибка HTTP: ${response.status}`);
        }
        const cats = await response.json();
        displayCats(cats);
    } catch (error) {
        displayError('cats-list', error.message);
    }
}
async function handleCatForm() {
    const form = document.getElementById('add-cat-form');
    const formData = new FormData(form);
    const catData = Object.fromEntries(formData.entries());
    
    // Преобразуем возраст в число
    catData.age = parseInt(catData.age);

    try {
        console.log('Sending cat data:', catData);
        const response = await fetch(`${API_BASE}/cats`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(catData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Ошибка при добавлении котика');
        }

        const newCat = await response.json();
        alert(`Котик ${newCat.name} успешно добавлен!`);
        form.reset(); // Очистить форму
        loadCats(); // Перезагрузить список
    } catch (error) {
        alert(error.message);
    }
}

function displayCats(cats) {
    const table = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Имя</th>
                    <th>Порода</th>
                    <th>Возраст</th>
                    <th>Любимый корм</th>
                </tr>
            </thead>
            <tbody>
                ${cats.map(cat => `
                    <tr>
                        <td>${cat.id}</td>
                        <td>${cat.name}</td>
                        <td>${cat.breed}</td>
                        <td>${cat.age}</td>
                        <td>${cat.favorite_food}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;
    document.getElementById('cats-list').innerHTML = table;
}

document.getElementById('add-cat-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const catData = Object.fromEntries(formData.entries());
    catData.age = parseInt(catData.age);

    try {
        const response = await fetch(`${API_BASE}/cats`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(catData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Ошибка при добавлении котика');
        }

        const newCat = await response.json();
        alert(`Котик ${newCat.name} успешно добавлен!`);
        event.target.reset(); 
        loadCats(); 
    } catch (error) {
        alert(error.message);
    }
});

// ================== ФУНКЦИИ ДЛЯ КОРМА ==================
async function loadFood() {
    try {
        const response = await fetch(`${API_BASE}/foods`);
        if (!response.ok) throw new Error(`Ошибка HTTP: ${response.status}`);
        const food = await response.json();
        displayFood(food);
    } catch (error) {
        displayError('food-list', error.message);
    }
}

async function loadFoodByBrand() {
    const brand = document.getElementById('brand-filter').value;
    if (!brand) {
        alert('Введите бренд для поиска');
        return;
    }
    try {
        const response = await fetch(`${API_BASE}/foods/brand/${encodeURIComponent(brand)}`);
        if (!response.ok) throw new Error(`Ошибка HTTP: ${response.status}`);
        const food = await response.json();
        displayFood(food);
    } catch (error) {
        displayError('food-list', error.message);
    }
}

async function loadFoodByPrice() {
    const min = document.getElementById('min-price').value || 0;
    const max = document.getElementById('max-price').value || 10000; // Большое число

    try {
        const response = await fetch(`${API_BASE}/foods/price?min=${min}&max=${max}`);
        if (!response.ok) throw new Error(`Ошибка HTTP: ${response.status}`);
        const food = await response.json();
        displayFood(food);
    } catch (error) {
        displayError('food-list', error.message);
    }
}

async function loadFoodByRating() {
    const minRating = document.getElementById('min-rating').value;
    if (!minRating) {
        alert('Введите минимальный рейтинг');
        return;
    }
    try {
        const response = await fetch(`${API_BASE}/foods/rating/${minRating}`);
        if (!response.ok) throw new Error(`Ошибка HTTP: ${response.status}`);
        const food = await response.json();
        displayFood(food);
    } catch (error) {
        displayError('food-list', error.message);
    }
}

function displayFood(foods) {
    if (foods.length === 0) {
        document.getElementById('food-list').innerHTML = '<p>Ничего не найдено.</p>';
        return;
    }
    const table = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Название</th>
                    <th>Бренд</th>
                    <th>Цена</th>
                    <th>Рейтинг</th>
                </tr>
            </thead>
            <tbody>
                ${foods.map(food => `
                    <tr>
                        <td>${food.id}</td>
                        <td>${food.name}</td>
                        <td>${food.brand}</td>
                        <td>${food.price} руб.</td>
                        <td>${food.rating} / 5</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;
    document.getElementById('food-list').innerHTML = table;
}

document.addEventListener('DOMContentLoaded', () => {
    loadCats();
    loadFood();
});