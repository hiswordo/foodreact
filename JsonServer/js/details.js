// javascript for details.html
// const id = new URLSearchParams(window.location.search) // 則html後面的全部都取
const id = new URLSearchParams(window.location.search).get('id');
const container = document.querySelector('.details');

const renderDetails = async () => {
  const res = await fetch('http://localhost:3000/posts/' + id); //單獨取用一個json裡面的資料 //?? 這會對應id喔!!很神奇
  const post = await res.json();
  console.log(post)
  const template = `
    <h1>${post.title}</h1>
    <p>${post.body}</p>
  `

  container.innerHTML = template;
}


window.addEventListener('DOMContentLoaded', () => renderDetails());