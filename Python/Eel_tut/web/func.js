
// python調用jsc函數
// eel.expose(hello);
// function hello(){
//     return 5;
// }

// # 從js調用函數slo2. 測試中
// eel.expose(hello);
// async function hello(){
//     wait1 = wait(500);
//     await wait1;
//     return 5;
// }

//  js調用python函數
// function wrapper(x){
//     alert(x);
// }
// function ranint(){
//     eel.ran_int()(wrapper);
// }
// 也可以兩個寫在一起
// function ranint(){
//     function wrapper(x){
//         alert(x);
//     }
//     eel.ran_int()(wrapper);
// }

// js調用python函數，比較好的寫法。協恆??
// async function ranint(){
//     var x = await eel.ran_int()();
//     alert(x)
// }

