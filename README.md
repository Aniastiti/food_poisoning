<h1> Food Poisoning Across the United States </h1>

Hi There,

Thank you for visiting my project looking into food poisoning (food borne illness) across the United States with a data set that covers a time period from 1998-2015. 


**** <b>Regarding the information in this data set, please read the following disclaimer by the CDC.</b> <i>Data available via FOOD Tool originate from a dynamic outbreak surveillance database. Reporting agencies (state, local, territorial, and tribal health departments, and CDC) can modify their reports at any time, even months or years after an outbreak. Therefore, FOOD Tool results are subject to change. FOOD Tool was last updated on 9/1/2016; this date is recorded in the "Last Transfer Date" field in the downloaded file.

Source: https://wwwn.cdc.gov/foodborneoutbreaks/</i>****




-------------------
<h3><u>The Goal</u></h3>

<font color = blue>**Why are we here?**</font>

* <font color = red>Goal 1:</font> <i>Identify most common location of food borne illness</i>
* <font color = red>Goal 2:</font> <i>Identify which states are most likely to have food borne illness </i>
* <font color = red>Goal 3:</font> <i>Which food is most likley to be connected to food poisoning? </i>

-------------------
<h3><u>Where Is Our Data Coming From?</u></h3>

* This data is being pulled from data.world.
    * It can be found at the following link. https://data.world/cdc/foodborne-outbreak-database

* This repository also has a CSV of the data available as well

------------------
<H3><u> Project Planning </u></H3>

In addition to this README, you can see my TRELLO project pipeline by visiting the following link: https://trello.com/b/Kl3EAgKD/food-poisoning-project

-------------

<h3><u>Data Dictionary</u></h3>
    
-  Please use this data dictionary as a reference for the variables used within in the data set.



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|   |   |  |





-------------------
 <h3><u>Hypothesis and Questions</u></h3>

- Is illness from food borne illness correlated to state?
- Is there a relationship between hospitalization and state?
- Which type of food poisoning is most prevalent?
- Is food type correlated to illness?
- Is food type correlated to hospitalization?
- Are there states seeing decreasing rates of hospitalization over the years due to food poisoning?
- Are there states seeing rising cases of hospitalization due to food poisoning?

<h5> The questions above will be answered using correlation tests, chi^2 tests and t-tests.</h5>

TBD

--------------------
 <h3><u>How To Recreate This Project</u></h3>
 
 To recreate this project you will need use the following files:
 
 - wrangle.py
 - explore.py
 - model.py
 - food_data.csv or you can acquire it from data.world ---> https://data.world/cdc/foodborne-outbreak-database
 
 Your target variable will be ---- which is defined in the above data dictionary. Please visit my final notebook to see this variable being used.
 
 <b>Step 0.</b> Clone this repo to your local machine with the above files.
 
 <b>Step 1.</b> Import all necessary libraries to run functions. These can be found in each corresponding .py file
 
 <b>Step 2.</b> Use pd.read to bring in the csv file from your local folder. 
 
 <b>Step 3.</b> To see the the cleaned data set before training do the following:
 
```df = clean_df()``` 

After you have gotten to know the data set, run the following to gather the train, validate, test data


    
 
 <b>Step 4.</b> Verify that your data has been prepped using df.head()
 
 <b>Step 5.</b>. Enter the explore phase using the different univariate, bivariate, and multivariate functions from the explore.py file. This is also a great time to use different line plots, swarm plots, and bar charts. The associated libraries to make the charts happen are from matplotlib, seaborn, scipy, plotly and sklearn
 
 <b>Step 6.</b> Evaluate and model the data using different regression algorithms. 
         
         
TBD
 
<b>Step 7.</b> After you have found a model that works, test that model against out of sample data using the function in my notebook.
 
 For a more detailed look, please visit my final notebook for employee classification for further assistance.
 
--------------------



<h3>Key Takeaways, Recommendations, & Next Steps</h3>

Through this classification project I came away with the following <b> key takeaways</b>:

TBD

<b>Recommendations & next steps</b>:

TBD

-----
