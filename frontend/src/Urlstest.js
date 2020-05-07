import React from 'react';
import App from "./App";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

let testurl = () =>{
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/app">App</Link>
                        </li>
                        <li>
                            <Link to="/users">Users</Link>
                        </li>
                    </ul>
                </nav>

                {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
                <Switch>
                    <Route path="/app">
                        <App />
                    </Route>
                    <Route path="/users">
                        2
                    </Route>
                    <Route path="/">
                        3
                    </Route>
                </Switch>
            </div>
        </Router>);
};

export default testurl;