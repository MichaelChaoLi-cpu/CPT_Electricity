# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:44:29 2024

@author: Li Chao
"""

import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CPT_result_df = pd.read_csv('Data/JapaneseElectricity.csv')
CPT_result_df['company'] = CPT_result_df['nake_name'].str.split('/').str[1]
CPT_result_df['year'] = CPT_result_df['nake_name'].str.split('/').str[-1].str.split('_').str[-1].str.split('.').str[0].astype(int)

CPT_result_df = CPT_result_df[CPT_result_df['no_valid_file']==False]

CPT_result_df = CPT_result_df[CPT_result_df['year'] > 1999]

CPT_result_df = CPT_result_df[['company', 'year', 'model_i0_index', 
                               'model_i1_index', 'model_i2_index', 'model_i3_index',
                               'model_i4_index', 'model_i5_index', 'model_i6_index', 'model_i7_index',
                               'model_i8_index', 'model_i9_index', 'model_i10_index',
                               'model_i11_index', 'model_i12_index']]
CPT_result_df.columns = ['Company', 'Year', 
                         'Community',
                         'Air Pollution', 'Greenhouse Gas', 'Water Consumption', 
                         'Mining Consumption', 'Work Environment',
                         'Safety and Health', 'Human Rights', 
                         'Governance Risk', 'Production Cost',
                         'Domestic Job Creation', 'Economic Ripple Effect',
                         'Domestic Reflux Rate'
    ]
CPT_result_df = CPT_result_df[['Company', 'Year','Air Pollution', 
                         'Greenhouse Gas', 'Water Consumption', 
                         'Mining Consumption',
                         'Work Environment', 'Community',
                         'Safety and Health', 'Human Rights', 
                         'Domestic Job Creation',
                         'Domestic Reflux Rate',
                         'Governance Risk', 'Production Cost',
                         'Economic Ripple Effect']]

CPT_result_df.sort_values(by='Year', inplace=True)

Kyuden_df = CPT_result_df[CPT_result_df['Company'] == 'Kyuden'].copy()
Kyuden_df = Kyuden_df.drop('Company', axis=1)
Kyuden_df.set_index('Year', inplace=True)

Chubuden_df = CPT_result_df[CPT_result_df['Company'] == 'Chubuden'].copy()
Chubuden_df = Chubuden_df.drop('Company', axis=1)
Chubuden_df.set_index('Year', inplace=True)

Chugokuden_df = CPT_result_df[CPT_result_df['Company'] == 'Chugokuden'].copy()
Chugokuden_df = Chugokuden_df.drop('Company', axis=1)
Chugokuden_df.set_index('Year', inplace=True)

Kanseiden_df = CPT_result_df[CPT_result_df['Company'] == 'Kanseiden'].copy()
Kanseiden_df = Kanseiden_df.drop('Company', axis=1)
Kanseiden_df.set_index('Year', inplace=True)

Okiden_df = CPT_result_df[CPT_result_df['Company'] == 'Okiden'].copy()
Okiden_df = Okiden_df.drop('Company', axis=1)
Okiden_df.set_index('Year', inplace=True)

Rikuden_df = CPT_result_df[CPT_result_df['Company'] == 'Rikuden'].copy()
Rikuden_df = Rikuden_df.drop('Company', axis=1)
Rikuden_df.set_index('Year', inplace=True)

Siden_df = CPT_result_df[CPT_result_df['Company'] == 'Siden'].copy()
Siden_df = Siden_df.drop('Company', axis=1)
Siden_df.set_index('Year', inplace=True)

Toden_df = CPT_result_df[CPT_result_df['Company'] == 'Toden'].copy()
Toden_df = Toden_df.drop('Company', axis=1)
Toden_df.set_index('Year', inplace=True)

Tohokuden_df = CPT_result_df[CPT_result_df['Company'] == 'Tohokuden'].copy()
Tohokuden_df = Tohokuden_df.drop('Company', axis=1)
Tohokuden_df.set_index('Year', inplace=True)


X_colname = ['Air Pollution', 'Greenhouse Gas', 'Water Consumption', 
             'Mining Consumption', 'Work Environment', 'Community',
             'Safety and Health', 'Human Rights', 'Domestic Job Creation',
             'Domestic Reflux Rate', 'Governance Risk', 'Production Cost',
             'Economic Ripple Effect']
sub_order = ['a', 'b', 'c', 'd', 'e', 
             'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm']
fig, axs = plt.subplots(nrows=5, ncols=3, figsize=(21, 29.7), dpi=300)
for i, variable_name in enumerate(X_colname):
    i_row, i_col = i//3, i%3
    text_y = np.max(CPT_result_df[variable_name]) - 0.03 * (np.max(CPT_result_df[variable_name])-np.min(CPT_result_df[variable_name]))
    axs[i_row, i_col].plot(Kyuden_df.index.tolist(), 
                           Kyuden_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=2, color = 'red', 
                           label='Kyushu')
    axs[i_row, i_col].plot(Chubuden_df.index.tolist(), 
                           Chubuden_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=2, color = 'sienna', 
                           label='Chubuden')
    axs[i_row, i_col].plot(Chugokuden_df.index.tolist(), 
                           Chugokuden_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=2, color = 'gold', 
                           label='Chugoku')
    axs[i_row, i_col].plot(Kanseiden_df.index.tolist(), 
                           Kanseiden_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=3, color = 'lime', 
                           label='Kansai')
    axs[i_row, i_col].plot(Okiden_df.index.tolist(), 
                           Okiden_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=2, color = 'deepskyblue', 
                           label='Okinawa')
#    axs[i_row, i_col].plot(Rikuden_df.index.tolist(), 
#                           Rikuden_df[variable_name] * 100, alpha=0.8,
#                           marker = '*', linewidth=3, color = 'slategray', 
#                           label='Rikuden')
    axs[i_row, i_col].plot(Siden_df.index.tolist(), 
                           Siden_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=2, color = 'navy', 
                           label='Shikoku')
    axs[i_row, i_col].plot(Toden_df.index.tolist(), 
                           Toden_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=2, color = 'darkviolet', 
                           label='Tokyu')
    axs[i_row, i_col].plot(Tohokuden_df.index.tolist(), 
                           Tohokuden_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=2, color = 'fuchsia', 
                           label='Tohoku')
    #axs[i_row, i_col].legend(loc='lower right', fontsize='large')
    axs[i_row, i_col].grid(True)
    axs[i_row, i_col].text(2000, text_y*100, sub_order[i], fontsize=20, weight='bold', color='r')
    axs[i_row, i_col].set_xlabel("Year", fontsize=15)
    axs[i_row, i_col].set_ylabel(variable_name + " (%)", fontsize=15)
    
axs[4, 1].plot([],[] , alpha=0.8, marker = '*', linewidth=2, color = 'red', 
               label='Kyushu')
axs[4, 1].plot([],[] , alpha=0.8, marker = '*', linewidth=2, color = 'sienna', 
               label='Chubu')
axs[4, 1].plot([],[] , alpha=0.8, marker = '*', linewidth=2, color = 'gold', 
               label='Chugoku')
axs[4, 1].plot([],[] , alpha=0.8, marker = '*', linewidth=2, color = 'lime', 
               label='Kansai')
axs[4, 1].plot([],[] , alpha=0.8, marker = '*', linewidth=2, color = 'deepskyblue', 
               label='Okinawa')
axs[4, 1].plot([],[] , alpha=0.8, marker = '*', linewidth=2, color = 'navy', 
               label='Shigoku')
axs[4, 1].plot([],[] , alpha=0.8, marker = '*', linewidth=2, color = 'darkviolet', 
               label='Tokyo')
axs[4, 1].plot([],[] , alpha=0.8, marker = '*', linewidth=2, color = 'fuchsia', 
               label='Tohoku')
axs[4, 1].legend(loc='lower right', fontsize=20)
axs[4, 1].set_axis_off()
    
#axs[4, 1].axis('off')
axs[4, 2].axis('off')
plt.show(); 
fig.savefig("Additional/05_JapaneseElec_Tendency.jpg", bbox_inches='tight')



### new figure pie chart tendency
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(29.7, 39.7), dpi=300, subplot_kw=dict(polar=True))
axs = axs.flatten()
#### average tendency
merged_df = Kyuden_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

colors = plt.cm.get_cmap('rainbow', avg_values.shape[0]+1)
x_lable = avg_values.index.tolist() + [avg_values.index.tolist()[0]]
x_lable = [item + " (%)" for item in x_lable]

ax = axs[0]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Kyushu Denryoku Average Tendency (2002-2023)", fontsize=22)


merged_df = Chubuden_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

ax = axs[1]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Chubu Denryoku Average Tendency (Only 2023)", fontsize=22)


merged_df = Chugokuden_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

ax = axs[2]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Chugoku Denryoku Average Tendency (2004-2012)", fontsize=22)


merged_df = Kanseiden_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

ax = axs[3]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Kansai Denryoku Average Tendency (2013-2017)", fontsize=22)


merged_df = Okiden_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

ax = axs[4]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Okinawa Denryoku Average Tendency (2000-2018)", fontsize=22)


merged_df = Siden_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

ax = axs[5]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Shikoku Denryoku Average Tendency (2018-2023)", fontsize=22)


merged_df = Toden_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

ax = axs[6]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Tokyo Denryoku Average Tendency (2000-2013, 2022)", fontsize=22)


merged_df = Tohokuden_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

ax = axs[7]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Tohoku Denryoku Average Tendency (2008-2022)", fontsize=22)


axs[8].axis('off')

plt.subplots_adjust(hspace=0.3)
plt.show();
fig.savefig("Additional/06_JapaneseElec_TendencyPie.jpg", bbox_inches='tight')


### compared with mean
data_avg = CPT_result_df.drop(['Company', 'Year'], axis=1).mean()
data_std = CPT_result_df.drop(['Company', 'Year'], axis=1).std()

### new figure pie chart tendency rebalance
fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(29.7, 39.7), dpi=300, subplot_kw=dict(polar=True))
axs = axs.flatten()
#### average tendency
merged_df = Kyuden_df
avg_values = merged_df.mean()
avg_values = avg_values

colors = plt.cm.get_cmap('rainbow', avg_values.shape[0]+1)
x_lable = avg_values.index.tolist() + [avg_values.index.tolist()[0]]
x_lable = [item for item in x_lable]

ax = axs[0]
data = (avg_values - data_avg)/data_std
data = data.tolist()

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Kyushu Denryoku Average Tendency (2002-2023)", fontsize=22)


merged_df = Chubuden_df
avg_values = merged_df.mean()
avg_values = avg_values

ax = axs[1]
data = (avg_values - data_avg)/data_std
data = data.tolist()

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Chubu Denryoku Average Tendency (Only 2023)", fontsize=22)


merged_df = Chugokuden_df
avg_values = merged_df.mean()
avg_values = avg_values

ax = axs[2]
data = (avg_values - data_avg)/data_std
data = data.tolist()

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Chugoku Denryoku Average Tendency (2004-2012)", fontsize=22)


merged_df = Kanseiden_df
avg_values = merged_df.mean()
avg_values = avg_values

ax = axs[3]
data = (avg_values - data_avg)/data_std
data = data.tolist()

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Kansai Denryoku Average Tendency (2013-2017)", fontsize=22)


merged_df = Okiden_df
avg_values = merged_df.mean()
avg_values = avg_values

ax = axs[4]
data = (avg_values - data_avg)/data_std
data = data.tolist()

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Okinawa Denryoku Average Tendency (2000-2018)", fontsize=22)


merged_df = Siden_df
avg_values = merged_df.mean()
avg_values = avg_values

ax = axs[5]
data = (avg_values - data_avg)/data_std
data = data.tolist()

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Shikoku Denryoku Average Tendency (2018-2023)", fontsize=22)


merged_df = Toden_df
avg_values = merged_df.mean()
avg_values = avg_values

ax = axs[6]
data = (avg_values - data_avg)/data_std
data = data.tolist()

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Tokyo Denryoku Average Tendency (2000-2013, 2022)", fontsize=22)


merged_df = Tohokuden_df
avg_values = merged_df.mean()
avg_values = avg_values

ax = axs[7]
data = (avg_values - data_avg)/data_std
data = data.tolist()

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("Tohoku Denryoku Average Tendency (2008-2022)", fontsize=22)


axs[8].axis('off')

plt.subplots_adjust(hspace=0.3)
plt.show();
fig.savefig("Additional/07_JapaneseElec_TendencyPie_Rebalance.jpg", bbox_inches='tight')












### Japanese
CPT_result_df = pd.read_csv('Data/NittoResult.csv', index_col=0)
CPT_result_df['company'] = CPT_result_df['nake_name'].str.split('/').str[-1].str.split('_').str[0]
CPT_result_df['year'] = CPT_result_df['nake_name'].str.split('/').str[-1].str.split('_').str[-1].str.split('.').str[0].astype(int)

CPT_result_df = CPT_result_df[CPT_result_df['year'] > 2009]

CPT_result_df = CPT_result_df[['company', 'year', 'model_i0_index', 
                               'model_i1_index', 'model_i2_index', 'model_i3_index',
                               'model_i4_index', 'model_i5_index', 'model_i6_index', 'model_i7_index',
                               'model_i8_index', 'model_i9_index', 'model_i10_index',
                               'model_i11_index', 'model_i12_index']]
CPT_result_df.columns = ['Company', 'Year', 'Community',
                         'Air Pollution', 'Greenhouse Gas', 'Water Consumption', 
                         'Mining Consumption', 'Work Environment',
                         'Safety and Health', 'Human Rights', 
                         'Governance Risk', 'Production Cost',
                         'Domestic Job Creation', 'Economic Ripple Effect',
                         'Domestic Reflux Rate'
    ]
CPT_result_df = CPT_result_df[['Company', 'Year','Air Pollution', 
                         'Greenhouse Gas', 'Water Consumption', 
                         'Mining Consumption',
                         'Work Environment', 'Community',
                         'Safety and Health', 'Human Rights', 
                         'Domestic Job Creation',
                         'Domestic Reflux Rate',
                         'Governance Risk', 'Production Cost',
                         'Economic Ripple Effect']]
CPT_result_df.columns = ['Company', 'Year','大気汚染', 
                         '温室効果ガス', '水資源消費', '採掘資源消費',
                         '労働環境・条件', 'コミュニティ','安全と健康', '人権影響', 
                         '国内雇用創出','国内還流率','ガバナンスリスク', '生産コスト',
                         '経済波及倍率']

Nitto_df = CPT_result_df[CPT_result_df['Company'] == 'Nitto'].copy()
Nitto_df = Nitto_df.drop('Company', axis=1)
Nitto_df.set_index('Year', inplace=True)

Sumitomo_df = CPT_result_df[CPT_result_df['Company'] == 'Sumitomo'].copy()
Sumitomo_df = Sumitomo_df.drop('Company', axis=1)
Sumitomo_df.set_index('Year', inplace=True)

X_colname = ['大気汚染', 
             '温室効果ガス', '水資源消費', '採掘資源消費',
             '労働環境・条件', 'コミュニティ','安全と健康', '人権影響', 
             '国内雇用創出','国内還流率','ガバナンスリスク', '生産コスト',
             '経済波及倍率']
sub_order = ['a', 'b', 'c', 'd', 'e', 
             'f', 'g', 'h', 'i', 'j', 
             'k', 'l', 'm']
fig, axs = plt.subplots(nrows=5, ncols=3, figsize=(21, 29.7), dpi=300)
for i, variable_name in enumerate(X_colname):
    i_row, i_col = i//3, i%3
    text_y = np.max(CPT_result_df[variable_name]) - 0.03 * (np.max(CPT_result_df[variable_name])-np.min(CPT_result_df[variable_name]))
    axs[i_row, i_col].plot(Nitto_df.index.tolist(), 
                           Nitto_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=3, color = '#FC5A50', 
                           label='日東電工')
    axs[i_row, i_col].plot(Sumitomo_df.index.tolist(), 
                           Sumitomo_df[variable_name] * 100, alpha=0.6,
                           marker = 'o', linewidth=3, color = '#C1F80A',
                           label='S社')
    axs[i_row, i_col].legend(loc='lower right', fontsize='large')
    axs[i_row, i_col].grid(True)
    axs[i_row, i_col].text(2010, text_y*100, sub_order[i], fontsize=20, weight='bold', color='r')
    axs[i_row, i_col].set_xlabel("年", fontsize=15)
    axs[i_row, i_col].set_ylabel(variable_name + " (%)", fontsize=15)
    
    
axs[4, 1].axis('off')
axs[4, 2].axis('off')
plt.show(); 
fig.savefig("Additional/04_Tendency.jpg", bbox_inches='tight')

### new figure
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(29.7, 21), dpi=300, subplot_kw=dict(polar=True))
axs = axs.flatten()
#### average tendency
merged_df = Nitto_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

colors = plt.cm.get_cmap('rainbow', avg_values.shape[0]+1)
x_lable = avg_values.index.tolist() + [avg_values.index.tolist()[0]]
x_lable = [item + " (%)" for item in x_lable]

ax = axs[0]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("日東電工の平均的なESG傾向 2010-2023", fontsize=18)

# 2022 Nitto
avg_values = Nitto_df.iloc[12:13,:]
avg_values = avg_values * 100

ax = axs[1]
data = avg_values.iloc[0,:].tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[1]+1)), 
       width = 2 * np.pi / avg_values.shape[1])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("日東電工のESG傾向 2022", fontsize=18)

# 2023 Nitto
avg_values = Nitto_df.iloc[13:,:]
avg_values = avg_values * 100

ax = axs[2]
data = avg_values.iloc[0,:].tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[1]+1)), 
       width = 2 * np.pi / avg_values.shape[1])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("日東電工のESG傾向 2023", fontsize=18)


### sumitomo average
merged_df = Sumitomo_df
avg_values = merged_df.mean()
avg_values = avg_values * 100

ax = axs[3]
data = avg_values.tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[0]+1)), 
       width = 2 * np.pi / avg_values.shape[0])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("S社の平均的なESG傾向 2010-2023", fontsize=18)

axs[4].axis('off')

### sumimoto 2022
avg_values = Sumitomo_df.iloc[12:,:]
avg_values = avg_values * 100

ax = axs[5]
data = avg_values.iloc[0,:].tolist() 

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

ax.bar(angles, data + [data[0]],
       color= colors(range(avg_values.shape[1]+1)), 
       width = 2 * np.pi / avg_values.shape[1])

ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=13)
ax.set_title("S社のESG傾向 2022", fontsize=18)

plt.subplots_adjust(hspace=0.3)
plt.show();
fig.savefig("Additional/03_TendencyPie.jpg", bbox_inches='tight')






