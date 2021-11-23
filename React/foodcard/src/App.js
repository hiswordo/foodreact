// import logo from './logo.svg';
// import './App.css';
import Navbar from './Navbar';
import Home from './Home';

// 多頁面需求
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// import Create from './Create';
// import CardDetails from './BlogDetails';
// import NotFound from './NotFound';


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
            {/* <Route path="/create">
              <Create />
            </Route> */}
            {/* <Route path="/cards/:id">
              <CardDetails />
            </Route> */}
            {/* <Route path="*">
              <NotFound />
            </Route> */}
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
