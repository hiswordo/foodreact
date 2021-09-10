import { Link } from "react-router-dom";


const BlogList = ({ blogs }) => {
    return (
        < div className="blog-list" >
            <h2>All Blogs</h2>
            {blogs.map((blog) => (
                <Link to={`/blogs/${blog.id}`}>
                    <div className="blog-preview" key={blog.id}>
                        <h2>{blog.title}</h2>
                        <p>written by {blog.author}</p>
                    </div>                
                </Link>
            ))}
        </div >
    );
}

export default BlogList;





