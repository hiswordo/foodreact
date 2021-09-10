import { useState, useEffect } from 'react';
import BlogList from './BlogList';

const Home = () => {
    const [blogs, setblogs] = useState([
        { title: 'My new website', body: 'lorem ipsum...', author: 'Mario', id: 1 },
        { title: 'Welcome party!', body: 'lorem ipsum...', author: 'Yoshi', id: 2 },
        { title: 'Web dev top tips', body: 'lorem ipsum...', author: 'Mario', id: 3 }
    ])

    const handleDelete = (id) => {
        const newBlogs = blogs.filter((blog) => (blog.id !== id));
        setblogs(newBlogs)
    }

    const [name, setName] = useState("Mario")

    // *Lesson 15: useEffect Dependencies
    // ! 在預設情況下，effect 會在每一個完整 render 後執行，但你也可以選擇它們在某些值改變的時候才執行。
    // [name]: 第一次，與name改變的情況會觸發
    // []: 只有第一次useState會觸發
    // 預設: 只要有useState就會觸發
    useEffect(() => {
        console.log('use effect run');
        console.log(blogs)
    }, [name])

    return (
        <div className="home">
            <BlogList blogs={blogs} title="All Posts!" handleDelete={handleDelete} />
            <p>{name}</p>
            <button onClick={() => setName("Luigi")}>Change Name</button>
        </div>
    );
}

// *Lesson 12 : reuse component, filter
// return (
//     <div className="home">
//         <BlogList blogs={blogs} title="All Posts!" />
//         <BlogList blogs={blogs.filter((elment) => (elment.author === "Mario"))} title="Mario's!" />
//     </div>
// );
export default Home
