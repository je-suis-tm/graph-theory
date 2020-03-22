# Epidemic Outbreak

Recently there has been an epidemic outbreak in Asia. As a data scientist, I keep wondering why it is so difficult to develop a new vaccine and contain the virus. Challenges on Kaggle such as identifying rare animal species are beneficial for both participants and scientific research organizations behind them. Those big pharmaceutical companies may be able to break down big problems into small chunks and outsource to the data science crowd for free. We, data scientists not Messiah, cannot rescue Koala from Australian bushfire or identify the potential Ebola infected in West Africa. And the data, the asset we value the most, leaves a heavy carbon footprint on the planet (because of the server). Yet, crunching number to help the humanity is the least if not the only we can offer. Most of us just pour all our resources to beat S&P500 by several decimals or improve facial recognition on the zminority. Where is the overhyped AI now?

While I was searching for <a href=https://github.com/je-suis-tm/graph-theory/blob/master/k%20core.ipynb>k core</a> graph in my university material, I discovered a module I have never taken called epidemic spreading on complex network. It suddenly struck me that we could apply graph theory to construct an agent-based model. The model would be able to simulate the epidemic outbreak and forecast the potential infected number. That was the least I could contribute to this shitstorm caused by mankind. This project started there.

###### The simulation of epidemic network is created via <a href=https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/gillespie%20algorithm.ipynb>Gillespie Algorithm</a>.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gillespie.gif)

### Non-linear Regression

Before moving onto a random graph, I took a naïve approach to predict the final death toll of novel corona virus by <a href=https://en.wikipedia.org/wiki/Gompertz_function>Gompertz curve</a>. The idea was inspired by an <a href=https://wwwnc.cdc.gov/eid/content/10/6/pdfs/v10-n6.pdf>article</a> on U.S. Centre of Disease Control journal (Emerging Infectious Diseases Vol. 10, No. 6, June 2004, Page 1165). The researchers intended to study the effectiveness of intervention measures during SARS pandemic in 2003. They chose <a href=https://en.wikipedia.org/wiki/Generalised_logistic_function>Richard’s curve</a> (which is a generalized logistic model) of different training data horizon to predict the potential result. Thus, the first step of this project was to replicate the similar result for SARS in 2003. Instead of Richard’s curve, the model took Gompertz curve, a special form of generalized logistic model. Gompertz was designed to study the population in a confined space, which also makes it applicable to examine the spread of a disease. Inevitably, there are other special forms of Richard's curve which are still fit for the purpose. <a href= https://en.wikipedia.org/wiki/Weibull_distribution>Weibull</a>,  <a href=http://www.pisces-conservation.com/growthhelp/index.html?janoschek.htm>Janoschek</a>, <a href=http://www.pisces-conservation.com/growthhelp/index.html?morgan_mercer_floden.htm>Morgan-Mercer-Flodin</a>, <a href=https://en.wikipedia.org/wiki/Von_Bertalanffy_function>von Bertalanffy</a>, <a href=https://mro.massey.ac.nz/handle/10179/14618>Levakovic</a>, <a href=https://www.researchgate.net/figure/Characteristics-of-main-models-fitted-with-the-Hossfeld-growth-equation_tbl2_202038062>Hossfeld</a>, <a href=https://www.researchgate.net/publication/225560632_A_derivation_of_the_generalized_Korf_growth_equation_and_its_application>Korf</a>, etc.

The training data came from <a href=https://www.who.int/csr/sars/country/en>WHO official website</a>. The full script of web scraping and ETL is attached. I have to make a complaint on how inconsistent the format of WHO report is. I probably spent 10 minutes to set up the web scraper and another 30 minutes to design the model and the figure. The data cleansing alone took me several hours. You are free to use the clean spreadsheet as long as you mention it comes from my hours of sweating and swearing.

Initially we look at the cumulated number of cases reported by WHO. The biggest challenge of the model is the data quality (like all the other data science problems). Due to various reasons (cover up, fake number), we exclude China to represent the global impact. We have observed some small bumps and spikes from the actual curve (Taiwan and U.S. discarded some of the cases). They are most likely caused by false positive and false negative. Unfortunately, WHO didn’t revise their old reports after the publish. The retract of cumulated number is really unacceptable.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-exclude%20china-cumulative%20number%20of%20cases.png)

