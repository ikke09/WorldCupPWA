import React from 'react';
import ReactDOM from 'react-dom';
import './Styles/index.css';
import App from './Scripts/App';
import registerServiceWorker from './Scripts/registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
