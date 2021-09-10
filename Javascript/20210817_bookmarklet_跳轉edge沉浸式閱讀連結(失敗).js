//範例一:alert
// javascript: (function () { alert("hello, world"); })();

// ! 是可以的，但頁面連結其實改變很多，規則待研究
javascript: (function () {
    var linknow = location.href;
    var linknew = "read://"+linknow;
    window.location.href=linknew;
    location.assign(linknew);
})();

// 頁面一: https://ithelp.ithome.com.tw/articles/10221289
// 頁面二: read://https_ithelp.ithome.com.tw/?url=https%3A%2F%2Fithelp.ithome.com.tw%2Farticles%2F10221289
// read://https_ithelp.ithome.com.tw/?url=https
// %3A%2F%2F
// ithelp.ithome.com.tw
// %2F
// article
// s%2F
// 10221289

// 頁面一: https://codertw.com/%E5%89%8D%E7%AB%AF%E9%96%8B%E7%99%BC/249812/
// 頁面二: read://https_codertw.com/?url=https%3A%2F%2Fcodertw.com%2F%25E5%2589%258D%25E7%25AB%25AF%25E9%2596%258B%25E7%2599%25BC%2F249812%2F

// 跳轉頁面: 
// location.assign('http://www.fooish.com/');
// window.location.href='http://www.fooish.com/';

// 範例二:跳轉頁面 正式機：http://domanname/index.php -> 測試機一號：http://localhost/index.php
// javascript:(function(){
//     f=window.location.href;
//     f=f.replace(location.hostname, "localhost");
//     window.location.href=f;
// }())