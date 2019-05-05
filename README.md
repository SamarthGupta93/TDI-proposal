# TDI-proposal
The Data Incubator - Propoject proposal - Statistical/Predictive analytics of online Job postings for job seekers

Online job postings are an important part of any professional seeking for a change in job or starting as a fresher. Every professional has gone through a phase where he/she has asked self:
1)	Is this the right time for job application?
2)	Which country/state/region has the best job opportunities for my domain?
3)	I want to switch from Domain A to Domain B. Which companies offer higher opportunities?
4)	How is the current growth of my domain in terms of jobs? Should I be looking for a change in domain? If yes, which one should I target?

The above questions are crucial for making optimal decisions for any professional. However, given that every firm has its own online job board, it is onerous for people to find a definitive solution to such queries and they end up asking other individuals for clarifications which may lead to poor decisions. 

In this project, I propose to create a web application which could provide insights into such intricate queries using statistical/predictive analytics. 

### Dataset 
I have used Thinknum’s job_listing dataset provided to me by The Data Incubator for the preliminary analysis. The dataset contains numerous job postings, each classified into different categories – Engineering, Sales, Financial Services etc. labeled by the “category” column. To explore the feasibility of the project, we work on one of the categories for the preliminary analysis labeled as “Engineering”.

### Preliminary analysis
For our preliminary analysis, we work on the “Engineering” job category of our dataset. The whole dataset is divided into seven parts. We extract the “Engineering” category from all the seven parts to create our filtered dataset of over 1.3 M entries.
The “Engineering” dataset contains job postings from Jan-2017 to Jul-2018 (as evaluated from “as_of_date” column). 

**Analysis 1**: We group the postings by each month and plot the total postings for every month starting from Jan-2017 to Jul-2018. 
Key Observations:
1)	We observe two major peaks in the graph – Jun-2017 and Mar-2018. 
2)	Most jobs are posted in the first half of the year. This insinuates an optimal time of the year for job seekers.
3)	The number of engineering job in 2018 has greatly increased as compared to 2017. This reflects the growth in the domain.

![alt text](/engineering_job_per_month.png)

**Analysis 2**: In this analysis, we explore the regional aspect of the Engineering jobs. We first group our dataset by “year”. Next, we group each year data by “country”. It is seen that USA has the leading number of online job postings followed by India and China. This is trivial as our dataset contains the firms listed in NYSE and NASDAQ which are both American stock exchange. Hence, we continue our analysis and work on a filtered dataset containing the “USA” job postings.  The filtered dataset contains 814,264 entries.
We group our dataset by “year” followed by “region” (States in USA). 
Key observation:
1)	In 2017, California had the maximum engineering job postings (32.7% of the total) followed by Iowa (8.5%) and Viriginia (7.4%). 
2)	In 2018, Washington (53.5%) surpassed California (17.9%) creating about triple the number of job postings. A deeper analysis into the dataset shows that a majority of the new job postings in WA were created by Microsoft. This hints a probable expansion of the Microsoft Washington campus, an insight which could be crucial for engineers aiming to work in the firm.
3)	California has about similar and high number of job postings in both 2017 and 2018, indicating a stable and major region for job seekers.

![alt text](/engineering_job_by_state.png)

### Conclusion
The preliminary analyses show that there are non-trivial trends in the job postings. It can detect major regions for a job category, the growth of the domain, optimal time of the year for job applications and many other key information. It can also reflect if a firm has increased its intake over the past few months or expanded to a new state. The analyses could be further detailed by including/comparing multiple domains and other statistical/predictive analyses. All this information can be vital for job seekers and needs to be evaluated in order to make an informed choice.
