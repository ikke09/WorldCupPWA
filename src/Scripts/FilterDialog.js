import React from 'react';
import PropTypes from 'prop-types';
import Button from '@material-ui/core/Button';
import DialogTitle from '@material-ui/core/DialogTitle';
import Dialog from '@material-ui/core/Dialog';
import DialogContent from '@material-ui/core/DialogContent';
import DialogActions from '@material-ui/core/DialogActions';
import Typography from '@material-ui/core/Typography';

import FormControlLabel from '@material-ui/core/FormControlLabel';

import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';

const filterNames = [
    "Todays Matches",
    "Upcoming Matches",
    "All Matches"
]

var choosenFilter = null;

class FilterDialog extends React.Component {
    handleClose = () => {
        this.props.onClose(choosenFilter);
    };

    handleListItemClick = value => {
        choosenFilter = value;
    };

    handleCancel = () => {
        choosenFilter = null;
        this.handleClose();
    }

    render() {
        const { classes, onClose, selectedValue } = this.props;

        return (
            <Dialog
                open={this.props.open}
                onClose={this.handleClose}
                aria-labelledby="simple-dialog-title"
            >
                <DialogTitle id="alert-dialog-title">{"Filter Matches"}</DialogTitle>
                <DialogContent>
                    <RadioGroup
                        aria-label="Filter"
                        name="matchFilter"
                        value='Filter'
                        onChange={this.handleChange}
                    >
                        {filterNames.map(filter => (
                            <FormControlLabel
                                value={filter}
                                control={<Radio />}
                                label={filter}
                                onClick={() => this.handleListItemClick({ filter })}
                            />
                        ))}
                    </RadioGroup>
                </DialogContent>
                <DialogActions>
                    <Button onClick={this.handleCancel} color="primary">
                        Cancel
                        </Button>
                    <Button onClick={this.handleClose} color="primary" autoFocus>
                        OK
                        </Button>
                </DialogActions>
            </Dialog>
        );
    }
}

FilterDialog.propTypes = {
    classes: PropTypes.object.isRequired,
    onClose: PropTypes.func,
    selectedValue: PropTypes.string,
};

export default FilterDialog;
