import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>The Dojo Blog</h1>
            <div className="links">
                <Link to="/">Home</Link>
                <Link to="/create">New Blog</Link>
            </div>
        </nav>
    );
}
 
export default Navbar;

// ?? 臨時加上style一定要這麼麻煩的原因是?
// 動態值{{}}，裡面的{}是javascript的object，對應的值記得stringfy
/* <a href="/create" style={{
    color:'white',
    backgroundColor:'#f1356d',
    borderRadius:'8px'
}}>New Blog</a> */