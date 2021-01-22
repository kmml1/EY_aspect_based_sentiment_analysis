import React from 'react';
import { Card, CardContent, Typography, Grid } from '@material-ui/core';
import CountUp from 'react-countup';
import cx from 'classnames';

import styles from './Cards.module.css';

const Cards = ({ data: { positive, neutral, negative, lastUpdate } }) => {
    if (!positive) {
        return 'Loading...';
    }
    return (
        <div className={styles.container}>
            <Grid container spacing={3} justify="center">
                <Grid item component={Card} xs={12} md={3} className={cx(styles.card, styles.positive)}>
                    <CardContent>
                        <Typography color="textSecondary" gutterBottom>Positive</Typography>
                        <Typography variant="h5">
                            <CountUp start={0} end={positive} duration={2.5} separator=',' />
                        </Typography>
                        <Typography color="textSecondary">{lastUpdate}</Typography>
                        <Typography variant="body2">Liczba pozytywnych tweetów</Typography>
                    </CardContent>
                </Grid>
                <Grid item component={Card} xs={12} md={3} className={cx(styles.card, styles.neutral)}>
                    <CardContent>
                        <Typography color="textSecondary" gutterBottom>Neutral</Typography>
                        <Typography variant="h5">
                            <CountUp start={0} end={neutral} duration={2.5} separator=',' />
                        </Typography>
                        <Typography color="textSecondary">{lastUpdate}</Typography>
                        <Typography variant="body2">Liczba neutralnych tweetów</Typography>
                    </CardContent>
                </Grid>
                <Grid item component={Card} xs={12} md={3} className={cx(styles.card, styles.negative)}>
                    <CardContent>
                        <Typography color="textSecondary" gutterBottom>Negative</Typography>
                        <Typography variant="h5">
                            <CountUp start={0} end={negative} duration={2.5} separator=',' />
                        </Typography>
                        <Typography color="textSecondary">{lastUpdate}</Typography>
                        <Typography variant="body2">Liczba negatywnych tweetów</Typography>
                    </CardContent>
                </Grid>
            </Grid>
        </div>
    )
}

export default Cards;