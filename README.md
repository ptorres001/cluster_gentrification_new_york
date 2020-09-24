# Detecting Gentrification in the Neighborhoods of New York City
## By Paul Torres

The goal of this project is to build a model that will be able to detect which neighborhoods are undergoing the process of gentrification. 

## Project
The demographic makeup of neighborhoods in New York City can change dramatically in the years between the decennial national census'. Over the most recent decades, it has occurred because New York City has rebounded from the disastrous 1970's and areas have become desirable again. This means that what were once under served communities have become hotspots for development and expansion of upscale living. This phenomenon is known as gentrification. 


## Overview
Using compiled U.S. Census Data and American Community Survey Responses, I calculated the percentage change in each demographic category. These percent changes were then used to determine how the makeup of each census tract changed over the course of ten years from 2000 to 2010. 

Next, came the clustering of census tracts. Using the features, both given and engineered, I ran the observations through several algorithms in order to determine the best way to cluster them in order to determine gentrification status. 


## Repository Structure
- Images -- contains images created during EDA and those linked in README
- 01_Data_Cleaning_Processing -- contains all of the data cleaning steps and techniques with markdowns explaining reasoning
- 02_EDA -- exploring all of the features and how they affect each other. 
- 03_Clusters -- contains all the code that determine the gentrification level of census tracts while looking at other census tracts with similar feature levels
- 04_Classifying -- on a parallel track, determining the gentrification level using predetermined metrics established in academic papers. These metrics will be the real values with which I compare my algorithm

## Business Case
Gentrification leads to displacement of whole communities that are under represented in local politics and most at risk for poverty related complications. A model that can identify a neighborhood at risk for gentrification would allow interested groups to reallocate resources to prevent displacement. A method that would be able to do so with the provided data would be helpful to community groups and government agencies to help those at risk for displacement.

- Who would this model serve?  
        1. Stakeholders include residents that are in areas that are susceptible to gentrification.  
        2. Community groups that exist to empower residents to battle gentrification.  
        3. Government agencies tasked with keeping housing affordable in under served communities.  

- What does this model take into account?  
        1. The model tracks the trends in neighborhoods that have gentrified and compares them with current neighborhoods.  
        2. While full counts of demographics may seem useful, it is actually more important to use the percent changes of each of the demographic categories.  
        3. Through feature selection and determining feature importance, I will try and conclude what changes in the demographic is more important in determining gentrification. 


## Data
The data used to determine the classifications was obtained from Longitudinal Tract Database (LTDB) and the United States Census Bureau. Both full count data and sample data was used in this project. 

## Preprocessing (Data Cleaning & Feature Engineering)

Standard data cleaning in order to fill in missing values, dispose of observations that were heavily flawed, and remove observations that did not include residential areas but were in fact parks, prisons, or heavily commercial areas.  
  
The next step was to change the actual counts of the data to percentage counts. This included calculating the percentage each demographic and housing type existed in each census tract. This process was repeated for the full count and sample data for both 2000 & 2010.  
  
Finally, I created percent changes between the two census years. The increase or decrease of a sub-group is the most important for gentrification metrics. 

## Exploratory Data Analysis

First, we took a cursory glance at the distribution of population changes from 2000 to 2010. 

![Pop Change Distribution](Images/Population_change_dist.png)

As you can see, the distribution is centered about zero with tails on either side. There are a lot more extreme outliers in the positive direction. 

While informative about the overall population growth, it doesn't speak on the make up of the different census tracts. First, we take a look at the changes based on race. For clarity, we grouped non-white populations together. 

![Pop Change By Race](Images/count_positive_race_pop_changes.png)

The graph above is a count of all of the census tracts that have seen an increase in white and non-white populations. From this data, we see that there is an increase in non-white populations in more census tracts –– which goes against what you would expect from a gentrifying city. However, let's raise the bar. 

![Pop Change By Race 50%](Images/50_increase_count_race_pop_changes.png) ![Mean Pop Change](Images/mean_increase_count_race_pop_changes.png) 


From the graphic on the left, we can see that when the bar raises from any increase to 50% or more there is a large difference in the amount of white vs non-white populations. We should take this to mean that while there are small increases in non-white populations across the census tracts, there is a more focused increase to certain areas for white populations. The graphic on the right shows us the mean change in population increase. Changes in the white population averaged around 40% and the non-white population averaged around 12%. 