
// for_of_循環
const fruits = ['Apple', 'Banana', 'Pineapple', 'lemon'];

// ----四種循環比較----
// 1st: For循環
// for (i = 0; i < fruits.length; i++){
//     console.log(fruits[i]);
// }

// *2nd: forEach - 不能中斷
// fruits.forEach(fruit => console.log(fruit))

// 3rd: for in (記得它循環的是屬性名，非屬性質)
// ?? 等號問題: 這裡得用兩個==，不能用===?
for (fruit in fruits){
    if (fruit == 3){
        break;
    }
    console.log(`${fruit}: ${fruits[fruit]}`)
}

// 4th: for of
for (fruit of fruits){
    if (fruit === 'lemon'){
        break;
    }
    console.log(fruit);
}