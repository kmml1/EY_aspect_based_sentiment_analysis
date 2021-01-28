import React from 'react';
import { Card, CardContent, Typography, Grid } from '@material-ui/core';
import cx from 'classnames';

import styles from './RandomTweets.module.css';

const RandomTweets = ({ data: { positive, neutral, negative, randomTweets } }) => {
    if (!(neutral + positive + negative)) {
        return "";
    }
    return (
        <div className={styles.container}>
            <Grid container spacing={3} justify="center">
                <Grid item component={Card} xs={12} md={12} className={cx(styles.card, styles.positive)}>
                    <CardContent>
                        <Typography color="textSecondary" gutterBottom>Losowy pozytywny tweet</Typography>
                        <Typography variant="body2">{randomTweets.positive}</Typography>
                    </CardContent>
                </Grid>
                <Grid item component={Card} xs={12} md={12} className={cx(styles.card, styles.neutral)}>
                    <CardContent>
                        <Typography color="textSecondary" gutterBottom>Losowy neutralny tweet</Typography>
                        <Typography variant="body2">{randomTweets.neutral}</Typography>
                    </CardContent>
                </Grid>
                <Grid item component={Card} xs={12} md={12} className={cx(styles.card, styles.negative)}>
                    <CardContent>
                        <Typography color="textSecondary" gutterBottom>Losowy negatywny tweet</Typography>
                        <Typography variant="body2">{randomTweets.negative}</Typography>
                    </CardContent>
                </Grid>
            </Grid>
        </div>
    )
}

export default RandomTweets; 