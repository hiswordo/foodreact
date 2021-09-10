import { useState, useEffect } from 'react';
import BlogList from './BlogList';
import useFetch from './useFetch';


const Home = () => {
    // we call it(data) blogs in this context
    // ! data, isPending, error要fetch裡面一樣
    // ?? 但為什麼呢? 這頁面跟上頁面有何關係?
    const { data: blogs, isPending, error } = useFetch('http://localhost:8000/blogs') 
    // const { data, isPending2, error2 } = useFetch('http://localhost:8000/blogs')

    return (
        <div className="home">
            {error && <div>{error}</div>}
            {isPending && <h2>Loading ... </h2>}
            {blogs && <BlogList blogs={blogs} />}
            {/* {data && <BlogList blogs={data} />} */}
        </div>
    );
}

export default Home
