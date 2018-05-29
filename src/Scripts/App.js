import React, { Component } from 'react';
import logo from '../Resources/Logo_2018_FIFA_World_Cup.svg';
import '../Styles/App.css';
import Button from '@material-ui/core/Button';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">FIFA World Cup 2018 in Russia</h1>
        </header>
      </div>
    );
  }
}

export default App;