The figures of Hong Kong and Singapore demonstrate a perfect logistic curve. We have to praise the high-quality data provided by these two city states (crown jewels of Asia). The figures also show the early stage of forecast is perhaps overestimated. The result generated by first 30% or 40% training data is way too high. Two reasons could contribute to the phenomenon. One is the exponential growth rate of early stage. It may sound a bit counter intuitive. Gompertz curve is supposed to be a slow start, bonanza in the middle and slow ending. However, governments don’t normally report zero cases to WHO or WHO doesn’t include zero cases. If you look at the first report of WHO, it was issued on March 17th where both Hong Kong and Singapore have more than one case. We may never be able to detect the real early stage. The second reason could be the governments vowed to contain the virus with whatever it took after the initial outbreak. The effect of border seal, immigration check and patient quarantine kicked in. It slowed down the exponential growth rate. The saturation point of the curve shifted downwards accordingly. I sincerely hope it’s the latter reason or a mix of both. We still haven’t found out what really drove SARS away. The hypothesis of heat doesn’t hold as the winter of Singapore is still above 28 Celsius degrees.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-hong%20kong-cumulative%20number%20of%20cases.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-singapore-cumulative%20number%20of%20cases.png)

There are strange cases where the early stage estimation turns out to be optimistic. For Canada, the government changed the definition of infection on May 30th, 2003 which led to a second hike. Pour la France, je ne sais pas ce qui s’est passé, ça a été très rapide. :joy: 

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-canada-cumulative%20number%20of%20cases.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-france-cumulative%20number%20of%20cases.png)

Let’s turn to the final death toll. The similar pattern from the previous cases exists as well.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-exclude%20china-number%20of%20deaths.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-hong%20kong-number%20of%20deaths.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-singapore-number%20of%20deaths.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-sars-canada-number%20of%20deaths.png)

Now that we have showed the model is valid, the same methodology will be used to produce an early forecast for the novel corona virus. The data is still collected from <a href= https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports>WHO situation reports</a>. The format is even worse this time as the data is inside pdf files. Do you know that WHO staff type in every number? They seriously need a technology upgrade. Apart from manually cleansing the data, there is no shortcut. You are still free to use the aggregated data as long as you give me enough credits. Aside from the terrible format, you would notice the change of format and metrics is no coincidence. If you relate it to the visit of WHO chief, I am pretty sure you would get the delicate political message.

Looking at the model, the global infection number may reach to **58K**!! That’s why they say the novel corona virus is more contagious than SARS. Given 39 days, it is going to reach 95% maximum infection number which is about 56K. Please take notice of that the 95% maximum doesn’t imply 95% quantile. I just assume 95% maximum is where the curve exits its exponential growth rate.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-corona-total-confirmed%20cases.png)

Based upon the model, the impact on U.S. or Hong Kong or Taiwan seems quite limited (very skeptical on that). The impact on Singapore is going to be severe. But I am pretty sure Singapore will manage to change the course.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-corona-united%20states%20of%20america-confirmed%20cases.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-corona-hong%20kong-confirmed%20cases.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-corona-singapore-confirmed%20cases.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-corona-taiwan-confirmed%20cases.png)

Currently death only occurs in China. The ultimate death toll in China might be 1280, which is higher than SARS. In proportion to the infection number, estimated case fatality rate is 2% respectively, much lower than SARS. In about 43 days, the whole situation is supposed to quiet down. Let’s pray for those poor souls.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gompertz-corona-china-number%20of%20deaths.png)

In general, this is an early stage pessimistic estimation. Please take it with a grain of salt. So far, I have only managed to obtain 11 available data points from WHO. The model on some of the countries (e.g. Australia, France, Japan) do not even converge. In reality, 90% of the models fail miserably. There is no need to panic from the model projection or take comfort in the low mortality. One thing we should learn from the model. Carpe diem.

###### This chapter is finished on February 1st, 2020. No further updates.

### Dynamic System

Gompertz curve is a naïve but effective approach. It is comprehensive and it can work with simple data structure. But the shortcoming of Gompertz curve is that we need to forecast cumulated infected cases and virus-caused death independently. In reality, they should be intertwined to a certain degree. That is when the classic approach of epidemic modelling, <a href= https://services.math.duke.edu/education/ccp/materials/diffcalc/sir/sir2.html>SIR model</a>, kicks in. This compartmental model is the foundation of the modern epidemiology. It is a dynamic system consisted of three <a href=https://mathinsight.org/ordinary_differential_equation_introduction>ordinary differential equations</a> which represents Susceptible, Infected and Recovered population. It has the capability of mapping out the prevalence and the duration of an epidemic outbreak. The flipside of the coin is too many pre-assumptions and conditions attached.

