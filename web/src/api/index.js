import axios from 'axios';

const url = 'https://covid19.mathdro.id/api';

export const fetchData = async () => {
    try {
        //const { data: {confirmed, recovered, deaths, lastUpdate} } = await axios.get(url);

        return {
            positive:10000,
            neutral:15000,
            negative:5000,
            lastUpdate:"22.01.2021"
        };

    } catch (error) {
        
    }
}

export const fetchDailyData = async () => {
    try {
        const { data } = await axios.get('https://api.covidtracking.com/v1/us/daily.json');
  
        return data.map(({ positive, recovered, death, dateChecked: date }) => ({ confirmed: positive, recovered, deaths: death, date }));

    } catch (error) {

    }
}