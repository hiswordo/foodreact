import { useState, useEffect } from 'react';

// 如果還沒跑完主頁面，就跳到其他頁面會出現錯誤如下
// Can't perform a React state update on an unmounted component
// 需要abortController並將此與useEffect聯繫一起
// 轉成err.name: `err.message = AbortError: Failed to execute 'fetch' on 'Window': The user aborted a request.
// 如果不希望catch這個錯誤訊息，加上if來判斷
// !不要拼錯 err.name = AbortError

const useFetch = (url) => {
    const [data, setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const abortCont = new AbortController();

        setTimeout(() => {
            fetch(url, {signal: abortCont.signal})
                .then(res => {
                    console.log(res);
                    if (!res.ok) {
                        throw Error("Could not fetch the data for that source!!!!");
                    }
                    return res.json();
                })
                .then(data => {
                    setIsPending(false);
                    setData(data);
                    setError(null);
                })
                .catch(err => {
                    // console.log(err.message);
                    // console.log(err.name);
                    if (err.name === 'AbortError'){
                        console.log("fetch aborted")
                    } else{
                        setIsPending(false);
                        setError(err.message);
                    }
                })
        }, 1000);

        return () => abortCont.abort();
        // return () => console.log("Clean Up") //?? 離開的時候觸發return，可以這樣說嗎?
    }, [url])

    return { data, isPending, error }
}

export default useFetch;