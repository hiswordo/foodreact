// Initialize button with user's preferred color 
let changeColor = document.getElementById("changeColor");

// 讓popup.html button的背景變為color
chrome.storage.sync.get("color", ({
  color
}) => {
  changeColor.style.backgroundColor = color;
});

// "permissions": ["activeTab", "scripting"]
// When the button is clicked, inject setPageBackgroundColor into current page
changeColor.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({
    active: true,
    currentWindow: true
  });

  chrome.scripting.executeScript({
    target: {
      tabId: tab.id
    },
    function: setPageBackgroundColor,
  });
});

// The body of this function will be executed as a content script inside the
// current page
function setPageBackgroundColor() {
  chrome.storage.sync.get("color", ({
    color
  }) => {
    document.body.style.backgroundColor = color;
  });
}



// function addElementDiv(obj) {
//   var parent = document.getElementById(obj);
//   //新增 div
//   var div = document.createElement("div");
//   //設定 div 屬性，如 id
//   div.setAttribute("id", "newDiv");
//   div.innerHTML = "js 動態新增div";
//   parent.appendChild(div);
// }

function addElementDiv() {
  // var parent = document.getElementById(obj);
  //新增 div
  var div = document.createElement("div");
  //設定 div 屬性，如 id
  div.setAttribute("id", "newDiv");
  div.innerHTML = "js 動態新增div";
  // parent.appendChild(div);
  return div
}
// @link [html - Using Javascript to hide elements with specific data-test-id value - Stack Overflow](https://stackoverflow.com/questions/48064475/using-javascript-to-hide-elements-with-specific-data-test-id-value) at 2021/10/6
// @link [javascript如何隐藏显示div - web开发 - 亿速云](https://www.yisu.com/zixun/451914.html) at 2021/10/6
// @link [getelementbyid - Get element inside element by class and ID - JavaScript - Stack Overflow](https://stackoverflow.com/questions/7815374/get-element-inside-element-by-class-and-id-javascript) at 2021/10/6

let hidediv = document.getElementById("hideDiv");

hidediv.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({
    active: true,
    currentWindow: true
  });

  chrome.scripting.executeScript({
    target: {
      tabId: tab.id
    },
    function: hidingSelectedDiv,
  });
});


// function savingdata(myArray){
//   // Save the current myArray value.
//   chrome.storage.local.set({'storedArray': myArray}, function() {
//   console.log(`storedArray now contains ${myArray}.`);
//   });
//   // Retrieve the the stored value, defaulting to an empty array.
//   chrome.storage.local.get({'storedArray': []}, function(data) {
//   console.log(`storedArray's value is ${data.storedArray}.`);
//   console.log(data.storedArray)
//   });
// }

