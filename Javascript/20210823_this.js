// @link [this 的值到底是什么？一次说清楚 - 知乎](https://zhuanlan.zhihu.com/p/23804247) at 2021/8/23
// @link [淺談 JavaScript 頭號難題 this：絕對不完整，但保證好懂](https://blog.techbridge.cc/2019/02/23/javascript-this/) at 2021/8/23

// ----脫離了物件的 this----
// function hello() {
//   console.log(this);
// }
// hello(); // object [global]

/*
「脫離了物件，this 的值就沒什麼意義」。
1.嚴格模式底下就都是undefined (話說airbnb eslint會把'use strict';直接拿掉)
2.非嚴格模式，瀏覽器底下是window
3.非嚴格模式，node.js 底下是global
這就是"預設綁定"，在沒意義的情況底下就會有個預設值，嚴格模式就是undefined，非嚴格模式底下就是全域物件。
*/

// ----3種等價呼叫語法----
// call 跟 apply 的差別，一個跟平常呼叫 function 一樣，差別都只是傳入參數的差別，一個用 array 包起來。
/* 'use strict';
function hello(a, b) {
  console.log(this, a, b);
}

hello(1, 2); // undefined 1 2, this自動被當作undefined參數傳進去
hello.apply(undefined, [1, 2]); // undefined 1 2
hello.call(undefined, 1, 2); // undefined 1 2 (這種調用形式，才是正常調用形式) */

// ----轉換代碼----
/* function func() {
  console.log(this);
}

func.call(undefined); // 可以簡寫為 func.call()
func.call()
func.call('context') // [String: 'context'] => String {"context"}
 */
// 按理說列印出來的 this 應該就是 undefined 了吧，但是瀏覽器裡有一條規則：
// 如果你傳的 context 是 null 或 undefined，那麼 window 物件就是預設的 context（嚴格模式下預設 context 是 undefined）
// 所以當你需要this傳到別的物件，把context改名就好了

// ----obj.child.method（p1， p2） 的 this 如何確定----
//! obj.foo(); === obj.foo.call(obj);
const obj = {
  foo() {
      console.log(this);
  },
};

obj.foo(); // { foo: [Function: foo] }
obj.foo.call(obj); // 等價轉換代碼

// ----經常面試題目----
const obj = {
  foo() {
    console.log(this);
  },
};

const bar = obj.foo;
obj.foo(); // 則是obj.foo.call(obj)，this 就是 obj
bar(); // bar.call(), no context, this=undefined, 瀏覽器轉this=window obj
// 等價於 obj.foo.call(windows obj) = obj.foo.call();
// obj.foo.call()

// *所以說
// obj.foo() // 打印出的 this 是 obj
// bar() // 打印出的 this 是 window

// ----[ ] 語法補充----
function fn() { console.log(this); }
const fn2 = 30;
const arr = [fn, fn2];
arr[0](); // this=? => 對應剛剛的child.method，就類似於arr.0.call(arr)的概念
// 所以會得到array, [ [Function: fn], 30 ]
// 其他想法:
/*  arr[0]（）陣列其實就是個物件，對象裡面有函數。與obj.foo（）同
所以obj.foo（）的this是obj
arr[0]（）的this自然就是arr
 */

// ----箭頭函數----
// 實際上箭頭函數里並沒有 this，直接把它當作箭頭函數外面的 this 即可。

// ----總結----
// ! this 就是你 call 一個函數時，傳入的第一個參數。 （請務必背下來「this 就是 call 的第一個參數」）
// ! 如果你的函數調用形式不是 call 形式，請按照「轉換代碼」將其轉換為 call 形式。

// ----三種可以改變 this 的值的方法----
/* class Car {
  hello() {
    console.log(this);
  }
}

const myCar = new Car();
myCar.hello(); // myCar instance Car {}
myCar.hello.call('yaaaa'); // yaaaa

'use strict';
function hello() {
  console.log(this)
}

const myHello = hello.bind('my')
myHello() // my

function hello() {
  console.log(this);
}

hello.call(123); // 轉成 object [Number: 123]
const myHello = hello.bind('my');
myHello(); // 轉成 object [String: 'my']

 */
