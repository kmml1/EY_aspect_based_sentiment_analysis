import React, { useState, useEffect } from 'react';
import { fetchDailyData } from '../../api';
import { Bar, Line } from 'react-chartjs-2';

import styles from './Chart.module.css';

const Chart = ({hashtag , chartType}) => {
    const [dailyData, setDailyData] = useState({});
    
    useEffect(() => {
        const fetchAPI = async () => {
            const initialDailyData = await fetchDailyData(hashtag);
            initialDailyData.sort(compare);
            setDailyData(initialDailyData);
        }

        fetchAPI();
    }, [hashtag]);

    if(!dailyData.length) {
        return null;
    }   

    const lineChart = (
        dailyData[0]
            ? (
                <Line
                    data={{
                        labels: dailyData.map(({ date }) => date),
                        datasets: [{
                            data: dailyData.map(({ positive }) => positive),
                            label: 'Pozytywne',
                            borderColor: 'rgb(0, 255, 0)',
                            backgroundColor: 'rgba(0, 255, 0, 0.25)',
                            fill: true,
                        }, {
                            data: dailyData.map(({ neutral }) => neutral),
                            label: 'Neutralne',
                            borderColor: 'rgb(255, 255, 0)',
                            backgroundColor: 'rgba(255, 255, 0, 0.25)',
                            fill: true,
                        }, {
                            data: dailyData.map(({ negative }) => negative),
                            label: 'Negatywne',
                            borderColor: 'red',
                            backgroundColor: 'rgba( 255, 0, 0, 0.25)',
                            fill: true,
                        }],
                    }}
                />) : null
    );

    const barChart = (
        dailyData[0]
            ? (
                <Bar
                    data={{
                        labels: dailyData.map(({ date }) => date),
                        datasets: [{
                            data: dailyData.map(({ positive }) => positive),
                            label: 'Pozytywne',
                            borderColor: 'rgb(0, 255, 0)',
                            backgroundColor: 'rgba(0, 255, 0, 1)',
                            fill: true,
                        }, {
                            data: dailyData.map(({ neutral }) => neutral),
                            label: 'Neutralne',
                            borderColor: 'rgb(255, 255, 0)',
                            backgroundColor: 'rgba(255, 255, 0, 1)',
                            fill: true,
                        }, {
                            data: dailyData.map(({ negative }) => negative),
                            label: 'Negatywne',
                            borderColor: 'red',
                            backgroundColor: 'rgba( 255, 0, 0, 1)',
                            fill: true,
                        }],
                    }}
                />) : null
    );

    return (
        <div className={styles.container}>
            {chartType ? barChart : lineChart}
        </div>
    )
}

function compare(a,b) {
    a = a.date;
    b = b.date;
    const a_array = a.split(" ");
    const b_array = b.split(" ");
    if(Number(a_array[1]) < 10) {
        a_array[1] = "0" + a_array[1];
    }
    if(Number(a_array[2]) < 10) {
        a_array[1] = "0" + a_array[1];
    }
    if(Number(b_array[1]) < 10) {
        b_array[1] = "0" + b_array[1];
    }
    if(Number(b_array[2]) < 10) {
        b_array[2] = "0" + b_array[2];
    }
    const a_date = a_array[0] + a_array[1] + a_array[2];
    const b_date = b_array[0] + b_array[1] + b_array[2];
    if(a_date > b_date) {
        return 1;
    }
    if(a_date < b_date) {
        return -1;
    }    
    return 0;
}


export default Chart;