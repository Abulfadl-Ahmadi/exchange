import React, { Component } from "react";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
  } from "react-router-dom";
import CreateBookPage from "./CreateBookPage";



export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (<Router>
            <Routes>
                <Route path='/' element={ <p>Home Page</p> }></Route>
                <Route path='/create' element={ <CreateBookPage/> }></Route>
            </Routes>
        </Router>);
    }
}
