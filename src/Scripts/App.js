import React, { Component } from 'react';
import logo from '../Resources/Logo_2018_FIFA_World_Cup.svg';
import '../Styles/App.css';

import FilterDialog from './FilterDialog';
import Match from './Match';

import PropTypes from 'prop-types';
import classNames from 'classnames';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import MenuItem from '@material-ui/core/MenuItem';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Divider from '@material-ui/core/Divider';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import FilterIcon from '@material-ui/icons/FilterList';

const drawerWidth = 240;

var dummyMatch = {
  home_team: "Russia",
  away_team: "Germany",
  home_flag: "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/900px-Flag_of_Russia.png",
  away_flag: "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/800px-Flag_of_Germany.png",
  date: new Date(2018,6,18,19,0,0,0),
  away_result: 1,
  home_result: 0
};

const styles = theme => ({
  root: {
    flexGrow: 1,
  },
  flex: {
    flex: 1,
  },
  appFrame: {
    height: 430,
    zIndex: 1,
    overflow: 'hidden',
    position: 'relative',
    display: 'flex',
    width: '100%',
  },
  appBar: {
    position: 'absolute',
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  'appBarShift-left': {
    marginLeft: drawerWidth,
  },
  'appBarShift-right': {
    marginRight: drawerWidth,
  },
  menuButton: {
    marginLeft: 12,
    marginRight: 20,
  },
  menuButtonRight: {
    marginLeft: 20,
    marginRight: 12,
  },
  hide: {
    display: 'none',
  },
  drawerPaper: {
    position: 'relative',
    width: drawerWidth,
  },
  drawerHeader: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: '0 8px',
    ...theme.mixins.toolbar,
  }
});

class App extends Component {
  state = {
    drawerOpen: false,
    dialogOpen: false,
    drawerAnchor: 'left',
    selectedValue: null,
  };

  handleClickDrawerOpen = () => {
    this.setState({ drawerOpen: true });
  };

  handleClickDialogOpen = () => {
    this.setState({ dialogOpen: true });
  };

  handleDrawerClose = () => {
    this.setState({ drawerOpen: false });
  };

  handleDialogClose = (value) => {
    this.setState({ selectedValue: value, dialogOpen: false });
  };

  render() {
    const { classes, theme } = this.props;

    const drawer = (
      <Drawer
        variant="persistent"
        anchor={this.state.drawerAnchor}
        open={this.state.drawerOpen}
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <div className={classes.drawerHeader}>
          <IconButton onClick={this.handleDrawerClose}>
            {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
          </IconButton>
        </div>
        <Button variant="flat" color="primary">Overview</Button>
        <Button variant="flat" color="primary">Statstable</Button>
      </Drawer>
    );

    return (
      <div className={classes.root}>
        <div className={classes.appFrame}>
          <AppBar
            className={classNames(classes.appBar, {
              [classes.appBarShift]: this.state.drawerOpen,
              [classes[`appBarShift-${this.state.drawerAnchor}`]]: this.state.drawerOpen,
            })}
          >
            <Toolbar disableGutters={!this.state.drawerOpen}>
              <IconButton
                color="inherit"
                aria-label="open menu"
                onClick={this.handleClickDrawerOpen}
                className={classNames(classes.menuButton, this.state.drawerOpen && classes.hide)}
              >
                <MenuIcon />
              </IconButton>
              <Typography variant="title" color="inherit" classes={classes.flex} noWrap>
                FIFA World Cup 2018
              </Typography>
              <IconButton
                color="inherit"
                aria-label="open filter dialog"
                onClick={this.handleClickDialogOpen}
                className={classes.menuButtonRight}
              >
                <FilterIcon />
              </IconButton>
              <FilterDialog
                selectedValue={this.state.selectedValue}
                open={this.state.dialogOpen}
                onClose={this.handleDialogClose}
              />
            </Toolbar>
          </AppBar>
          {drawer}
        </div>
        <Match Match={dummyMatch}></Match>
      </div>
    );
  }
}

App.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired,
};

export default withStyles(styles, { withTheme: true })(App);     
