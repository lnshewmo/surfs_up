# SQLite Surf's Up Challenge

## Overview
Purpose:  The client is interested in temperature patterns in Oahu to help inform the success of a proposed new ice cream and surf shop.  Available data from 9 weather stations located in Oahu from 2010-2017 were analyzed using SQLite and SQLalchemy.  The client is specifically interested temperatures during the months of June and December.  A similar past venture in another location was unsuccessful due to unfavorable weather conditions across the winter.   

### Resources
- SQLite: [Hawaii database](https://github.com/lnshewmo/surfs_up/blob/main/hawaii.sqlite)
- SQLalchemy
- Python
- Jupyter Notebook

## Results

### Temperature Statistics
The following tables show the descriptive statistical analysis for 10 years of temperature measurements taken in June vs Dec.
<p align="left">
    <img width="20%" src="https://github.com/lnshewmo/surfs_up/blob/main/june_stats.png">
    <img width="19%" src="https://github.com/lnshewmo/surfs_up/blob/main/dec_stats.png">
</p>   

Key differences in weather between June and Dec:
- The average temperature is 3 degrees warmer in June than December
- The median temperature is 4 degrees warmer in June than December
- Half of the time points for June are between 73 and 77 degrees, and half of the time points for December are between 69 and 74 degrees
- These are modest overall temperature differences, with June being slightly warmer than December

This figure represents the same data as a histogram:

<img src="https://github.com/lnshewmo/surfs_up/blob/main/temp_histogram.png" width="50%">

## Summary

Oahu has an established reputation as a surfing destination with year-round conditions to accomodate surfers of all experience levels.  "Big wave" season typically coincides with the winter months (ho'olio) of November to March, and is host to Oahu's most famous surf competitions.  The data analysis for temperatures during this time support the position that temperatures are only slightly lower in the winter than the summer (1).  The proposed shop will have a surf 'outfitter' component and an ice cream component.  The surf component may be more robust to inclement weather, however is likely that the ice cream component will experience sales that correlate strongly with weather conditions (low temperatures and/or high precipitation resulting in low sales).  


Additional queries:

Using the only the dataset provided:
- Temperatures could be analzyed for the remaining 10 months.
- The same analysis could be performed on precipitation.  
- There is data reported by station.  The station closest to the proposed shop location can be pulled out for analysis.

With additional data:
- If there is an available dataset on ice cream sales volume by temperature, this could be useful to support the sales projections for the proposed surf shop.


### Citations:
(1) ["Surfing Oahu": https://www.bestsurfdestinations.com/surfing-oahu/](https://www.bestsurfdestinations.com/surfing-oahu/)
