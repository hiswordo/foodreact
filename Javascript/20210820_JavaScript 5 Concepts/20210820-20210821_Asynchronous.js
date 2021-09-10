// @link [5 JavaScript Concepts You HAVE TO KNOW - YouTube](https://www.youtube.com/watch?v=a00NRSFgHsY) at 2021/8/20
/* 
1. Equality
2. Asynchronous Js
3. Error Handling
4. Es6 Syntax
5. Array Methods 
*/
const fs = require('fs');
const fetch = require('node-fetch');

//----2. Asynchronous Js-----
// @link [Asynchronous JavaScript in ~10 Minutes - Callbacks, Promises, and Async/Await - YouTube](https://www.youtube.com/watch?v=670f71LTWpM) at 2021/8/20
//----CallBacks----
// 20210820_ArrowFunction.js
// @link [[JavaScript] 一次搞懂同步與非同步的一切：待會叫你 — 回呼函式(Callback Function) | by itsems | itsems_frontend | Medium](https://medium.com/itsems-frontend/javascript-callback-function-993abc2c0b42) at 2021/8/21
// def: A callback is a function passed as an argument to another function.
// Callback function 是在"指定時機"才觸發的 function
/* function sayHi(name, mycallback){
    mycallback(name);
}

const callwho = who => console.log(`Hello, ${who}`);
// const callwho = who => console.log("Hello, "+who);
sayHi('emma',callwho); */

// @link [什麼是Callback函式 (Callback function) | by Jun | appxtech | Medium](https://medium.com/appxtech/%E4%BB%80%E9%BA%BC%E6%98%AFcallback%E5%87%BD%E5%BC%8F-callback-function-3a0a972d5f82) at 2021/8/21
/* 
CallBack的必要條件
1、讓函式成為另一個函式的參數
2、讓函式控制參數函式的執行時機

CallBack function的好處，在於
1、確保程式時機與關連
2、便於維護
 */

// callback function 指的是這一段 ()=>{}
// *nested setTimeout
/*
setTimeout(()=>{
    console.log('3')
    setTimeout(()=>{
        console.log('2')
        setTimeout(()=>{
            console.log('1')
        },1000);
    },1000);
},1000); */

// *button event handler in browser Js
// const btn;
// btn.addEventListener('click',()=>{})

//----error first callback (ex非同步讀取檔案)----
// 20210822_require.js
// @link [Day8 - Node.js 檔案系統 - iT 邦幫忙一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10185422) at 2021/8/20
/* fs.readFile('./Javascript/20210820_JavaScript 5 Concepts/test.txt', function (err, data) {
    if (err) throw err; // TODO 
    console.log(data.toString()); // ?? toString()會自動encoding嗎?
}); */

// ! fs.read 用絕對路徑真的很麻煩
/* fs.readFile('./Javascript/20210820_JavaScript 5 Concepts/test.txt', function (err, data) {
    if (err) {
        console.log('ERROR');
        console.log(err);
    }else {
        console.log('GOT DATA');
        console.log(data.toString());
    }
}); */

/* fs.readFile('./Javascript/20210820_JavaScript 5 Concepts/test2.txt', encoding='utf-8', (err, data) => {
    if (err) throw err;
    console.log(data);
}); */

//----Promises----
// @link [ES6 Promise詳細用法（我見過最簡潔優秀的文章） - IT閱讀](https://www.itread01.com/content/1546338963.html) at 2021/8/20
// @link [JavaScript Promise 全介紹 | 卡斯伯 Blog - 前端，沒有極限](https://wcc723.github.io/development/2020/02/16/all-new-promise/) at 2021/8/20
/*
// 開始
// 程式碼結束
// 非同步事件
console.log('開始');
setTimeout(() => { console.log('非同步事件'); }, 0);
console.log('程式碼結束');
 */

/* function promise(num) {
    return new Promise((resolve, reject) => {
      num ? resolve(`${num}, 成功`) : reject('失敗');
    });
  }

  promise(1)
  .then(success => {
    console.log(success);
    return promise(2);
  })
  .then(success => {
    console.log(success);
    return promise(0); // 這個階段會進入 catch
  })
  .then(success => {   // 由於上一個階段結果是 reject，所以此段不執行
    console.log(success);
    return promise(3);
  })
  .catch(fail => {
    console.log(fail);
  }) */

//----
// *always have success path and fail path
/* 
//?? resolve and reject的運作呢?
const myPromise = new Promise((resolve, reject) => {
    // 隨機 0 or 1
    const rand = Math.floor(Math.random() * 2);
    if (rand === 0) {
        resolve();
    } else {
        reject();
    }
})

// ?? 甚麼快捷鍵，可以讓.then .catch直接移動到下兩行呢?
myPromise
    .then(() => console.log('Success'))
    .catch(() => console.log('Somthing went wrong')) */

// *fs readFile with promise
// ! 這樣用，都不需要去定義甚麼東西耶，有點厲害喔
/* fs.promises
    .readFile('./Javascript/20210820_JavaScript 5 Concepts/test.txt', encoding = 'utf-8')
    .then((data) => console.log(data))
    .catch((err) => console.log(err)); */

// *fetch with promises
/* fetch('https://pokeapi.co/api/v2/pokemon/ditto')
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((err) => console.log(err)); */

// async function建立後，就可以await了!
// *readfile
/* const loadFile = async () => {
    try {
        const data = await fs.promises.readFile('./Javascript/20210820_JavaScript 5 Concepts/test.txt', encoding = 'utf-8');
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}
loadFile();
 */

// fetchPokemon
const fetchPokemon = async (id) => {
    const res = await fetch('https://pokeapi.co/api/v2/pokemon/'+id);
    const data = await res.json();
    console.log(data)
}
fetchPokemon(2);

// 補充
// @link [JavaScript Promise 漂亮的串接非同步事件 - YouTube](https://www.youtube.com/watch?v=QVAWqE-R0Ok) at 2021/9/2