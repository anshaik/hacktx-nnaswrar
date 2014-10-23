---------------------------------------------------------
#### Introduction

Our group’s members are people who love to travel (and have lots of reasons to do so); but we're also students who need to stay healthy and fit for school as well as informed people who want to use the internet to get the heads up on the places we go to. 

---------------------------------------------------------

#### What does Threat Wire do?

Threat Wire is a platform that allows users to view and submit reports of communicable diseases at the location of their choosing; it then creates a custom Threat Score based on the number of reportings near the selected location, the  contagiosity of the disease in question, as well as the user’s profile (student, health worker, retiree who doesn’t leave home much). The Threat Score allows you to make a quick and informed decision about what you should do in the interest of safety, and enables you to share your information with other Threat Wire users.

* **Computes threat level through various metrics**
* **Graphically displays threat levels**
* **Provides self-reporting channel**
* **Threat detailed breakdown by country/region/city**

---------------------------------------------------------
#### _The Technology_

* Python+Flask
* HTML5, CSS, JavaScript
* Multiple APIs

---------------------------------------------------------

#### _The Data_

Utilizing various API's, we generate the data needed to power ThreatWire. From the [Mashery APIs](http://developer.mashery.com) we used the [USA Today](http://developer.usatoday.com/) API. To power e-mail integration, we used both [Context.io](http://context.io/) and [SendGrid](https://sendgrid.com/). For additional data points, we used [Google Trends](http://www.google.com/trends/).


---------------------------------------------------------

#### _The UI_

The UI was designed in Adobe Illustrator and built in HTML5, CSS, and JavaScript. 

*Home Page*: the first page users sees on logging on to ThreatWire, known as the Threat View. The user has three options: drill down on a continent, report sickness ("I'm sick!"), and search for a location relevant to the user ("Look for threat rates in"). 


![index.html ](https://raw.githubusercontent.com/anshaik/hacktx-nnaswrar/master/submission/hackt_tx_ui.png)

*Report disease page*: users self-report when infected by an infectious disease. Three pieces of information are provided; current location (may be auto filled by location services or set manually), type of disease, and level of exposure to the public (i.e. student, healthcare worker, retiree). 


![Page 2 ](https://raw.githubusercontent.com/anshaik/hacktx-nnaswrar/master/submission/hackt_tx_ui_2.png)

*Disease report page*: shows an example of a detailed reports page. Detailed reports can be viewed for regions, countries, and cities. 

![Page 3 ](https://raw.githubusercontent.com/anshaik/hacktx-nnaswrar/master/submission/hackt_tx_ui_3.png)

*Mobile view*:

![iPhone Example ](https://raw.githubusercontent.com/anshaik/hacktx-nnaswrar/master/submission/hacktx_main_iPhone.PNG)


---------------------------------------------------------

#### _The Team_

Noemie Nakamura; Texas A&M University
Anna Reiter; UT Dallas
Will Retzloff; UT Dallas
Adil Shaikh; UT Dallas
