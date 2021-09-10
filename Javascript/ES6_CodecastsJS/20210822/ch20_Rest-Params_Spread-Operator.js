// ----ch20.剩餘參數 Rest Params----
/* function sum(...nums) {
    return nums.reduce((acc, cur) => acc + cur, 0);
}
console.log(sum(1, 2, 3, 4));
console.log(sum(1, 2, 3)); */

// *amounts : [[Prototype]]: Array(0)
/* function convertCurrency(rate, ...amounts) {
    return amounts.map(amount => amount * rate);
}
console.log(convertCurrency(0.89, 30, 50, 100)); */

// 解構 destructing
/* const player1 = ['Jelly', 14377, 78.8, 77.1, 60.5, 85.7];
const [name, id, ...scores] = player1;
console.log(player1);
console.log(player1[0]);
console.log(name, id, scores); */

// ----ch21.擴展運算符 Spread Operator Intro----
// 與rest相反
/* splitedword = [...'expensive'] // ["e", "x", "p", "e", "n", "s", "i", "v", "e"]
console.log(splitedword); */

// 合併
/* const youngers = ['George','John','Thomas'];
const olders = ['james','Adrew','Martin'];
const members = youngers.concat(olders);
console.log(members); */

// 那如果合併中間要加一個對象Mary呢?
// 差想法: 用上述想法，要先let一個空的[]，然後依序放進去對吧?
/* const youngers = ['George', 'John', 'Thomas'];
const olders = ['james', 'Adrew', 'Martin'];
const newMembers = [...youngers, 'Mary', ...olders];
console.log(newMembers);
 */

// 製作:插入array資料函式
// insertMember($插入值, $原array, $插入位置));
/* const testmembers = ['George', 'John', 'Thomas', 'james', 'Adrew', 'Martin'];
const insertMember = (name, members, position) => {
  const formerMembers = members.slice(0, position - 1);
  const latterMembers = members.slice(position - 1, members.length);
  return [...formerMembers, name, ...latterMembers];
};
console.log(insertMember('Mary', testmembers, 4)); */

// 製作:插入array資料函式 (進階物件寫法)
// memberList: [ 'George', 'John', 'Thomas', 'james', 'Adrew', 'Martin' ],
// insertMember: [Function: insertMember]
/* const memberArray = (...members) => ({
  memberList: [...members],
  insertMember(newName, position) {
    console.log(this);
    const formerMembers = this.memberList.slice(0, position - 1);
    const latterMembers = this.memberList.slice(position - 1, this.memberList.length);
    return [...formerMembers, newName, ...latterMembers];
  },
});
const members001 = memberArray('George', 'John', 'Thomas', 'james', 'Adrew', 'Martin');
console.log(members001.insertMember('Mary', 4)); */

// ! fn()會直接執行，且function放在後面也沒關係，所以程式碼按照2,3,4執行
// fn();
// console.log('3');
// function fn() {
//   console.log('2');
// }
// console.log('4');
