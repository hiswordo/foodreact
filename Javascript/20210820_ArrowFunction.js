//----Arrow Functions----
// @link [Arrow Functions In JavaScript - Getting Started - YouTube](https://www.youtube.com/watch?v=prG68DQobbw) at 2021/8/20
// TODO @link [JavaScript Arrow Functions: Fat & Concise Syntax - SitePoint](https://www.sitepoint.com/javascript-arrow-functions/) at 2021/8/20
// function multiplyByTwo (num) { return num * 2 }
// const multiplyByTwo = function (num) { return num * 2 } //原本函式中的函式都是帶這個
// const multiplyByTwo = (num) => { return num * 2 } // 箭頭類似function本來意思
// const multiplyByTwo = num => { return num * 2 } //一個parameter()可省略
const multiplyByTwo = num => num * 2;  //! without return，就不需要{} 
//?? 甚麼時候可以保留{}，看起來是匿名就可以?
// ^ multiplyByTwo takes the parameter, num, and run in function (num*2)
console.log(multiplyByTwo(3));

// const result = [1, 2, 3, 4].map(multiplyByTwo);
// const result = [1, 2, 3, 4].map(function (num) { return num * 2 });
// const result = [1, 2, 3, 4].map((num) => { return num * 2 });
// 應用 //! 不能用this相關方式，function跟()=>{}，對於this來說，前者會自動binding所謂的this
// map & filter
/* const result = [1, 2, 3, 4].map(num => num * 2);
const array = [1, 2, 3, 4].filter(num => num % 2 === 0);
console.log(result);
console.log(array);
 */

