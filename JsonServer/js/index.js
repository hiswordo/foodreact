// javascript for index.html
// ??
const container = document.querySelector('.blogs'); //class blogs
console.log(container) // ?? 為什麼可以得到下面跑完的結果

const renderPosts = async () => {
    let uri = "http://localhost:3000/posts"

    const res = await fetch(uri);
    const posts = await res.json();
    // console.log(posts)

    // href="/xxx.html" 絕對路徑
    // href="xxx.html" 絕對路徑
    let template = '';
    posts.forEach(post => {
        template += `
            <div class="post">
                <h2>${post.title}</h2>
                <p><small>${post.likes} likes</small></p>
                <p>${post.body.slice(0, 200)}...</p>
                <a href="details.html?id=${post.id}">Read more ...</a>
            </div>
        `
    });
    container.innerHTML = template; //!記得要放函式裡面
}



window.addEventListener('DOMContentLoaded', () => renderPosts());