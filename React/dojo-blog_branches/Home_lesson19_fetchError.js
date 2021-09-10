import { useState, useEffect } from 'react';
import BlogList from './BlogList';

const Home = () => {

    const [blogs, setBlogs] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        setTimeout(() => {
            fetch('http://localhost:8000/blogss')
                .then(res => {
                    console.log(res);
                    if (!res.ok) {
                        // 已經有錯誤了，就不能再成功執行console.log了，網頁會直接爆掉
                        // 他會變成繼續執行下面的程式碼，然後使BlogList出現問題(TypeError: blogs.map is not a function)
                        throw Error("Could not fetch the data for that source!!!!");
                    }
                    return res.json();
                })
                .then(data => {
                    setBlogs(data);
                    setIsPending(false);
                })
                .catch(err => {
                    // 抓取網路連線錯誤，ex沒有連線上，但不能知道res,api的問題
                    // 如果上面throw Error有定義訊息，會捕捉，如果上面沒有，網頁一樣直接爆掉
                    console.log(err.message);
                    setError(err.message);
                })
        }, 500)
    }, [])

    // 只有error有值，才會執行&&後面的動作
    return (
        <div className="home">
            {error && <div>{error}</div>}
            {isPending && <h2>Loading ... </h2>}
            {blogs && <BlogList blogs={blogs} />}
        </div>
    );
}

export default Home