The model for SARS is quite straight forward. It takes the classic form of SIR model with vital dynamics. As the data is on a daily basis, all rates inside the model are daily rates. In some literatures, S, I and R takes the form of extensive rather than intensive variables. Here, S, I and R are the actual numbers instead of proportions inside a population.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-sir%20model%20vital%20dynamic.PNG)

The susceptible exposure S of any given time t is determined by three factors. The first is the crude birth rate α of all the living population (including the infected ones). It is based upon <a href= https://wwwnc.cdc.gov/eid/content/10/2/pdfs/v10-n2.pdf>a case</a> recorded on U.S. Centre of Disease Control journal (Emerging Infectious Diseases Vol. 10, No. 2, February 2004, Page 345), which the pregnant mother infected with SARS delivered a healthy enfant. Whether it was due to the dedication of the health care workers or the contagion limit of the virus, we assume the virus cannot pass from the infected parents to the next generation. As long as you are not six feet deep under, you can deliver a healthy child, sadly another susceptible target. So far, there is no evidence suggesting the immunity can pass onto the second generation. Therefore, the inclusion of recovered patients is necessary. The second factor is the crude death rate γ on the susceptible exposure S. The cycle of life and death is inevitable even if you don’t get infected with virus. The third factor is the infection rate β. It quantifies the possibility of converting a susceptible individual to an infected patient. The conversion should be proportional to the respective numbers of S and I in the population.

The infected population I of any given time t is what we care the most. Aside from the conversion from S, there are two other factors. One factor is the recovery rate ε. Patients with good immune system and scientific treatment shall recover at the given rate ε. The other is the grim reaper. The deadly virus could take lives by fatality rate δ, of course. The disputed part is crude death rate γ. Without the virus, those who could have become the infected population can still die from a natural cause. Everybody in our system regardless of gender and ethnicity is equal to Anubis. Assuming a 90-year-old grandma with diabetes complications, she is about to die in the next 7 days. Two days later, his grandson who carries SARS but shows no symptoms passes the virus to her. After another five days, grandma passes away with respiratory infections. What is the cause of death diagnosis then? As you can see, it is difficult for the hospital to note the distinction between virus-caused death and non-virus-related-death. There is nothing wrong to provide a counter argument to challenge this assumption. If you intend to remove crude death rate γ from the infected population I, you must change the calculation of R null as well.

The recovered patients R of any given time t involves the conversion from I. In SIR model, the underlying R will obtain lifetime immunity from the virus after recovery. You may wonder why crude death rate γ does not play a role in the recovered patients. In theory, it should. In fact, recovered patients are not closely monitored after they pose no virus threat to the general public. Sadly, their death does not exist in WHO reported numbers.

The recovered patients R of any given time t involves the conversion from I. In SIR model, the recovered patients R will obtain lifetime immunity from the virus after recovery.

The last one, virus-caused death D, is not explicitly stated in the dynamic system. It is impacted by the number of the infected population I and the virus fatality rate δ.

The model we use for SARS is a deterministic model without stochastic features. SIR model has many variations such as SIS (where recovered patients can still get infected due to virus mutation), SEIR (the virus targets at people with certain genes or features, people don’t immediately get infected after exposure for various reasons), etc. You will find more models at <a href=https://institutefordiseasemodeling.github.io/Documentation/general/model-overview.html>Institute for Disease Modelling</a>. There are plenty of literatures on SARS epidemic modelling with more advanced models. They introduce other variables like quarantined patients and super spreaders. You will find them in the further reading section. Truth be told, the choice of SIR comes from the constraint of the data. Data is the new oil, no? At the current stage, there is only so much offered by WHO.

Now that we have set up the differential equations in the dynamic system, we should get hands on the modelling. Crude birth rate α  and crude death rate γ are acquired from <a href=http://data.un.org>United Nations Statistics Division</a>. This is one of the best databases and datamarts I have ever seen across all the free data sources. In contrast to WHO, UN deserves some kudos for the clean-cut CSV format. Though we need to convert α and γ from annual rate to daily rate before leveraging them. Thus, the unknown parameters are infection rate β, fatality rate δ and recovery rate ε. They will be estimated by non-linear least square method. The objective is to minimize the cost function, sum of squared standardized error, by <a href=https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method>Nelder-Mead algorithm</a>.
  
