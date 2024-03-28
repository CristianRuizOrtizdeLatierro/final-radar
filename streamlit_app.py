import streamlit as st
import pandas as pd
import math
from pathlib import Path

import numpy as np
import altair as alt
from funciones import funcion_colores_params
from scipy import stats
from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP Dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

# @st.cache_data
# def get_gdp_data():
#     """Grab GDP data from a CSV file.

#     This uses caching to avoid having to read the file every time. If we were
#     reading from an HTTP endpoint instead of a file, it's a good idea to set
#     a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
#     """

#     # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
#     DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
#     raw_gdp_df = pd.read_csv(DATA_FILENAME)

#     MIN_YEAR = 1960
#     MAX_YEAR = 2022

#     # The data above has columns like:
#     # - Country Name
#     # - Country Code
#     # - [Stuff I don't care about]
#     # - GDP for 1960
#     # - GDP for 1961
#     # - GDP for 1962
#     # - ...
#     # - GDP for 2022
#     #
#     # ...but I want this instead:
#     # - Country Name
#     # - Country Code
#     # - Year
#     # - GDP
#     #
#     # So let's pivot all those year-columns into two: Year and GDP
#     gdp_df = raw_gdp_df.melt(
#         ['Country Code'],
#         [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
#         'Year',
#         'GDP',
#     )

#     # Convert years from string to integers
#     gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

#     return gdp_df

# gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: GDP Dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
'''

# Add some spacing
''
''

# min_value = gdp_df['Year'].min()
# max_value = gdp_df['Year'].max()

# from_year, to_year = st.slider(
#     'Which years are you interested in?',
#     min_value=min_value,
#     max_value=max_value,
#     value=[min_value, max_value])

# countries = gdp_df['Country Code'].unique()

# if not len(countries):
#     st.warning("Select at least one country")

# selected_countries = st.multiselect(
#     'Which countries would you like to view?',
#     countries,
#     ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

# ''
# ''
# ''

# # Filter the data
# filtered_gdp_df = gdp_df[
#     (gdp_df['Country Code'].isin(selected_countries))
#     & (gdp_df['Year'] <= to_year)
#     & (from_year <= gdp_df['Year'])
# ]

# st.header('GDP over time', divider='gray')

# ''

# st.line_chart(
#     filtered_gdp_df,
#     x='Year',
#     y='GDP',
#     color='Country Code',
# )

# ''
# ''


# first_year = gdp_df[gdp_df['Year'] == from_year]
# last_year = gdp_df[gdp_df['Year'] == to_year]

# st.header(f'GDP in {to_year}', divider='gray')

# ''

# cols = st.columns(4)

# for i, country in enumerate(selected_countries):
#     col = cols[i % len(cols)]

#     with col:
#         first_gdp = first_year[gdp_df['Country Code'] == country]['GDP'].iat[0] / 1000000000
#         last_gdp = last_year[gdp_df['Country Code'] == country]['GDP'].iat[0] / 1000000000

#         if math.isnan(first_gdp):
#             growth = 'n/a'
#             delta_color = 'off'
#         else:
#             growth = f'{last_gdp / first_gdp:,.2f}x'
#             delta_color = 'normal'

#         st.metric(
#             label=f'{country} GDP',
#             value=f'{last_gdp:,.0f}B',
#             delta=growth,
#             delta_color=delta_color
#         )


# # Page title
# st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
# st.title('📊 Interactive Data Explorer')

# with st.expander('About this app'):
#   st.markdown('**What can this app do?**')
#   st.info('This app shows the use of Pandas for data wrangling, Altair for chart creation and editable dataframe for data interaction.')
#   st.markdown('**How to use the app?**')
#   st.warning('To engage with the app, 1. Select genres of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')
  
# st.subheader('Which Movie Genre performs ($) best at the box office?')

# Load data
df = pd.read_csv('data/dfc.csv')

# Input widgets
## Name selection
name_list = df['Jugador'].unique().tolist()
name_selection = st.selectbox('Seleccione una opción:', name_list)
print(name_selection)

## Stats selection
stats_list = df.columns[15:].tolist()
stats_selection = st.multiselect('Select stats', stats_list)
print(stats_selection)

# df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
# reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
# reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# # Display DataFrame

# df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
#                             column_config={"year": st.column_config.TextColumn("Year")},
#                             num_rows="dynamic")
# df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

df_jugador = df[df['Jugador'] == name_selection]
columnas_plot = [i+'_percentil' for i in stats_selection]
values = df_jugador[columnas_plot].values.tolist()[0]
custom_values_text = [str(value) for value in df_jugador[stats_selection].values.tolist()[0]]

# # color for the slices and text
slice_colors = funcion_colores_params(stats_selection,columnas_plot)
text_colors = ["#F2F2F2"] * len(stats_selection)

# # instantiate PyPizza class
baker = PyPizza(
    params=stats_selection,                  # list of parameters
    background_color="#EBEBE9",     # background color
    straight_line_color="#EBEBE9",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    last_circle_lw=0,               # linewidth of last circle
    other_circle_lw=0,              # linewidth for other circles
    inner_circle_size=5            # size of inner circle
)

# plot pizza
        
fig, ax = baker.make_pizza(
    values,                          # list of values
    figsize=(10, 11),                # adjust figsize according to your need
    color_blank_space="same",        # use same color to fill blank space
    slice_colors=slice_colors,       # color for individual slices
    value_colors=text_colors,        # color for the value-text
    value_bck_colors=slice_colors,   # color for the blank spaces
    blank_alpha=0.4,                 # alpha for blank-space colors
    kwargs_slices=dict(
    edgecolor="#F2F2F2", zorder = 2, linewidth=1
),                               # values to be used when plotting slices
    kwargs_params=dict(
        color="#000000", fontsize=11,
        #fontproperties=robotto_regular.prop, va="center"
    ),                               # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=11,
        bbox=dict(
            edgecolor="#000000", facecolor="cornflowerblue",
            boxstyle="round,pad=0.2", lw=1
        )
    )                               # values to be used when adding parameter-values
)

texts = baker.get_value_texts()
for i, text in enumerate(texts):
    text.set_text(custom_values_text[i])

# add title
fig.text(
    0.515, 0.975, f"{df_jugador['Jugador'].iloc[0]} - {df_jugador['Equipo'].iloc[0]}", size=25,
    ha="center", color="#000000"
)

# add subtitle
fig.text(
    0.515, 0.953,
    f"Percentiles vs. {df_jugador['Position principal'].iloc[0]} | 2 RFEF Grupo II",
    size=13,
    ha="center", color="#000000"
)

# add text
fig.text(
    0.28, 0.925, "Generales         Pases           Defensiva         Ataque", size=14,
     color="#000000"
)

# add rectangles
fig.patches.extend([
    plt.Rectangle(
        (0.25, 0.9225), 0.025, 0.021, fill=True, color="#1a78cf",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.405, 0.9225), 0.025, 0.021, fill=True, color="#ff9300",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.53, 0.9225), 0.025, 0.021, fill=True, color="lightblue",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.68, 0.9225), 0.025, 0.021, fill=True, color="#d70232",
        transform=fig.transFigure, figure=fig
    ),
])
st.altair_chart(fig, use_container_width=True)