function hidingSelectedDiv() {
  // restids = ['vendor-y8gl', 'vendor-i27q'] //朱確幸餐館 & 新煮義關東煮專賣店、炒泡麵

  // @link 獲得與增加屬性id等 [DOM HTML 屬性 HTML Attributes - JavaScript (JS) 教學 Tutorial](https://www.fooish.com/javascript/dom/html-attributes.html) at 2021/10/7
  // let restids = document.getElementsByClassName('vendor-list')[0].getElementsByTagName('li'); // 選到li跟更裡面的li，麻煩
  // 為所有餐廳加上按鈕
  let items = document.getElementsByClassName('vendor-list')[0].childNodes;
  for (let item of items) {
    // console.log(restid.getAttribute('data-testid'));  // 店家ID
    // console.log(restid.getElementsByClassName("name")[0].textContent); // 店家店名
    let addbut = document.createElement("button");
    let dataid = item.getAttribute('data-testid');
    addbut.setAttribute("class", "addBtn");
    addbut.setAttribute("id", dataid);
    addbut.innerHTML = "Remove";
    // TODO 增加mark功能，顯示需再調整
    let markbut = document.createElement("button");
    markbut.setAttribute("class", "markbut");
    markbut.setAttribute("id", dataid);
    markbut.innerHTML = "Mark";
    // @link [Node.isEqualNode - Web API 接口参考 | MDN](https://developer.mozilla.org/zh-CN/docs/Web/API/Node/isEqualNode) at 2021/10/7
    //?? 直接用相等式卻沒辦法，原因不明 addbut == item.lastChild，就算長一樣，結果變成一定false
    condition = addbut.isEqualNode(item.lastChild) || addbut.isEqualNode(item.lastChild.previousSibling);
    if (condition){
      //pass
    } else {
      item.appendChild(addbut);
      item.appendChild(markbut);
    }
  }

  // @link 監聽所有按鈕 [javascript - How to add one event listener for all buttons - Stack Overflow](https://stackoverflow.com/questions/49680484/how-to-add-one-event-listener-for-all-buttons/49680660) at 2021/10/7
  // @link 存資料 [javascript - Storing a HTML OBJECT Array inside Chrome Storage for a Chrome Extension - Stack Overflow](https://stackoverflow.com/questions/57676249/storing-a-html-object-array-inside-chrome-storage-for-a-chrome-extension) at 2021/10/7
  const wrapper = document.getElementsByClassName('vendor-list')[0];

  // @link 清除資料 [javascript - How to clear chrome.storage.local and chrome.storage.sync? - Stack Overflow](https://stackoverflow.com/questions/31812937/how-to-clear-chrome-storage-local-and-chrome-storage-sync) at 2021/10/7 
  // chrome.storage.local.clear(function() {
  //   var error = chrome.runtime.lastError;
  //   if (error) {
  //       console.error(error);
  //   }
  //   // do something more
  // });
  // chrome.storage.sync.clear();

  chrome.storage.local.get({
    'storedArray': [], 'storedMarkArray': []
  }, function (data) {  
    console.log(`storedArray's value is ${data.storedArray}.`);
    console.log(data.storedArray);
    console.log(data.storedMarkArray);
    const myArray = [...data.storedArray]; //!拓展array ES6 寫法真棒耶!
    const myMarkArray = [...data.storedMarkArray];

    // @link undefined的資料判斷 [javascript - How can I determine if a variable is 'undefined' or 'null'? - Stack Overflow](https://stackoverflow.com/questions/2647867/how-can-i-determine-if-a-variable-is-undefined-or-null) at 2021/10/7
    // var element = document.querySelectorAll('[data-testid=' + "vendor-kdxj" + ']');
    // console.log(element[0]);
    // element[0].style.display = 'none';
    // "vendor-x0od" "vendor-f5oj" 沒有的ID 
    for (let idname of data.storedArray) {
      //   // console.log(idname);
      if (idname !== ''){
        var element = document.getElementsByClassName('vendor-list')[0].querySelectorAll('[data-testid=' + idname + ']'); 
      } else{
        var element = document.getElementsByClassName('vendor-list')[0].querySelectorAll('[data-testid=' + 'Nothing' + ']');
      }
      //! 如果沒先抓vendor-list，有可能找到兩個重複的，因為上面也有同樣餐廳
      // console.log(element)
      if (element[0] == null) {
        console.log("Nothing Found");
      } else {
        // console.log(element);
        element[0].style.display = 'none';
      }
    }

    for (let idmname of data.storedMarkArray) {
      //   // console.log(idname);
      if (idmname !== ''){
        var element = document.getElementsByClassName('vendor-list')[0].querySelectorAll('[data-testid=' + idmname + ']'); 
      } else{
        var element = document.getElementsByClassName('vendor-list')[0].querySelectorAll('[data-testid=' + 'Nothing' + ']');
      }
      //! 如果沒先抓vendor-list，有可能找到兩個重複的，因為上面也有同樣餐廳
      // console.log(element)
      if (element[0] == null) {
        console.log("Nothing Found");
      } else {
        // console.log(element);
        element[0].style.border = '4px solid #ff9800';
      }
    }

    // @link [Check if an Element Contains a Class in JavaScript](https://www.javascripttutorial.net/dom/css/check-if-an-element-contains-a-class/) at 2021/10/13
    wrapper.addEventListener('click', (event) => {
      // const isButton = event.target.nodeName === 'BUTTON';
      const isaddButton = event.target.classList.contains('addBtn');
      // console.log(event.target.classList.contains('addBtn')); //true
      // const isRmButton = event.target.getElementsByClassName('removeBtn');
      // console.log("Test");
      // console.log(isRmButton)
      // console.log(isRmButton[0] == null);
      if (isaddButton) {
        // console.dir(event.target.id);
        // *增加array新資料
        console.log("let's add");
        myArray.push(event.target.id);
        chrome.storage.local.set({
          'storedArray': myArray
        }, function () {
          console.log(`storedArray now contains ${event.target.id}.`);
        });
        //?? 並且當下清空div，半個都沒找到，也會變得怪怪的...還是""空白欄位惹得呢?
        var emptydiv = document.getElementsByClassName('vendor-list')[0].querySelectorAll('[data-testid=' + event.target.id + ']'); 
        emptydiv[0].style.display = 'none';
      }

      //增加markArray
      const ismarkButton = event.target.classList.contains('markbut');
      if (ismarkButton) {
        // console.dir(event.target.id);
        // *增加array新資料
        console.log("let's mark");
        myMarkArray.push(event.target.id);
        chrome.storage.local.set({
          'storedMarkArray': myMarkArray
        }, function () {
          console.log(`storedMarkArray now contains ${event.target.id}.`);
        });
        //?? 並且當下清空div，半個都沒找到，也會變得怪怪的...還是""空白欄位惹得呢?
        var markthediv = document.getElementsByClassName('vendor-list')[0].querySelectorAll('[data-testid=' + event.target.id + ']'); 
        markthediv[0].style.border = '4px solid #ff9800';
      }

      // const jsonContent = JSON.stringify(myArray);
      // const fs = require('fs');
      // const path = require('path');
      // fs.writeFileSync(path.resolve(__dirname, 'myArray.json'), JSON.stringify(jsonContent));
      // const jsonContent = JSON.stringify(myArray);
      // const fs = require('fs');
      // fs.writeFile("./myArray.json", jsonContent, 'utf8', function (err) {
      //     if (err) {
      //         return console.log(err);
      //     }

      //     console.log("The file was saved!");
      // }); 
    }); 
  });
}