The perfect match of in-sample data for Hong Kong and Singapore is splendid. Both recovered patients R and virus-caused death D surge. However, the dynamic system seems to miss the late spike of currently infected population I before its downfall. Unfortunately, WHO didn’t keep track of recovery data until April 4th, 2003. Typically, we can never get the data dated back to the real T0. This is the result of modelling on data from T+N. The fatality rate δ of both is approximately 2%. The underlying δ implies about 2% of the infected population I dies from the virus every day.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-hong%20kong-in%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-singapore-in%20sample.png)

The <a href=https://en.wikipedia.org/wiki/Basic_reproduction_number>basic reproduction ratio</a> R0 for Hong Kong and Singapore are 0.5 and 0.7. R0 refers to the expected infected individuals of the next moment when only one infected person occurs in the entire population. R0 larger than 1 is the pre-condition of an epidemic outbreak. As our simulation begins in the middle of the process, no wonder we observe a relatively small R0. The table in Wikipedia suggests R0 for SARS should oscillate between 2 and 5.

The basic reproduction ratio R0 of our model can be derived from the following steps.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-sir%20model%20r0.PNG)

The case of North America is slightly off the track. As mentioned earlier, any change of definition or retraction will lead to a spike or a dip, which has an overwhelming impact on the model. The daily fatality rate δ for U.S. is 3%, a bit higher than 2% for Canada. The basic reproduction ratio R0 for both are roughly the same, 0.7 and 0.6.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-canada-in%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-united%20states-in%20sample.png)

The in-sample data for ASEAN countries are also fantastic. The dynamic system precisely captures S, I and R. Even though D is not in the differential equations, it is still within marginal errors. The daily fatality rates δ for Viet Nam and Malaysia are 4% and 3%. You can argue it is caused by the poor local health infrastructure. R0 is an odd case here. For Viet Nam, it is only 0.2, but it is 0.7 for Malaysia.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-viet%20nam-in%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-malaysia-in%20sample.png)

The only country we test for EMEA region is France. As shown in the figure below, the dynamic system works quite well in general. The underlying δ stays at the range from 2% to 3%. It is rather consistent across different countries. The basic reproductive ratio R0 is about 0.6 which is aligned with other countries.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-france-in%20sample.png)

Okay, now comes the real deal, out-of-sample data. The result is quite the same as Gompertz curve. Using only a small percentage of the data is often an overestimation except for one country. Anglo-Saxion exceptionalism is something we hear all the time. Nevertheless, Francophonie exceptionalism in epidemic modelling is really astonishing (c'est toujours comme ça:joy: )!

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-hong%20kong-out%20of%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-singapore-out%20of%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-canada-out%20of%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-united%20states-out%20of%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-viet%20nam-out%20of%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-malaysia-out%20of%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-sars-france-out%20of%20sample.png)

Before we move onto the novel corona virus, you may ask me why we don’t test the global impact this time. Regrettably, the biggest trouble is to get a pair of initial values for the function to converge. I tried a 10k random number simulation. My machine kept working all night long while I was dozing off. Yet, the result still brought no morning glory to me. If you have found a great choice, be sure to let me know!

The case of novel corona virus has much more issues with the data. Given the fact that the event is not far from the beginning, there are few cases where the patients are fully recovered. I cannot accuse WHO of limited data variety and length. Hence, our SIR model must be simplified into SI model. In SI model, we cannot simulate the recovered patients. Once you get infected, the only way out is to kick the bucket. As unscientific and unethical it sounds, it is the only feasible model at the moment.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-si%20model%20vital%20dynamic.PNG)

The consequence of the model switch is also severe. The daily fatality rate δ of novel corona virus is likely to be exaggerated because it is equal to the true value of δ plus the hidden daily recovery rate ε. Additionally, the susceptible population S is likely to be underestimated because the removal of crude birth rate α on recovered patients R. R0 is theoretically unbiased in spite of all those effects. The increase in δ shall offset the vanish of ε in the denominator.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-si%20model%20r0.PNG)

