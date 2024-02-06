# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:44:29 2024

@author: Li Chao
"""

import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CPT_result_df = pd.read_csv('Data/NittoResult.csv', index_col=0)
CPT_result_df['company'] = CPT_result_df['nake_name'].str.split('/').str[-1].str.split('_').str[0]
CPT_result_df['year'] = CPT_result_df['nake_name'].str.split('/').str[-1].str.split('_').str[-1].str.split('.').str[0].astype(int)

CPT_result_df = CPT_result_df[CPT_result_df['year'] > 2009]

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

Nitto_df = CPT_result_df[CPT_result_df['Company'] == 'Nitto'].copy()
Nitto_df = Nitto_df.drop('Company', axis=1)
Nitto_df.set_index('Year', inplace=True)

Sumitomo_df = CPT_result_df[CPT_result_df['Company'] == 'Sumitomo'].copy()
Sumitomo_df = Sumitomo_df.drop('Company', axis=1)
Sumitomo_df.set_index('Year', inplace=True)

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
    axs[i_row, i_col].plot(Nitto_df.index.tolist(), 
                           Nitto_df[variable_name] * 100, alpha=0.8,
                           marker = '*', linewidth=3, color = '#FC5A50', 
                           label='Nitto')
    axs[i_row, i_col].plot(Sumitomo_df.index.tolist(), 
                           Sumitomo_df[variable_name] * 100, alpha=0.6,
                           marker = 'o', linewidth=3, color = '#C1F80A',
                           label='Sumitomo')
    axs[i_row, i_col].legend(loc='lower right', fontsize='large')
    axs[i_row, i_col].grid(True)
    axs[i_row, i_col].text(2010, text_y*100, sub_order[i], fontsize=20, weight='bold', color='r')
    axs[i_row, i_col].set_xlabel("Year", fontsize=15)
    axs[i_row, i_col].set_ylabel(variable_name + " (%)", fontsize=15)
    
    
axs[4, 1].axis('off')
axs[4, 2].axis('off')
plt.show(); 
fig.savefig("Additional/02_Tendency.jpg", bbox_inches='tight')



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
ax.set_title("Nitto Average Tendency From 2010-2023", fontsize=18)

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
ax.set_title("Nitto Tendency on 2022", fontsize=18)

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
ax.set_title("Nitto Tendency on 2023", fontsize=18)


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
ax.set_title("Sumitomo Average Tendency From 2010-2023", fontsize=18)

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
ax.set_title("Sumitomo Tendency on 2022", fontsize=18)

plt.subplots_adjust(hspace=0.3)
plt.show();
fig.savefig("Additional/01_TendencyPie.jpg", bbox_inches='tight')


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






