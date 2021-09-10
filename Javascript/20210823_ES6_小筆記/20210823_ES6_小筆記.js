// @link [Day04【ES6 小筆記】箭頭函式 - 基礎使用範例（Arrow function ） - iT 邦幫忙一起幫忙解決難題，拯救 IT 人的一天](https://ithelp.ithome.com.tw/articles/10213501) at 2021/8/23

// ! 如果要直接 return 物件，必須在物件外面加上括號()，否則會報錯。
// 出現錯誤
// let myHome = () => { dog: 1, brother: "豪豪" };

// 正確寫法
// const myHome = () => ({ dog: 1, brother: '豪豪' });
// console.log(myHome());

// 當你需要物件的資料
const restaurant = {
  name: '那一天義法餐館',
  chef: '阿華師',
  price: 30,
  menu: {
    duck: '法式櫻桃鴨胸',
    pig: '噶瑪蘭黑豚',
    rice: '檸檬奶油煙燻鮭魚燉飯',
  },
};
// way 1
console.log(restaurant.name);
// way 2
let name = restaurant.name;
console.log(name);

// ----way 3 解構對應destructing----
// const { name, chef } = restaurant;
// console.log(name, chef);

// 輕鬆重新命名，讓排名變得很容易
const { rice: NO1, duck: NO2, pig: NO3 } = restaurant.menu;
console.log(NO1, NO2, NO3);

// 臨時增用的感覺，當沒其他地方需要他，也沒有要新增到原obj上時用吧
// const { soup = 'No soup today' } = restaurant;
// console.log(soup);
// console.log(restaurant.soup); // undefined

// 字串也可以拆解喔=>同數組解構
const please = '格幫我買飲料';
[a, b, c, d, e, f] = please;
console.log((a));

// 類似python的迴圈
const youtuber = ['洋蔥人', 'howhow', 'fred吃上癮', '啾啾鞋', '黃大謙'];
for (const name of youtuber) {
  console.log(name);
}

//! map() 方法使用起來跟 forEach() 方法非常類似，最大的區別就是 forEach() 會修改原本的陣列
const A = [9000, 8500, 5500, 6500];
const B = A.map((value) => value * 2);
console.log(B);

console.log(A);
A.forEach((value, index, array) => {
  array[index] = value * 2;
});
console.log(A);

// 寫的複雜一點的話，原本意思是這樣
