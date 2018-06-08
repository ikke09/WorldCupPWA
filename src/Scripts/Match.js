import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';

import '../Styles/Match.css';
import Paper from '@material-ui/core/Paper';

class Match extends React.Component {
    constructor(props) {
        super(props);
        this.Match = props.Match;
    }

    render() {
        return (
            <div className="Match">
                <Paper className="PaperMatch" elevation={4} style={{backgroundColor: '#ccc'}}>
                <div class="grid-container">
                    <div class="grid-item home flag">
                        <img src={this.Match.home_flag} 
                        alt={"Flag of "+this.Match.home_team} 
                        width={48} 
                        height={48}
                        />
                    </div>
                    <div class="grid-item home name">{this.Match.home_team}</div>
                    <div class="grid-item home result">{this.Match.home_result}</div>

                    <div class="grid-item divider">:</div>

                    <div class="grid-item away result">{this.Match.away_result}</div>
                    <div class="grid-item away name">{this.Match.away_team}</div>
                    <div class="grid-item away flag">
                    <img src={this.Match.away_flag} 
                        alt={"Flag of "+this.Match.away_team} 
                        width={48} 
                        height={48}
                        />
                    </div>

                    <div class="grid-item attr">{this.Match.date.toString()}</div>
                </div> 
                </Paper>
                
            </div>
        );
    }
}

export default Match;