
// @link [2 - ES6 : let vs const 關鍵字 - YouTube](https://www.youtube.com/watch?v=qjHNdaf3cpE&list=PLCRqr1mERvdJ0IZMD1U4oSB7k0gyAjyIx&index=2) at 2021/8/22
//----var----
// var: Function Level Scope (可以重複定義，function外不能存取)
// let、const: 塊級作用域 (Block Level Scope)(if(){let...}裡面使用)
// function外不能存取

// *var 可以重複定義覆蓋的，還會蓋到windows函數等麻煩事情出現
var price = 350;
var price = 700;
price = 100;
console.log(price);

let price2 = 770;
price2 = 300; //*可重新賦值
console.log(price2);

const price3 = 300;
//! price3 = 400; //不可重新賦值
console.log(price3);

// *函數內的定義皆不能被外面用 //? 以前var好像可以
function discount() {
    var newPrice = price * 0.6;
    console.log(newPrice);
    let newPrice2 = price2 * 0.6;
    console.log(newPrice2);
    const newPrice3 = price3 * 0.6;
    console.log(newPrice3);
}
discount();
console.log(newPrice); //undefined，後面程式碼還可以執行，因為前面還是會自動加一行var newPrice;
//! console.log(newPrice2);
//! console.log(newPrice3);

// *只有var在block外還可以用
const numck = 10
if (numck > 0) {
    var newPrice = price * 0.6;
    console.log(newPrice);
    let newPrice2 = price2 * 0.6;
    console.log(newPrice2);
    const newPrice3 = price3 * 0.6;
    console.log(newPrice3);
}
console.log("newPrice: " + newPrice);
//! console.log(newPrice2);
//! console.log(newPrice3);

// 雖說const不變的，但物件的話，還是有可以變的地方
const person = {
    name: 'Jelly',
    age: 20
}
person.name = 'Ali';
person.age = 30;
person.music = 'west';
console.log(person);

//! 要用出生的名字才能freeze屬性
const Jelly = Object.freeze(person);
// 全都無法在改變了
// person.name = 'John';
// person.age = 40;
// person.like = 'basketball'; 
console.log(person);

//! let能讓for迴圈維持在當前的i

//! const能讓{}內的值，不被外面使用

//----Temporal Dead Zone (TDZ) 暫時性死區----
//! 常見問題 - 若變數尚未定義就被用到
console.log(color);
var color = 'green';
//^ 上述等同於下述
var color;
console.log(color);
color = 'green';