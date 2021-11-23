import { useState } from "react";
import { useEffect } from "react";
import Cardlist from "./Cardlist";
// import DisplayAnImage from "./DisplayAnImage";

// import pic from './res/beefhotpot.jpg'; 
// one image link is wrong, it will crash
const Home = () => {

    const [cards, setCards] = useState([
        { title: 'store 1', body: '@expo/res/beefhotpot.jpg', stars:'★★★★★', id: 1},
        { title: 'store 2', body: './res/meatsoup.jpg', stars:'★★★☆☆', id: 2},
        { title: 'store 3', body: './res/noodle.jpg', stars:'★★★★☆', id: 3},
    ])

    const [visited, setVisited] = useState(false);
    const [name, setName] = useState('new guest');
    const inputNmae = <input type="text" />;

    const changeName = () => {
        setName(inputNmae)
    }

    useEffect(() => {
        setVisited(true);
    },[])
    // const handleClickAgain = (name, ee) => {
    //     console.log("Hello", ee.target);
    // }

    return (
        <div className="home">
            < Cardlist cards={cards}/>
            {/* < DisplayAnImage /> */}
            {/* <img src={pic} alt="" /> */}
            {/* <h2>Ground</h2>
            <p>Hello { name }</p>
            <p>Welcome! Can you tell me ur name?</p>
            { inputNmae }
            <button onClick={changeName}>Enter</button> */}
            {/* <button onClick={(ee)=>{handleClickAgain('name',ee)}}>Yes~</button> */}
        </div> 
    );
}

export default Home;