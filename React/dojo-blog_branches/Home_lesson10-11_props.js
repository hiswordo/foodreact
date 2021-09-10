import { useState } from 'react';
import BlogList from './BlogList_lesson10-11_props';

const Home = () => {
    const [blogs, setblogs] = useState([
        { title: 'My new website', body: 'lorem ipsum...', author: 'mario', id: 1 },
        { title: 'Welcome party!', body: 'lorem ipsum...', author: 'yoshi', id: 2 },
        { title: 'Web dev top tips', body: 'lorem ipsum...', author: 'mario', id: 3 }
    ])
    const num_list = 3;

    // *Lesson 11
    // Attempted import error: './BlogList' does not contain a default export 
    // 當你把return裡面的{參數}一起帶走，那資料會對不上
    // 此時可以用props來幫忙傳遞資料，也讓這個BlogList模組能夠更能reusable
    // *傳遞的名稱應該是命名一樣會比較好用?
    // blogsmoving就相當於BlogList裡的props物件裡面的屬性 //!如果用有s結尾的名稱，要注意兩個文件內都有
    // ?? BlogList都沒有complete code提示出來，也不會自動import原因是甚麼? 
    return (
        <div className="home">
            <BlogList blogsmoving = {blogs} nummoving = {num_list}/>
        </div>
    );
}





// Lesson 10
// const Home = () => {
//     const [blogs, setblogs] = useState([
//         { title: 'My new website', body: 'lorem ipsum...', author: 'mario', id: 1 },
//         { title: 'Welcome party!', body: 'lorem ipsum...', author: 'yoshi', id: 2 },
//         { title: 'Web dev top tips', body: 'lorem ipsum...', author: 'mario', id: 3 }
//     ])

//     /* {blogs.map(()=>())} */
//     // blogs.map((blog)，blog可以取任何名字，表i
//     return (
//         <div className="home">
//             {blogs.map((blog) => (
//                 <div className="blog-preview" key={blog.id}>
//                     <h2>{blog.title}</h2>
//                     <p>written by { blog.author }</p>
//                 </div>

//             ))}

//         </div>
//     );
// }

export default Home
