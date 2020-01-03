
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import matplotlib.animation as animation
from IPython.display import HTML


# In[3]:
df = pd.read_csv('endorsements.csv')


# In[4]:


df.head()


# In[5]:


df.groupby('won_primary')['money_raised'].count()


# In[6]:

df.year.unique()
# This is the last frame that i want my audience to see which is the 2012 results

# In[28]:


latestyear = 2012
# Use eq() function to test for equality between a data frame object and a series object

dff = (df[df['year'].eq(latestyear)].sort_values(by='money_raised', 
        ascending = True).head(10))
dff


# Make fig and ax object using matplotlib
# horizontal ax with candidates name and money raised 

# laying out basics

# In[21]:
fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(dff['candidate'], dff['money_raised'])


# In[24]:


df.party.unique()


# make colors dictionary 

# In[25]:


colors = dict(zip(['Republican', 'Democratic'],['#EE3B3B', '#00BFFF']))
group_lk = df.set_index('candidate')['party'].to_dict()


# In[26]:


fig, ax = plt.subplots(figsize=(15, 8))
dff = dff[::-1]   # audience view the money_raised DESC
# pass values to color=`
ax.barh(dff['candidate'], dff['money_raised'], color=[colors[group_lk[x]] for x in dff['candidate']])
# interate the values
for i, (money, candidate) in enumerate(zip(dff['money_raised'], dff['candidate'])):
    ax.text(money, i,     candidate,            ha='right') # candidate 
    ax.text(money, i-.25, group_lk[candidate],  ha='right') # party group
    ax.text(money, i,     money,           ha='left')  

    
# add year on the canvas on the right 

ax.text(1, 0.4, latestyear, transform=ax.transAxes, size=46, ha='right')


# In[32]:


fig, ax = plt.subplots(figsize=(15, 8))
def draw_barchart(year):
    dff = df[df['year'].eq(latestyear)].sort_values(by='money_raised', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['candidate'], dff['money_raised'], color=[colors[group_lk[x]] for x in dff['candidate']])
    dx = dff['money_raised'].max() / 200
    
    # zip function use iterable objects to format the axes 
    for i, (value, name) in enumerate(zip(dff['money_raised'], dff['candidate'])):
        ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
    
   
    # ... all polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'money_raised', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    
    ax.text(0, 1.15, 'Money raised through 6/30 before the primary- 1980 to 2012',
            transform=ax.transAxes, size=23, weight=500, ha='left')
    ##add some notation
    ax.text(1, 0, 'Data sources: FivethirtyEight @ZoeZ', transform=ax.transAxes, ha='right',
             color='#577777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)
    
draw_barchart(2012)


# In[33]:


from IPython.display import HTML
fig, ax = plt.subplots(figsize=(15, 8))

animator = animation.FuncAnimation(fig, draw_barchart,frames=(1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012))
HTML(animator.to_jshtml()) 

# .save as gif or mp4 fps is the speed and dpi is the resolution
animator.save('moneyraise.gif', fps=.5, dpi=200)


# In[ ]:




