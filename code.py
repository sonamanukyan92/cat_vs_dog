#!/usr/bin/env python
# coding: utf-8

# <b> A Steady Passion For Pets?! US Dog and Cat Population

# The dataset has been taken from Tableau public datasets page. It shows the survey results about population and ownership by a household of dogs and cats broken down by states. The survey was conducted by American Veterinary Medical Association and the dataset includes columns such as 'Number of Households, 'Number of Pet Households', 'Dog Owning Households', 'Cat Owning Households', summarised for each state.
# <br>This visualization can help businesses that offer products and services for pets, to predict how much they might be able to sell. Also, Veterinarians need to know how many patients to expect, and veterinary schools must determine enrolment numbers and course offerings.

# In[1]:


from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')


# In[2]:


get_ipython().run_cell_magic('javascript', '', 'IPython.OutputArea.prototype._should_scroll = function(lines) {\n    return false;\n}')


# In[3]:


import pandas as pd
df = pd.read_excel('catsvdogs.xlsx')


# Cat and Dog population varies across states. Households in Texas, Tennessee, Arizona, Missouri, Georgia are the most likely to include dogs. While Households in New York, Pennsylvania, Ohio, Maryland, Massachusetts are the most likely to include cats.

# In[4]:


colors = {'dog (high)':'rgb(27, 158, 119)',
          'dog (moderate)':'rgb(102, 194, 165)',
          'cat (high)':'rgb(152, 78, 163)',
          'cat (moderate)':'rgb(222, 203, 228)',
          'almost equal':'rgb(255, 255, 204)'}
import plotly.express as px
fig = px.choropleth(df, 
                    locations='state', 
                    locationmode="USA-states", 
                    scope="usa", 
                    color="Population Majority Cat vs Dog",
                    color_discrete_map=colors, 
                    #range_color=(0, 3), 
                    #color="Mean Number of Dogs per household",
                    labels={'Population Majority Cat vs Dog':'Cat vs Dog Popularity'},
                    hover_name="Location", 
                    hover_data=["Cat Population (in 1000)",
                                "Dog Population (in 1000)"], 
                    title="US Dog and Cat Population by Popularity")

#fig.update_layout(height=600, width=800)
fig.show()


# <b>The average American family owns 1.6 dogs and 2 cats.</b>

# The chart shows the percentage of pet owner households by state sorted in descending order. The colour categories stand for households who own only dogs, only cats, or both. Vermont households are the most likely to include pets. In almost all states ownership ranges from 50 per cent to 70 per cent of households and in almost all states, over half of households include at least one pet.

# In[5]:


colors = {'only dog':'#00CC96',
          'only cat':'#AB63FA',
         'both dog and cat':'#FFA15A'}

fig = px.bar(df, y="Location", 
             x=["Only Dog(s)", 
                "Only Cat(s)",
                "Both Dog(s) and Cat(s)"],
             range_x=[0, 100], labels={'value':'Percentage', 'Location':'State', 'variable':'Category'},
             color_discrete_map=colors,
             hover_data=["Percentage of households with pets", "Number of Households (in 1000)"],
             title="65,787,000 Households or 56.9% own at least one pet",
             orientation='h').update_yaxes(categoryorder="total ascending")
             #, How Many Housholds Have Pets in the USA Percentage of Households owning Dog, Cat, or Both, color='continent', barmode='group', hover_data=['continent', 'country'], title='Monthly New Cases by Continent')
#fig.update_traces(colorscale=colors)
fig.update_layout(height=600, width=800)
fig.show()


# Link to GitHub repo: https://github.com/sonamanukyan92/cat_vs_dog
