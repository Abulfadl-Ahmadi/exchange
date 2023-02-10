import React, { Component } from "react";
import { createRoot } from 'react-dom/client';

// import { render } from "react-dom";

import HomePage from "./HomePage";


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <HomePage />
            </div>
        );
    }
}

// const appDiv = document.getElementById("app");
// render(<App />, appDiv);



// Before
// import { render } from 'react-dom';
// const appDiv = document.getElementById('app');
// render(<App tab="home" />, appDiv);

// After
// import { createRoot } from 'react-dom/client';
const appDiv = document.getElementById('app');
const root = createRoot(appDiv); // createRoot(container!) if you use TypeScript
root.render(<App />);