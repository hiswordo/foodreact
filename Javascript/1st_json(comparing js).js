    /* json = javascript object notation*/
    // 教學:https://www.youtube.com/watch?v=t7TSFImLa0U

    // var point = new Object();
    // point.x = 3;
    // point.y = 4;
    // point.get = function(){
    //     alert(this.x + "," + this.y);
    // };

    var point = {"x":3,"y":4,"get":function(){
        alert(this.x + "," + this.y);
    }}
    // point.get();
    
    // console.log(point); //可以清楚看到object詳細資料
    // /*json傳輸需要轉成字串，轉換會忽略函式(方法的部分)*/
    // var jsonStr = JSON.stringify(point);
    // console.log(jsonStr); 
    // var jsonObj = JSON.parse(jsonStr);
    // console.log(jsonObj);
    // alert(jsonObj.x);
    // 線上js編輯器 https://playcode.io/new/