// @link [JavaScript Array Filter Method Practice in 5 Minutes - YouTube](https://www.youtube.com/watch?v=3LOEGS4qcRM&list=PLDlWc9AfQBfZGZXFb_1tcRKwtCavR7AfT&index=1) at 2021/8/21
// @link [GitHub - jamesqquick/javascript-array-functions-practice](https://github.com/jamesqquick/javascript-array-functions-practice) at 2021/8/21

const characters = [
    {
        name: 'Luke Skywalker',
        height: 172,
        mass: 77,
        eye_color: 'blue',
        gender: 'male',
    },
    {
        name: 'Darth Vader',
        height: 202,
        mass: 136,
        eye_color: 'yellow',
        gender: 'male',
    },
    {
        name: 'Leia Organa',
        height: 150,
        mass: 49,
        eye_color: 'brown',
        gender: 'female',
    },
    {
        name: 'Anakin Skywalker',
        height: 188,
        mass: 84,
        eye_color: 'blue',
        gender: 'male',
    },
];

//----FILTER----
//1. Get characters with mass greater than 100
/* const greater100Characters = characters.filter(
    (character) => character.mass > 80
);
console.log(greater100Characters); */
//2. Get characters with height less than 200
//3. Get all male characters
//4. Get all female characters


//----MAP----
//1. Get array of all names
/* const names = characters.map(character => character.name);
console.log(names); */


//2. Get array of all heights
//3. Get array of objects with just name and height properties
//! {}外面要再加()，形成({})
/* const minifiedRecords = characters.map(character => ({
    name: character.name, 
    height: character.height
}));
console.log(minifiedRecords); */
//4. Get array of all first names
/* const firstname = characters.map(character => character.name.split(" ")[0]);
console.log(firstname); */

//----Comparing to foreach and include---
//----FOREACH---
// 依次印出每個人的名字
// characters.forEach(character => console.log(character.name))
// 將每個人的名子組成一個array
/* const x = [];
const foreachChracter = characters.forEach(character => x.push(character.name));
console.log(x); */

// *增加array的元素item
// const x = [1, 2, 3];
// const y = [...x, 4, 5];
// console.log(x);
// console.log(y);

// const x = [1, 2, 3]
// x.push(4, 5);
// console.log(x);

//----INCLUDES----
/* const items = [1,2,3,4,5];
const newinitems = items.includes(3);
console.log(newinitems); */

//----SOME----
//1. Is there at least one male character?
/* const oneManCharacter = characters.some(character => character.gender==="male");
console.log(oneManCharacter); */
//2. Is there at least one character with blue eyes?
//3. Is there at least one character taller than 210?
//4. Is there at least one character that has mass less than 50?


//----SORT----
//! 分為數字 a,b => a-b 由小排到大
//! 字串兩種
//1. Sort by mass (由小排到大)
/* const byMass = characters.sort((a, b) => a.mass - b.mass);
console.log(byMass); */
//2. Sort by height (由大排到小)
/* const byHeight = characters.sort((a, b) => b.height - a.height);
console.log(byHeight.map(x=>x.height)); */
//3. Sort by name
/* const byName = characters.sort((a, b) => {
    if (a.name < b.name) {
        return -1
    } else { return 1 }
});
console.log(byName); */
//4. Sort by gender (倒過來排，從Male排到Female)
/* const byGender = characters.sort((a, b) => {
    if (a.gender < b.gender) return 1;
    return -1;
});
console.log(byGender); */

//----REDUCE---- ((acc, cur)=>,acc=0)
//1. Get total mass of all characters
// TODO #JS Reduce: acc原本為空的，其實也可以放{}，這裡，讓acc=0起頭，cur為逐次讀進來的object{}直到把objects全部讀完
// const totalMass = characters.reduce((acc, cur) => acc + cur.mass, 0) //acc=0
// console.log(totalMass);
//2. Get total height of all characters
//*3. Get total number of characters by eye color
/* const totalEyecolor = characters.reduce((acc, cur) => {
    const color = cur.eye_color;
    if(acc[color]){
        acc[color] = acc[color] + 1; 
        console.log(color);
        console.log("Add1");
    }else{
        console.log(acc[color]); //只要進到這個迴圈的都是undefined，需要第一次建立
        acc[color] = 1; //等於直接建立一個新的key&value，第一次就是blue:1
        console.log(color);
        console.log("be the 1");
    }
    console.log("going to return");
    return acc;
}, {})
console.log(totalEyecolor); //{ blue: 2, yellow: 1, brown: 1  */

//3-2. 區分male，跟female總數
/* const totalGender = characters.reduce((acc, cur) => {
    const cgender = cur.gender;
    if (acc[cgender]){
        acc[cgender] ++;
    } else{
        acc[cgender]=1;
    }
    return acc
}, {})
console.log(totalGender);
 */
/* const totalGender = characters.reduce((acc, cur) => {
    if (cur.gender==="male"){
        acc["male"] ++;
    }else{
        acc["female"] ++;
    }
    return acc;
}, {"male":0,"female":0})
console.log(totalGender); */

//4. Get total number of characters in all the character names
/* const totalNameCharacters = characters.reduce((acc, cur) => acc = acc + cur.name.length, 0)
console.log(totalNameCharacters);
 */
// reduce實驗
/* const arrayNum = [2,7,1,5]; //15
const totalNum = arrayNum.reduce((a,b)=>a*2+b,0);
// a = 0*2+2
// a = 2*2+7
// a = 11*2+1
// a = 23*2+5
// a = 51
console.log(totalNum); */


//----EVERY----
//1. Does every character have blue eyes?
/* const areAllBlueEyes = characters.every((character) => character.eye_color === "blue");
console.log(areAllBlueEyes); */
//2. Does every character have mass more than 40?
//3. Is every character shorter than 200?
//4. Is every character male?

