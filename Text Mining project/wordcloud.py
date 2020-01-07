
# coding: utf-8

# In[1]:


#i dont know why word cloud is not included in conda
#so pip install wordcloud first if u dont have it
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image

os.chdir('k:/mena')


# In[2]:


#convert pic to rgb data
#i would recommend nothing too complicated
#or you will need to use contour to highlight the shape
# https://github.com/je-suis-tm/graph-theory/blob/master/Text%20Mining%20project/preview/silhouette.jpg
mask=np.array(Image.open('silhouette.jpg'))


# In[3]:


#the same text that is used to do graph traversal
# https://github.com/je-suis-tm/graph-theory/blob/master/Text%20Mining%20project/mid%20east.csv
text=("""Timeline: Algeria's 30 turbulent years 
Netherlands recalls Iran ambassador as diplomatic spat intensifies 
Algerian protesters reject Bouteflika's attempt to calm anger 
Baby boom exacerbates bleak prospects for Iraqi youth 
Defiant Netanyahu paints himself as the besieged saviour 
Bouteflika's offer fails to appease Algeria's protesters
Saudi's Jubeir: 'Too early' to reopen Syria embassy
Trump's 'ultimate deal' faces ultimate failure
Gov't formation in Iraq Kurdish region closer after KDP-PUK deal
Hundreds in Syria's Baghouz 'surrender' amid slowdown in fighting
Syria rebels slow down battle against ISIL to protect civilians
Qatar FM: Doha buying S-400s 'not anyone's business'
Saudi Arabia says it believes Canada to go ahead with arms deal
Barclays bosses fretted over Qatar deal in 2008 fundraising
Rolls-Royce scales back on joining fighter jet project with Turkey's Kale Group
US Jerusalem consulate merges with embassy
Egypt releases award-winning photojournalist
Fleabag returns
U.S. Allies Battle to Oust Islamic State From Final Syrian Outpost
Saudis Prepare to Put Rights Activists on Trial
Israeli Attorney General Lays Out Planned Charges Against Netanyahu
Kushner Pushes Israeli-Palestinian Peace Plan on Middle East Tour
Iran's President Blocks Foreign Minister's Resignation
Despite Pressure From Trump, OPEC Stands Firm on Oil Curbs
Cleric warns against polygamy 'injustice'
Chlorine likely used in Douma attack - OPCW
Final assault on IS in Syria 'begins'
IS in Syria: Last of the caliphate leave Baghuz
'I nearly drowned, now I dream of Olympic glory'
Cairo train crash and station fire kill 25
What was life like for the IS couple?
Algeria protests: The beginning of the end?
How much trouble is Netanyahu in?
Who will take IS fighter and his teenage 'bride'?
Tales from inside the chaos left by IS
All Together Now
ISIS is dying ... but believers in its ideology live on
Can Netanyahu survive his own Trump-style 'witch hunt'?
US-backed forces begin push against ISIS pocket in Syria
Opinion 
This girl survived an airstrike in Syria. Her siblings didn't make it
Saudi sisters trapped in Hong Kong seek visa extension 
MBS 'clampdown' fuels surge in numbers of Saudi refugees
Israel's Benjamin Netanyahu to be indicted on corruption charges
Five-star concierges: The wild requests of the mega-rich
Netanyahu faces charges over ties to business barons 
Barclays ex-chief: Qataris sought state assurance 
Jordan PM calls for 'critical' support from allies 
Saudi Arabia: why jobs overhaul could define MBS's rule 
Algerian fury over ailing Bouteflika drives protests 
Iran's foreign minister remains after president's plea 
Jamal Khashoggi's body likely burned in large oven at Saudi home
'My mission is to ensure nobody can say: I didn't know'
'Decisive battle' against ISIL expected in Syria
""")


# In[4]:


#use the image color to fill the color of word cloud
#i would recommend nothing too complicated
image_colors=ImageColorGenerator(mask)
wordcloud=WordCloud(mask=mask,
                    #to draw the boundary
                    #contour_width=3,contour_color='grey',
                    background_color='white',
                    color_func=image_colors
                     ).generate(text)


# In[5]:


#use dpi to control the resolution
ax=plt.figure(dpi=1000).add_subplot(111)

#display the image of word cloud
plt.imshow(wordcloud)

#remove axis
plt.axis("off")
plt.show()

