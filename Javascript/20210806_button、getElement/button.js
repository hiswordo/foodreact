
// @link [【javascript】如何取得html元素 - YouTube](https://www.youtube.com/watch?v=LDbUPJ66s_E&list=PLRjgE3pAnTIKSGvW5_9akzyuu1M1lQi-U&index=17) at 2021/8/17
// 取得html
// 其實都是在window全域!底下
/* BOM
link = window.location.href
document.write(link) */
// DOM
// window.document.write();
// window.console.log();
/* var a ='specialist';
window.document.write(window.a) //?? 為什麼需要特別提呢 
*/

/* var get_h1 = document.getElementById("header");
// console.log(get_h1) //<h1 id="header">Helle Wolrd</h1>
get_h1.innerText = "小白好帥";
//必須是原先就有的屬性
get_h1.style.background="blue";
get_h1.style.color="green"; */

/* var get_link = document.getElementById("link")
get_link.href = "http://amazon.com"
console.log(get_link) */


// event listener 事件監聽
// https://www.w3schools.com/jsref/dom_obj_event.asp

// 在html btn上放onclick啟動hand_ck函式
/* function hand_ck(that){
    // alert('就你按你就案??');
    // console.log(that); // ??得到的是變化後的按鈕?為什麼
    that.innerText = "就你按你就案??";
    that.style = "color:white; background:red; border-width:10px; border-block-color:green;"//height: 60px; width: 120px;"
 
} */

/* function pagewrite(){
    document.write("great")
} */
// javscript add listener 抓取 按鈕 改變 按鈕:踢我
/* var btn = document.getElementById('btn');
console.log(btn);
btn.addEventListener('click',pagewrite) //
btn.addEventListener('click',hand_ck(btn)) // ??不用按就執行了，為什麼呢?
 */

/* var btn = document.getElementById('btn');
console.log(btn);
btn.addEventListener('click',function(){
    this.innerText = "就你按你就案??"; //這邊可以用this，很好用
    this.style = "color:white; background:red; border-width:10px; border-block-color:green;"
});
 */
//----點我: 越點變越多---
// 不過效果沒辦法累加 //?? 缺少可以讓style增加而非新增而取代的方式
/* var btn_count = 0;
function hand_ck(that){
    // 迴圈style大失敗，想複雜了，可以用的話也許有地方可以用??
    style_list = ['color','background','border-width']
    style_pairlist = ['white','red','10px']
    if(btn_count<3){
        that.style = style_list[btn_count]+":"+style_pairlist[btn_count];
        btn_count += 1;
        console.log(btn_count)
    }
} */

//----讓他越點越大----
/* var btn_count = 0;
function hand_ck(that){
    // that.style.height = that.style.height + 60px; //本身沒有的東西，當然沒用啦
    heightrange = 100+btn_count*100
    that.style = "height:"+heightrange+"px"
    console.log(that.style.height)
    if(btn_count<5){
        btn_count++
    }
}

 */