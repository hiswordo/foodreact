// Custom Hook need to start with "use", otherwise, it won't work
import { useState, useEffect } from 'react';
// ?? 雖然成功了，但有Compiled with warnings，'useState' is defined but never used   no-unused-vars等

// Custom Hook
// 1.move useEffect
// 2.import and export the things u need
// 3.change the name of property which might not mean sth in the future
// 4.return those properties
// 5.check if any sepcific data is only used in this project

// ! 函式 記得打清楚 x = () => {} 
const useFetch = (url) => {
    const [data, setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    // useEffect(() => {}, [])如果後面沒改成[url]會出現以下錯誤
    // React Hook useEffect has a missing dependency: 'url'. Either include it or remove the dependency array  react-hooks/exhaustive-dep
    useEffect(() => {
        setTimeout(() => {
            fetch(url)
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
                    console.log(err.message);
                    setIsPending(false);
                    setError(err.message);
                })
        }, 1000);
    }, [url])


    // you can return anything (array, object, symbol, etc), even a boolean value
    // 當然用[Array]來回傳，JavaScript array destructuring syntax allows you to name each element.
    //! The destructuring assignment syntax is a JavaScript expression that makes it possible to 
    //! unpack values from arrays, or properties from objects, into distinct variables.
    // ex [a, b, ...rest] = [10, 20, 30, 40, 50]; console.log(rest); // expected output: Array [30,40,50]
    // ({a, b, ...rest} = {a: 10, b: 20, c: 30, d: 40}); // console.log(rest); // {c: 30, d: 40}
    return { data, isPending, error }
}

export default useFetch;