The overnight jump of clinical diagnosed patients on February 13th, 2020 really distorted the whole model (top notch data quality from China as always). The daily fatality rate δ is only 0.3% despite being amplified by the hidden recovery rate ε. With that being said, novel corona virus is indeed a gentle killer. Nonetheless, R0 for China is shockingly 63.3!! With that basic reproduction ratio, the mad spread of the disease can easily wipe out more lives than SARS. If you look at the bottom right, the balance state indicates only very few people will stay uninfected in the end. Luckily there are hidden factors we ignore. One is the death number D also includes the recovered patients R. The other is the lockdown of several regions which greatly reduces the underlying S (with sufficient data we can construct SEIR model to monitor the exposed population E). Otherwise, this is not an epidemic outbreak, it is a bioweapon in Racoon City.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-china-in%20sample.png)

The data of Hong Kong and Singapore is like quantum entanglement. The underlying δ for both are 0.5% and 0.4% where there is a confirmed death in HK. In that sense, we can assume the daily recovery rate ε for both city states should converge to 0.4%. This is based upon the assumption that no death has occurred in Singapore yet and both city states are homogenous. On the contrary, the underlying ε for SARS ranges from 3% to 10%. As in the early stage, no effective treatment has been found. 0.4% sounds like a reasonable number. The R0 for both are 41 and 57 which seems a bit dramatic. As stated by Wikipedia, the current estimate of R0 is about 1.4 to 6.6. The prophecy of the crystal ball is that the susceptible population S could plunge like freefall in mid-March and infected population I could peak in mid-April. Well, this is purely based on the assumption of no recovery and no government intervention.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-hong%20kong-in%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-singapore-in%20sample.png)

In North America, the numbers look more reasonable. The underlying δ is 4% for Canada and 2% for U.S. But the death still hasn’t knocked on their doors. Does it mean the potential daily recovery rate ε is about 3%? R0 for both are 4 and 8 respectively which echoes the result from Wikipedia. The crystal ball is hard to tell. A much smaller R0 still doesn’t protect the majority from the virus. Things could get worse in June and peak in July. The good news is, unlike the previous three countries in Asia, the peak of the infected number I doesn’t converge to the susceptible exposure S. My interpretation is that the death toll D is more likely to be the number of recoveries R.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-canada-in%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-united%20states%20of%20america-in%20sample.png)

ASEAN countries show similar properties as North America. The underlying R0 for Viet Nam and Malaysia are 6 and 7. They fluctuate around the upper bound of Wikipedia forecast. Supposedly this could be the real R0 for novel corona virus. Daily fatality rate δ for both are 2% with no actual casualty. This further confirms our speculation of 3% daily recovery rate ε.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-vietnam-in%20sample.png)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-malaysia-in%20sample.png)

The last case is France with δ at 2% and R0 at 4. The numbers don’t tell anything interesting but France always surprises me. The first virus-caused death in Europe speaks a lot about the local health infrastructure.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/differential-corona-france-in%20sample.png)

One of the most prominent features of the projections above is the susceptible population S will fall to the very low eventually (the reasons behind were explained earlier). This reminds me of the <a href=https://www.bloomberg.com/news/articles/2020-02-13/coronavirus-could-infect-two-thirds-of-globe-researcher-says>article</a> on Feb 13th, 2020. A WHO adviser claimed two-thirds of the world’s population could catch the virus. At first, I laughed it off. I mean, dude, come on? When I finished the dynamic system, I ain’t laughing any more. Without global collaboration and transparent governance, the likelihood of the extreme scenario is pretty high.

There is another common feature among the projections predictions above. All the fitted infection number I overestimate the situation. Is the model being too pessimistic? From our previous study on SARS, we always observe an overestimation in the early stageof 30% or 40% training data. Except on novel corona virus, Gompertz curve done on February 1st, 2020 underestimated all the numbers back on February 1st, 2020. Right now, we should be very cautious with the result. Next thing you know, it this shitstorm may turn to a pandemic outbreak.

Recently Amid the current outbreak, I have been reading a lot of stories about bats, snakes and pangolins from Le Parisien. What did they do to cause the global crisis? Can we blame Uranium-235’s half-life for what happened in Chernobyl?

###### This chapter is finished on February 18th, 2020. No further updates.

### Agent-based Model

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/graph-sars-sir%20model%20vital%20dynamics.PNG)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/graph-sars-sir%20model%20r0.PNG)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/graph-corona-si%20model%20vital%20dynamics.PNG)

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/graph-corona-si%20model%20r0.PNG)
