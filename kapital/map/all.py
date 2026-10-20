import json
import plotly.express as px
import pandas as pd
from django.shortcuts import render
import os
from general.functions import read_recent_file
from general.formatters import format_number
from django.contrib.auth.decorators import login_required

@login_required
def mapper(request):
    npl_or_portfel = request.GET.get('choice')
    if npl_or_portfel == 'npl':
        colorising = 'percent'
        color = 'Reds'
    else:
        colorising = 'total'
        color = 'Greens' 
        # Sample DataFrame with fictional population data
    all_regions = {
        'region_code': ['UZAN', 'UZBU', 'UZJI', 'UZQA', 'UZNG', 'UZNW', 'UZSA', 'UZSU', 'UZSI', 'UZXO', 'UZFA', 'UZQR', 'UZTK'],  # Combine UZTO and UZTK into UZTK
        'region_name_rus': [
            'Андижанская область',
            'Бухарская область',
            'Джизакская область',
            'Кашкадарьинская область',
            'Наманганская область',
            'Навоийская область',
            'Самаркандская область',
            'Сурхандарьинская область',
            'Сырдарьинская область',
            'Хорезмская область',
            'Ферганская область',
            'Республика Каракалпакстан',
            'Ташкент (город и область)'  # Combined name
        ],
        'region_name_show': [
            'Андижан',
            'Бухара',
            'Джизак',
            'Кашкадаря',
            'Наманган',
            'Навоий',
            'Самарканд',
            'Сурхандаря',
            'Сырдаря',
            'Хорезм',
            'Фергана',
            'Каракалпакстан',
            'Ташкент'  # Combined name
        ],
        'population': [
            3100000, 1900000, 1400000, 3200000, 2700000, 1000000, 3800000, 2600000, 850000, 1600000, 3700000, 1900000,
            2900000 + 2900000  # Sum population of UZTO and UZTK
        ]
    }
    
    region_mapping = {
        'Андижанская область': 'Андижанская область',
        'Бухарская область': 'Бухарская область',
        'Кашкадарьинская область': 'Кашкадарьинская область',
        'Ферганская область': 'Ферганская область',
        'г. Ташкент с учетом Ташкентской области': 'Ташкент (город и область)',  # Map to combined region
        'Наманганская область': 'Наманганская область',
        'Республика Каракалпакстан': 'Республика Каракалпакстан',
        'Самаркандская область': 'Самаркандская область',
        'Сурхандарьинская область': 'Сурхандарьинская область',
        'Хорезмская область': 'Хорезмская область'
    }
    region_mapping_1 = {
        'Андижанская область': 'Андижан',
        'Бухарская область': 'Бухара',
        'Кашкадарьинская область': 'Кашкадаря',
        'Ферганская область': 'Фергана',
        'г. Ташкент с учетом Ташкентской области': 'Ташкент',  # Map to combined region
        'Наманганская область': 'Наманган',
        'Республика Каракалпакстан': 'Каракалпакстан',
        'Самаркандская область': 'Самарканд',
        'Сурхандарьинская область': 'Сурхандаря',
        'Хорезмская область': 'Хорезм'
    }
    
    df = pd.DataFrame(all_regions)
    
    # Load and process loan portfolio data
    lp, lp_name = read_recent_file()
    print("This is", lp.columns)
    lp_reg = pd.pivot_table(lp, index='region', columns='is_npl', values='Ос. кр. на балансе(экв.брутто)', aggfunc='sum').reset_index()
    lp_reg[['yes', 'no']] = lp_reg[['yes', 'no']].fillna(0)
    lp_reg['yes'] = lp_reg['yes'].fillna(0)
    
    lp_reg['total'] = lp_reg['yes'] + lp_reg['no']
    lp_reg['total'] = lp_reg['total'].fillna(0)
    lp_reg['percent'] = lp_reg['yes'] / lp_reg['total'].replace(0, 1)*100  # Avoid division by zero
    lp_reg['geojson_region'] = lp_reg['region'].map(region_mapping_1)
    
    # Aggregate Tashkent City and Region data
    lp_reg = lp_reg.groupby('geojson_region').agg({
        'yes': 'sum',
        'no': 'sum',
        'total': 'sum',
        'percent': 'mean'  # Average percent for combined region
    }).reset_index()
    
    # Merge with all regions to ensure all are included
    df = pd.merge(df, lp_reg, left_on='region_name_show', right_on='geojson_region', how='left')
    
    df['total'] = df['total'].fillna(0)
    df['yes'] = df['yes'].fillna(0)
    df['percent'] = df['percent'].fillna(0)
    df['percent']= df['percent'].round(1)
    
    df = df.sort_values(colorising, ascending = False)
    
    # Load GeoJSON
    geojson_path = 'service/uz.json'
    with open(geojson_path, 'r') as f:
        geojson_data = json.load(f)
    
    # Modify GeoJSON to combine UZTO and UZTK
    for feature in geojson_data['features']:
        if feature['properties']['id'] == 'UZTO':
            feature['properties']['id'] = 'UZTK'  # Map UZTO to UZTK
    
    # Create Plotly Choroplethmapbox
    df['NPL'] = df['yes'].apply(format_number).fillna(0)
    df['КП'] = df['total'].apply(format_number).fillna(0)
    
    fig = px.choropleth_mapbox(
        df,
        geojson=geojson_data,
        locations='region_code',
        featureidkey='properties.id',
        color=colorising,
        color_continuous_scale=color,
        range_color=[0, df[colorising].max() or 1],
        mapbox_style='carto-positron',
        zoom=5,
        center={'lat': 41.3775, 'lon': 64.5853},
        opacity=0.7,
        labels={'total': 'Объем кредитов (у.е.)', 'region_name_show': 'Регион', 'NPL': 'NPL90+', 'percent': 'Доля NPL (%)'},
        hover_data=['region_name_rus', 'КП', 'percent', 'NPL'],
        width=1100,
        height=800
    )
    
    # Update layout for a polished look
    fig.update_layout(
        modebar={
        'orientation': 'v',  # Vertical orientation for left-side modebar
        'remove': ['pan', 'lasso', 'select', 'select2d', 'box'],  # Remove pan, lasso, and box select buttons
        'bgcolor': 'rgba(255, 255, 255, 0.5)',  # Semi-transparent background
        'color': 'black',
        
    },
        
        margin={'r': 0, 't': 0, 'l': 0, 'b': 0},
        mapbox=dict(
            accesstoken='your_mapbox_token_here'  # Replace with your Mapbox token
        ),
        
        
        paper_bgcolor='rgba(245,245,245,1)',
        plot_bgcolor='rgba(245,245,245,1)',
        showlegend=True,
        transition=dict(duration=500, easing='cubic-in-out')
    )
    
    # Convert Plotly figure to JSON for client-side updates
   
    
    return render(request, 'service/map.html', {'lp_name':lp_name,
        'plot_div': fig.to_html(full_html=False),
        'regions': df[['region_name_show', 'total', 'percent', 'NPL']].to_dict('records'),
        'data_json': df[['region_code', 'total', 'percent', 'NPL']].to_json(orient='records')
    })