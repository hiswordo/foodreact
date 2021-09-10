// @link [Full React Tutorial #32 - 404 Pages & Next Steps - YouTube](https://www.youtube.com/watch?v=XW0t2lk4Ffo&list=PL4cUxeGkcC9gZD-Tvwfod2gaISzfRiP9d&index=32) at 2021/8/19
import Navbar from './Navbar';
import Home from './Home';
// 需求-多頁面，安裝npm install react-router-dom@5，穩定版5，到node_modules
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Create from './Create';
import BlogDetails from './BlogDetails';
import NotFound from './NotFound';

//npm run start
//npx json-server --watch .\data\db.json --port 8000

// Swich依序搜尋Route，找到match的，像是網址列xxx/creat，它搜尋到/就結束了，不會再管create
// 所以需要exact
// 其他路徑用*全部表示，但記得放在最下面
// ?? 但這沒辦法對付兩層之後的路徑阿像是 /create/acdkj 或是 /blogs/asdba 都不會404
function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/create">
              <Create />
            </Route>
            <Route path="/blogs/:id">
              <BlogDetails />
            </Route>
            <Route path="*">
              <NotFound />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;

/*
  const title = "Hello! welcome to ninja world."
  const num_likes = 3000
  const link = "http://www.google.com"
return (
  <div className="App">
    <div className="content">
      <h1>{title}</h1>
      <p>liked {num_likes} times</p>
      <p>{10}</p>
      <p>{"string"}</p>
      <p>{[1, 2, 3, 4]}</p>
      <p>{Math.random() * 10}</p>

      <a href={link}>Google Link</a>
    </div>
  </div>
); */

/* react-router-dom@5 安裝情況
npm WARN @babel/plugin-bugfix-v8-spread-parameters-in-optional-chaining@7.14.5 requires a peer of @babel/core@^7.13.0 but none is installed. You must install peer dependencies yourself.
npm WARN tsutils@3.21.0 requires a peer of typescript@>=2.8.0 || >= 3.2.0-dev || >= 3.3.0-dev || >= 3.4.0-dev || >= 3.5.0-dev || >= 3.6.0-dev
|| >= 3.6.0-beta || >= 3.7.0-dev || >= 3.7.0-beta but none is installed. You must install peer dependencies yourself.
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.3.2 (node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.3.2: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\watchpack-chokidar2\node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules\webpack-dev-server\node_modules\fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})

+ react-router-dom@5.2.0
added 11 packages from 6 contributors and audited 1954 packages in 8.13s

148 packages are looking for funding
  run `npm fund` for details

found 3 moderate severity vulnerabilities
  run `npm audit fix` to fix them, or `npm audit` for details */
/*
  fixed 0 of 3 vulnerabilities in 1954 scanned packages
  3 vulnerabilities required manual review and could not be updated */