// for (let restid of restids) {
//   var elements = document.querySelectorAll('[data-testid=' + restid + ']');
//   foo.attributes['data-testid'].value
//   for (let element of elements) {
//     element.style.backgroundColor = 'green';
//     // element.style.display = 'none';
//     resname = element.getElementsByClassName("name")[0].textContent;
//     var divadd = document.createElement("button");
//     //設定 div 屬性，如 id
//     divadd.setAttribute("id", "newDiv");
//     divadd.innerHTML = restid;
//     element.appendChild(divadd);
//   }
// }

// ---- version 1 ----
// function hidingSelectedDiv() {
//   restids = ['vendor-y8gl', 'vendor-i27q'] //朱確幸餐館 & 新煮義關東煮專賣店、炒泡麵
//   // or chrome.storage.sync,
//   // Save the current myArray value.
//   // myArray = ['vendor-y8gl', 'vendor-i27q']
//   // chrome.storage.local.set({'storedArray': myArray}, function() {
//   // console.log(`storedArray now contains ${myArray}.`);
//   // });

//   // Retrieve the the stored value, defaulting to an empty array.
//   chrome.storage.local.get({'storedArray': []}, function(data) {
//   console.log(`storedArray's value is ${data.storedArray}.`);
//   console.log(data.storedArray[1])
//   });

