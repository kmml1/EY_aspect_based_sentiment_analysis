import React from 'react';
import { NativeSelect, FormControl } from '@material-ui/core';

import styles from './HashtagPicker.module.css';

const HashtagPicker = ({handleHashtagChange}) => {

    return (
        <FormControl className={styles.FormControl}>
            <NativeSelect defaultValue="" onChange={(e) => handleHashtagChange(e.target.value)}>
                <option value="global">Global</option>
                <option value="kwarantanna">#Kwarantanna</option>
                <option value="vege">#vege</option>
                <option value="IgaŚwiatek">#IgaŚwiatek</option>
                <option value="hot16challange">#hot16challange</option>
                <option value="fitness">#fitness</option>
                <option value="krolowezycia">#krolowezycia</option>
                <option value="kryzys">#kryzys</option>
                <option value="ikea">#ikea</option>
                <option value="łódź">#łódź</option>
                <option value="haloween">#haloween</option>
                <option value="kawa">#kawa</option>
                <option value="radom">#radom</option>
                <option value="karmieniepiersia">#karmieniepiersia</option>
                <option value="pomidorowa">#pomidorowa</option>
                <option value="COVID19">#COVID19</option>
                <option value="nvidia">#nvidia</option>
                <option value="poniedziałek">#poniedziałek</option>
                <option value="biedronka">#biedronka</option>
            </NativeSelect>
        </FormControl>
    )
}

export default HashtagPicker;