import axios from 'axios';

const apiUrl = `https://semanticanalizisapp.azurewebsites.net/`;

export const fetchData = async (hashtag) => {
    let changeableUrl = apiUrl;

    if(hashtag) {
        changeableUrl = `${apiUrl}/${hashtag}`
    } else {
        changeableUrl = `${apiUrl}/global`
    }

    try {
        const { data: {positive, neutral, negative, lastUpdate, randomTweets }} = await axios.get(changeableUrl);
        
        return { positive, neutral, negative, lastUpdate, randomTweets };
    } catch (error) {
        console.log(error);
    }
}

export const fetchDailyData = async (hashtag) => {
    let changeableUrl = apiUrl;

    if(hashtag) {
        changeableUrl = `${apiUrl}/${hashtag}`
    } else {
        changeableUrl = `${apiUrl}/global`
    }


    try {
        const { data: {dailyData} } = await axios.get(changeableUrl);

        return dailyData;
    } catch (error) {
        console.log(error);
    }
}
