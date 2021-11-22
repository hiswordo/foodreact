import { useState, useEffect } from 'react';
import BlogList from './BlogList';
import useFetch from './useFetch';


const Home = () => {
    const { data: blogs, isPending, error } = useFetch('http://localhost:3000/blogs') 

    return (
        <div className="home">
            {error && <div>{error}</div>}
            {isPending && <h2>Loading ... </h2>}
            {blogs && <BlogList blogs={blogs} />}
        </div>
    );
}

export default Home
