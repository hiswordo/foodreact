import { useState } from 'react';
import { useHistory } from 'react-router';

const Create = () => {
    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');
    const [author, setAuthor] = useState('yoshi');
    // ?? 不能放在handle裡面喔
    const [isPending, setIsPending] = useState(false);

    // ?? 這種hook一定要先變物件才能呼叫，不太懂
    const history = useHistory();

    // 阻止頁面Refresh : e.preventDefault(); 不然還沒傳送出去資料就不見了
    // ?? preventDefault()詳細過程不清楚
    // 傳送資料須先json化，傳送給json的server，會自動加上id
    const handleSubmit = (e) => {
        e.preventDefault();
        setIsPending(true);

        const blog = { title, body, author };

        fetch('http://localhost:8000/blogs/', {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(blog)
        }).then(() => {
            console.log('new blog added');
            setIsPending(false);
            history.push('/')
        })
    }

    //! button要放在form裡面，onSubmit才有效
    return (
        <div className="create">
            <h2>Add a new blog!</h2>
            {isPending && <div>Loading ... </div>}
            {!isPending &&
            <form onSubmit={handleSubmit}>
                <label>Blog title:</label>
                <input
                    type="text"
                    required
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
                <label>Blog body:</label>
                <textarea
                    required
                    value={body}
                    onChange={(e) => setBody(e.target.value)}
                ></textarea>
                <label>Blog author:</label>
                <select
                    value={author}
                    onChange={(e) => setAuthor(e.target.value)}
                >
                    <option value="mario">Mario</option>
                    <option value="yoshi">Yoshi</option>
                </select>
                {!isPending && <button>Add it now!</button>}
                {isPending && <button disabled>Adding... count down 3 2 1 ...</button>}
            </form>}
            {/* <p>title input : {title}</p>
            <p>body input : {body}</p>
            <p>author input : {author}</p> */}
        </div>
    );
}

export default Create;

// How to show or hide element in React
/*     // @link [How to show or hide element in React | Mohammed Asker](https://www.mohammedasker.com/how-to-show-or-hide-element-in-react) at 2021/8/19
    const [showText, setShowText] = useState(false);
    const Text = () => <div>You clicked the button!</div>;
    <div>
        <button onClick={() => setShowText(true)}>Click me</button>
        {showText ? <Text /> : null}
    </div> */