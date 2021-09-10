// Lesson 8
import { useState } from 'react';

const Home = () => {
    // ! 利用hook，use State來改名字顯示
    const [name, setName] = useState("Mario"); // let name = "Mario" 一樣意思，但當setName接收到數值會回傳取代
    const mario_age = 25;
    const [age, setAge] = useState(mario_age);

    // num_animal會一直在0, 1, 0, 1, 1, 2重複
    var listAnimals = ["Tiger", "Lion", "Dog", "Cat"];
    const [animal, setAnimal] = useState(listAnimals[3]);
    var num_animal = 0;

    const handleClick = () => {
        setName("Luigi");  // template
        setAge(30);
        console.log(num_animal);
        if (num_animal < 4){
            num_animal += 1
            setAnimal(listAnimals[num_animal])
        }
        console.log(num_animal);
    }

    return (
        <div className="home">
            <h2>Homepage</h2>
            <p style={{padding:"8px 0px"}}>{ name } is {age}</p>
            <p style={{padding:"8px 0px"}}>{ animal }</p>
            <button onClick={handleClick}>button</button>
        </div>
    );
}
 
export default Home

// Lesson 8
/*     //錯誤示範
    let name = 'mario';
    const handleClick = () => {
        name = "Luigi"
        console.log(name) //確實點了會改變name，但是不會反應在網頁上
    } */

// @link [Full React Tutorial #6 - Adding Styles - YouTube](https://www.youtube.com/watch?v=NbTrGcz4DW8&list=PL4cUxeGkcC9gZD-Tvwfod2gaISzfRiP9d&index=7) at 2021/8/17
// Lesson 6
/* const Home = () => {
    const handleClick = () => {
        console.log("Hello Ninja")
    }
    const handleClickAgain = (name) => {
        console.log("Hello " + name)
    }
    const handleClick2 = (f) => {
        console.log("Hello Ninja", f.type) //+ click
    }
    const handleClickAgain2 = (name, g) => {
        console.log("Hello " + name, g.target) //+ <button style="user-select: auto;">Click me again</button>
    }
    return (
        <div className="home">
            <h2>Homepage</h2>
            <button onClick={handleClick}>button</button>
            <button onClick={() => handleClickAgain("Mario")}>Click me again</button>
            <h2>----</h2>
            <h2>EventObject</h2>
            <button onClick={handleClick2}>button</button>
            <button onClick={(e) => handleClickAgain2("Mario", e)}>Click me again</button>
        </div>
    );
}
 
export default Home */


// Lesson 7
// @link [Full React Tutorial #7 - Click Events - YouTube](https://www.youtube.com/watch?v=0XSDAup85SA&list=PL4cUxeGkcC9gZD-Tvwfod2gaISzfRiP9d&index=8) at 2021/8/17
// ! 三者效果是一樣的，點擊後觸發，但後兩著是用匿名函數的方式
/* <button onClick={handleClick}>button</button> */
/* <button onClick={ () => {handleClick()} }>button</button> */
/* <button onClick={ () => handleClick() }>button</button> */
// ! 錯誤示範:直接呼叫 <button onClick={handleClickAgain("Mario")}>button</button>