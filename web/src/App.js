import React from 'react';

import { Cards, Chart, HashtagPicker, RandomTweets } from './components';
import styles from './App.module.css';
import { fetchData } from './api';
import { BottomNavigation, BottomNavigationAction } from '@material-ui/core';
import BarChartIcon from '@material-ui/icons/BarChart';
import ShowChartIcon from '@material-ui/icons/ShowChart';

class App extends React.Component {

    state = {
        data: {},
        hashtag: 'global',
        chartType: 1,
    }

    async componentDidMount() {
        const fetchedData = await fetchData();

        this.setState({data: fetchedData});
    }

    handleHashtagChange = async (hashtag) => {
        const fetchedData = await fetchData(hashtag);
        
        this.setState({data: fetchedData, hashtag: hashtag});
    }

    handleChartChange = (event, newValue) => {
        this.setState({chartType: newValue})
    }
    
    render() {
        const {data} = this.state;
        const {hashtag} = this.state;
        const {chartType} = this.state;
        
        return (
            <div className={styles.container}>
                <Cards data={data}/>
                <HashtagPicker handleHashtagChange={this.handleHashtagChange}/>
                <BottomNavigation xs={12} md={3} value={this.state.chartType} onChange={this.handleChartChange}>
                    <BottomNavigationAction label={"Line"} value={0} icon={<ShowChartIcon />}/>
                    <BottomNavigationAction label={"Bar"} value={1} icon={<BarChartIcon />}/>
                </BottomNavigation>
                <Chart hashtag={hashtag} chartType={chartType}/>
                <RandomTweets data={data}/>
            </div>
        )
    }
}

export default App;