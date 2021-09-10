import { useHistory, useParams } from "react-router-dom";
import useFetch from "./useFetch";


// 使用router裡的變數:id，useParams
// ?? {}順序沒差的原因

const BlogDetails = () => {
    const { id } = useParams();
    const { data: blog, error, isPending } = useFetch("http://localhost:8000/blogs/" + id)
    const history = useHistory();
     
    const handleDelete = () => {
        fetch('http://localhost:8000/blogs/' + blog.id, {
          method: 'DELETE'
        }).then(() => {
          history.push('/');
        }) 
      }

    return (
        <div className="blog-details">
            {isPending && <h2>Loading ... </h2>}
            {error && <div>{ error }</div>}
            {blog &&
                <article>
                    <h2>Title: { blog.title }</h2>
                    <p>Written by { blog.author }</p>
                    <div>{ blog.body }</div>
                    <button onClick={handleDelete}>Delete</button>
                </article>}
        </div>
    );
}

export default BlogDetails;