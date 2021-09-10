
// @link 教學:https://www.youtube.com/watch?v=XPMiVUrx1iE&list=PLRjgE3pAnTIKSGvW5_9akzyuu1M1lQi-U&index=18

// @link 字串相關:https://www.w3schools.com/js/js_string_methods.asp

// @link [PlayCode - Javascript Playground](https://playcode.io/new/) at 2021/8/17

// var的容器，英數 or $ or _的組合，開頭不能數字

/* var phrase = "Hello Motto";
document.write(phrase.length)
document.write("<br>")
document.write(phrase.toUpperCase())
document.write("<br>")
document.write(phrase.charAt(0))
document.write("<br>")
document.write(phrase.indexOf("h"))  //! 大小寫有差。字串記得括號。找不到為-1
document.write("<br>")
document.write(phrase.substring(0,5))
document.write("<br>")
document.write(phrase)
document.write("<br>") */


// 數字相關:https://www.w3schools.com/js/js_number_methods.asp
/*
var number = 6;
document.write(Math.abs(number));
document.write("<br>");
number = 99;
document.write(Math.max(2,3,number));
document.write("<br>");
number = 2.9;
document.write(Math.round(number));
var rannum = Math.random() * 10;
document.write(rannum);
document.write("<br>");
document.write(Math.round(rannum));
*/

// 計算機

/* var num1 = prompt("num1=?")
var num2 = prompt("num2=?")
// ! 無條件捨去小數
num1 = parseInt(num1)
num2 = parseInt(num2)
// *浮點數
// num1 = parseFloat(num1)
// num2 = parseFloat(num2)
// *如果沒有parse，就會字串串接
document.write(num1+num2) */


//陣列
/* var friend = [20,true,"小黑"]; //大小寫有差內，true不能寫成True
console.log(friend);
document.write(friend);
document.write(friend.length);
 */

// function
/* function add(num1,num2){
    console.log(num2)
    document.write(num1+num2);
    document.write("<br>"); //<br> not <br/> or </br> 可能無法跑
    // console.log(num1+num2);
    return 30;  // return會直接跳出去
    document.write("Hi")
}
value = add(7,2);
// ! 得到 return值30
console.log(value);
document.write(10); */


// if
/* 
var hungry = true;
var rainy = false;
// if(hungry && rainy){
if(hungry || rainy){    
    document.write("不吃飯了")
}
else{
    document.write("都可以阿")
} */


// object
/* 
var car = {
    brand:"benz",
    price:400,
    is_used:true,
    finalprice:function(){
        if(this.is_used==false){
            var fiprice = this.price*0.9 //新車價特價
            return fiprice
        }
        else{
            var fiprice = this.price*0.6 //舊車價折價
            return fiprice 
        }
    }
}
car.is_used = false;
document.write('final price:'+car.finalprice());
document.write('<br>')
car.is_used = true;
document.write('final price:'+car.finalprice());
 */

// object真實物件
// movie https://en.wikipedia.org/wiki/The_Family_Man
/* 
var movie = {
    title: "The Family Man",
    release_date_infos: {
        year: 2000,
        month: 12,
        day: 22
    },
    release_date: function () {
        return this.release_date_infos.year + '-' + this.release_date_infos.month + '-' + this.release_date_infos.day
    },
    director: ["David Diamond", "David Weissman"],
    starring: [
        {
            name: "Nicolas Cage",
            age: 57,
            is_male: true
        }, // 很容易忽略,逗號
        {
            name: "Téa Leoni",
            age: 55,
            is_male: false
        }
    ]

}
// movie的title屬性
document.write(movie.title)
// movie的release_date方法，得到release_date_infos的整理訊息
document.write(movie.release_date());
// 物件屬性中的屬性
document.write(movie.release_date_infos.year)
//物件屬性陣列第一個
document.write(movie.director[0])
//物件屬性陣列第一個的屬性
document.write(movie.starring[0].name) */


//! while  迴圈小心無限迴圈
//* 兩者小於等於4的時候，沒差別，大於4
//* do至少跑一遍
//* 列印出2,3,4
/* var i = 5;
do {
    document.write(i)
    document.write('<br>')
    i++
} while (i <= 4)
 */
/* var i = 2;
while (i <= 4) {
    document.write(i)
    document.write('<br>')
    i++
}  */

//! for 小心()裡面放分號;
/* var friends = ['黑', '黃', '藍', '白']
for (var i = 0; i < friends.length; i++) {
        document.write(friends[i])
        document.write('<br>')
    } */

// 2維陣列、巢狀迴圈，列行包for
/* 
var arnumber = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9]
]

for(i=0; i<arnumber.length; i++){
    for(j=0; j<arnumber[i].length; j++){
        document.write(arnumber[i][j]);
    }
    document.write('<br>');
}
 */

// class (物件的模板)，如果全用物件寫，很沒效率
/* 
class Phone {
    constructor(a,b,c){
        this.number = a;
        this.year = b;
        this.is_waterproof = c;
    }
    phone_age(){
        return 2021 - this.year;
    }
}

var phone1 = new Phone('123',2001,false);
var phone2 = new Phone('456',2013,true);
var phone3 = new Phone('789',2020,true);
document.write(phone1.year)
document.write(phone1.is_waterproof)
document.write(phone2.phone_age())
 */

