const BlogList = (props) => {
    const blogs = props.blogsmoving; 
    console.log(props); // props物件傳過來，裡面包含看有幾項變數
    console.log("-----------");
    console.log(props.blogsmoving); //props物件裡面的List
    console.log(props.nummoving);

    return (
        // *Lesson 10 
        //map讓其建立成一個template iterator，數量龐大也能重複輸出List的元素
        <div className="blog-list">
            <p>Post Count:{props.nummoving} (把參數傳過來)</p>
            {
                blogs.map((blog) => (
                    <div className="blog-preview" key={blog.id}>
                        <h2>{blog.title}</h2>
                        <p>written by {blog.author}</p>
                    </div>
                ))
            }
        </div>
    );
}

export default BlogList;





