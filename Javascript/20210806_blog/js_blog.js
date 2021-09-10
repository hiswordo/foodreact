// 建立blog
// 教學:https://www.youtube.com/watch?v=wardEED9PT4&list=PLRjgE3pAnTIKSGvW5_9akzyuu1M1lQi-U&index=19

var title = document.getElementById("title");
var content = document.getElementById("content");
var btn = document.getElementById("btn");
var list = document.getElementById("list");

// console.log(btn);

// btn.addEventListener("click",function(){
//     // console.log(title.value);  //又來了，大小寫問題!value
//     // console.log(content.value);
//     // console.log(list.innerHTML);
//     //html就能引用js的內容${}，字串不能，且雙引號單引號都很容易衝突
//     //記得html的前後標註是用``esc下面的按鍵
//     list.innerHTML = list.innerHTML + `
//     <div class="article">
//         <h2>${title.value}</h2>
//         <p>${content.value}</p>
//     </div>`;
//     // 清空格子
//     title.value = "";
//     content.value = "";
// })

function posting(){
    list.innerHTML = list.innerHTML + `
    <div class="article">
        <h2>${title.value}</h2>
        <p>${content.value}</p>
    </div>`;
    // 清空格子
    title.value = "";
    content.value = "";
}

btn.addEventListener("click",posting) //啟用function不用posting()，posting就可以了