//   for (let restid of restids) {
//     var elements = document.querySelectorAll('[data-testid=' + restid + ']');
//     for (let element of elements) {
//       element.style.backgroundColor = 'green';
//       // element.style.display = 'none';
//       resname = element.getElementsByClassName("name")[0].textContent;
//       var divadd = document.createElement("button");
//       //設定 div 屬性，如 id
//       divadd.setAttribute("id", "newDiv");
//       divadd.innerHTML = restid;
//       element.appendChild(divadd);
//     }
//   }

// 抓取data-testid=vendor-y8gl屬性的tag，然後隱藏
// 新增: 對應抓取id底下的餐廳名稱，但不能達成===對應，很奇怪 (考慮用.innerText)
// function hidingSelectedDiv(){
//   var elements = document.querySelectorAll('[data-testid=vendor-y8gl]');
//   for (let element of elements) {
//     element.style.backgroundColor = 'green';
//     resname = element.getElementsByClassName("name")[0].textContent;
//     console.log(resname);
//     if(resname !== '朱確幸餐館'){
//       element.style.display = 'none';
//       element.style.backgroundColor = 'red';
//       console.log(resname);
//     }
//   }

// if(elements.style.display === 'none') {
//   elements.style.display = 'block';// 以块级元素显示
// } else {
//   elements.style.display = 'none'; // 隐藏
// }
// }

// ---- show ----
let showdiv = document.getElementById("showDiv");

showdiv.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({
    active: true,
    currentWindow: true
  });

  chrome.scripting.executeScript({
    target: {
      tabId: tab.id
    },
    function: showingSelectedDiv,
  });
});

function showingSelectedDiv() {
  let items = document.getElementsByClassName('vendor-list')[0].childNodes;
  for (let item of items) {
    item.style.display = 'none';
  }

  chrome.storage.local.get({
    'storedArray': []
  }, function (data) {  
    for (let idname of data.storedArray) {
      //   // console.log(idname);
      if (idname !== ''){
        var element = document.getElementsByClassName('vendor-list')[0].querySelectorAll('[data-testid=' + idname + ']'); 
      } else{
        var element = document.getElementsByClassName('vendor-list')[0].querySelectorAll('[data-testid=' + 'Nothing' + ']');
      }
      //! 如果沒先抓vendor-list，有可能找到兩個重複的，因為上面也有同樣餐廳
      // console.log(element)
      if (element[0] == null) {
        console.log("Nothing Found");
      } else {
        // console.log(element);
        element[0].style.display = 'block';
        let removebut = document.createElement("button");
        let dataid = element[0].getAttribute('data-testid');
        removebut.setAttribute("id", dataid);
        removebut.setAttribute("class", "removebtn");
        removebut.innerHTML = "AddBack";
        removebut.is
        condition = removebut.isEqualNode(element[0].lastChild) || removebut.isEqualNode(element[0].lastChild.previousSibling);
        // console.log(element[0].lastChild);
        // console.log(element[0].lastChild.previousSibling);
        if (condition){
          //pass
        } else {
          element[0].appendChild(removebut);
        }
      }
    }
    const wrapper = document.getElementsByClassName('vendor-list')[0];
    // @link [javascript - How can I remove a specific item from an array? - Stack Overflow](https://stackoverflow.com/questions/5767325/how-can-i-remove-a-specific-item-from-an-array) at 2021/10/8
    wrapper.addEventListener('click', (event) => {
      // console.log(event.target); //<button id="vendor-l9fe">vendor-l9fe</button>
      const isRmButton = event.target.getElementsByClassName('removeBtn')[0] == null;
      console.log("Click");
      console.log(isRmButton);
      console.log(event.target.id);
      if (isRmButton) {
        myArray = data.storedArray;
        const index = myArray.indexOf(event.target.id);
        if (index > -1) {
          myArray.splice(index, 1);
        }
        chrome.storage.local.set({
          'storedArray': myArray
        }, function () {
          console.log(`storedArray now has removed ${event.target.id}.`);
        });
      }
    }); 
  });
}

// 切換show跟hide他會一直新增按鈕，有幾顆，幾顆就會一起觸發