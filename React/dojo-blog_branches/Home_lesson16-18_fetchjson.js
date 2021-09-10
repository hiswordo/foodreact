import { useState, useEffect } from 'react';
import BlogList from './BlogList';

const Home = () => {
    //!小心部要打成[null]，好像會造成其他種類數值無法傳入，導致永遠是[null]
    const [blogs, setBlogs] = useState(null);
    const [isPending, setIsPending] = useState(true);

    // response需要時間，所以return .json下面要再接一個then才不會發生錯誤
    // 要看清楚loading可以加timeout，2秒後才執行裡面函示，平常部要亂用喔破壞使用者體驗
    console.log("----ck----")
    useEffect(() => {
        console.log("----4.start fetch----");
        setTimeout(() => {
            fetch('http://localhost:8000/blogs')
                .then(res => {
                    console.log("----5.start json----");
                    return res.json();
                })
                .then(data => {
                    setBlogs(data);
                    setIsPending(false);
                    console.log("----7.get data----");
                })
        },2000)
    }, [])
    //! [] 不要忘記 React 會延後執行 useEffect 直至瀏覽器完成繪制
    console.log("----1.break----")
    //! 因為blogs的初始值null，而接收data需要時間，如果沒有先確認收到，執行會出問題 // ??但為什麼
    // 錯誤訊息 TypeError: Cannot read property 'title' of null
    //! 記得讓javascript運作要再{}裡面
    // dynamic check &&的邏輯是:blogs本身是null，就會是false的狀態，而右邊的是正確描述式，所以呈現true。
    // 但因為F&T，所以不會有output，直到左邊也T，才執行右邊的描述
    // ?? 程式碼執行順序: 從頭到尾 -> useEffect -> BlogList(這邊一定要按順序到嗎?) -> setBlogs(這一定最後嗎?)
    //                     123 -> 45 -> 1236 -> 7
    return (
        <div className="home">
            {console.log("----2.start to return blogs----")}
            {isPending && <h2>Loading ... </h2>}
            {blogs && <BlogList blogs={blogs} />}
            {console.log("----3.ready to return blogs----")}
        </div>
    );
}

export default Home
