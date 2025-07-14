// Получить доступ к кнопке
const topBtn = document.querySelector(".go-top");

// Скроллинг окна
window.addEventListener("scroll", trackScroll);
// Реакция на нажатие
topBtn.addEventListener("click", goTop);


function trackScroll() {
    // положение от верхушки окна
    const scrolled = window.pageYOffset;
    console.log(scrolled);
    // высота окна браузера
    const wh = document.documentElement.clientHeight;
    // вышли за пределы одного экрана (прокрутили больше экрана)
    if (scrolled > wh) {
    //должна показаться кнопка
    topBtn.style.display = 'block';
    //topBtn.classList.add("go-top--show");
    } else {
    //или исчезает (убираем класс, где есть display:block)
    topBtn.style.display = 'none';
    }
}


function goTop() {
    //пока не вернулись наверх
    if (window.pageYOffset > 0) {
    //скроллим вверх
    window.scrollBy(0, -5000); // по Y на 28px в -
    setTimeout(goTop, 0); // рекурсивный вызов самой себя(goTop) через задержку(0)
    }
}
