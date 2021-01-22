import React, {useState, useEffect} from 'react';
import { NativeSelect, FormControl } from '@material-ui/core';

import styles from './HashtagPicker.module.css'

const HashtagPicker = () => {
    return (
        <FormControl className={styles.formControl}>
            <NativeSelect>
                <option value="all">Wszystkie</option>
            </NativeSelect>
        </FormControl>
    )
}

export default HashtagPicker;