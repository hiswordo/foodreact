// ----解構對應destructing----
// {}
/* 
1.需對應其屬性名稱，所以小心大小寫
2.變數不能事先宣告
3.如果解構為重寫變量，變量需用let定義，並注意新增()，有解構同時對應的感覺!(A、B交換值的概念)
 */
const Marry = {
    name: 'Marry Avis',
    age: 25,
    family: {
        father: 'Richard',
        mother: 'Norah',
        brother: 'Howard'
    }
}
// *不能事先宣告
// consta name = ''; 
// const { age, name } = Marry;
// console.log(name, age);

// *重寫變量，所以用let
// 但要用(重寫變量=誰的值)整個包起來，不然{}會被當作"代碼塊"而"非解構代碼"
let name = 'first name';
console.log(name);
// 若沒有()，形成{A, B} = {C.A, C.B}
// A = C.A, and then B = C.B 的感覺，跟無法 a=b, b=a，交換值的概念有點像
({ age, name } = Marry);
console.log(name, age);

// *重新命名變量，跟給予默認值(必須是原先undefined，null不行，其他蓋不過去)
const { father: f, mother = 'new mom', sister: s } = Marry.family;
console.log(f, mother, s); // Richard Norah undefined

//*數組解構-AB交換
let a = 10;
let b = 20;

//原本AB交換的方式
/* 
let temp = a;
a =  b;
b = temp;
console.log(a,b)  */

//現在方便許多
[a,b] = [b,a]
console.log(a,b)  

// *"..."的用法一定要是剩餘，後面不能有東西
const numbers = ['one', 'two', 'three', 'four'];
const [first, ...others] = numbers;
console.log(numbers);