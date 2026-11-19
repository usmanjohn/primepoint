import pandas as pd
import numpy as np

import numpy as np
import plotly.graph_objects as go

def process_balans(balans):
    balans.columns = ['arcdate', 'account', 'currency', 'amount']
    balans['account'] = balans['account'].astype(str) 
    acc_num = balans["account"].astype(int)

    # 2. Define boolean masks for the conditions
    is_in_range = (acc_num > 11000) & (acc_num < 15800)
    starts_with_exclude = balans["account"].str.startswith(("115", "118"))
    ends_with_99 = balans["account"].str.endswith("99")

    # 3. Setup conditions list and matching choices
    conditions = [
        (is_in_range & ~starts_with_exclude & ~ends_with_99),  # brutto
        (is_in_range & ~starts_with_exclude & ends_with_99),  # reserve
        (balans["account"] == "95413"),  # spisat
    ]

    choices = ["brutto", "reserve", "spisat"]

    # 4. Generate the new 'type' column falling back to 'other'
    balans["type"] = np.select(conditions, choices, default="other")
    return balans
    
def format_number(value):
    try:
        value = float(value)
        """Format large numbers to B (billions) or T (trillions)."""
        if abs(value) >= 1_000_000_000_000:
            return f"{value / 1_000_000_000_000:.1f} Трлн."
        elif abs(value) >= 1_000_000_000:
            return f"{value / 1_000_000_000:.1f} Млрд."
        elif abs(value) >= 1_000_000:
            return f"{value / 1_000_000:.1f} Млн."
        return f"{value:,.0f} Сум"
    except (ValueError, TypeError):
        return value
        
def find_summa_and_npl(df, col=None, condition=None):
    # 1. Safe copy & strict filtering
    if col and condition is not None:
        try:
            if condition == 'all':
                df = df.copy()
            else:
                df = df[df[col] == condition].copy()
            
        except Exception as e:
            raise ValueError(f"Error filtering dataframe: {e}")
    else:
        df = df.copy()
        
    if df.empty:
        return {}
    # 2. Vectorized logic using numpy instead of creating new dataframe columns
    is_bad_npl = df['npl_category'] > 2
    brutto_bad = np.where(is_bad_npl, df['brutto_95_amount'], 0)
    region_t = ['Центр', 'Чиланзар', 'Юнусабад', 'Мирабад', 'Сергели', 'Яшнабад', 'Алмазар', 'Учтепа']  # DEMO: neutral names
    
    df['in_tashkent'] = np.where(df['branch'].isin(region_t), 'yes', 'no')

    # 3. Base totals
    total_portfel = df['brutto_95_amount'].sum()
    total_npl = brutto_bad.sum()
    
    # Avoid zero division early
    if total_portfel <= 0:
        return {}

    is_city = df['in_tashkent'] == 'yes'
    is_village = df['in_tashkent'] == 'no'
    
    portfel_arr = df['brutto_95_amount'].values
    
    # Local metrics
    total_city_portfel = portfel_arr[is_city].sum()
    total_city_npl = brutto_bad[is_city].sum()
    
    # Global metrics (Fixed the currency bug here)
    total_village_portfel = portfel_arr[is_village].sum()
    total_village_npl = brutto_bad[is_village].sum()
    


    # 4. Currency segmentation using boolean masks (faster than splitting dataframes)
    is_local = df['currency'] == 'local'
    is_global = df['currency'] == 'global'
    portfel_arr = df['brutto_95_amount'].values
    
    if 'int_rate_amount' not in df.columns:
        int_rate_arr = df['int_rate'].values
        local_int_rate_sum = (int_rate_arr[is_local] * portfel_arr[is_local]/100).sum()
        global_int_rate_sum = (int_rate_arr[is_global] * portfel_arr[is_global]/100).sum()
    else:
        int_rate_arr = df['int_rate_amount'].values
        local_int_rate_sum = int_rate_arr[is_local].sum()
        global_int_rate_sum = int_rate_arr[is_global].sum()
    # Local metrics
    total_local_portfel = portfel_arr[is_local].sum()
    total_local_npl = brutto_bad[is_local].sum()
    
    # Global metrics (Fixed the currency bug here)
    total_global_portfel = portfel_arr[is_global].sum()
    total_global_npl = brutto_bad[is_global].sum()
    
    # 5. Output generation
    prefix = str(condition) if condition is not None else 'total'
    
    return {
        f'{prefix}_portfel': total_portfel,
        f'{prefix}_npl': total_npl,
        f'{prefix}_npl_percent': (total_npl / total_portfel) * 100,
        f'{prefix}_local_portfel': total_local_portfel,
        f'{prefix}_global_portfel': total_global_portfel,
        f'{prefix}_local_npl': total_local_npl,
        f'{prefix}_global_npl': total_global_npl,
        f'{prefix}_local_avg_percent': (local_int_rate_sum / total_local_portfel * 100) if total_local_portfel > 0 else 0,
        f'{prefix}_global_avg_percent': (global_int_rate_sum / total_global_portfel * 100) if total_global_portfel > 0 else 0,
        f'{prefix}_local_npl_percent': (total_local_npl / total_local_portfel * 100) if total_local_portfel > 0 else 0,
        f'{prefix}_global_npl_percent': (total_global_npl / total_global_portfel * 100) if total_global_portfel > 0 else 0,
        f'{prefix}_city_portfel': total_city_portfel,
        f'{prefix}_village_portfel': total_village_portfel,
        f'{prefix}_city_npl': total_city_npl,
        f'{prefix}_village_npl': total_village_npl,
        f'{prefix}_city_npl_percent': (total_city_npl / total_city_portfel * 100) if total_city_portfel > 0 else 0,
        f'{prefix}_village_npl_percent': (total_village_npl / total_village_portfel * 100) if total_village_portfel > 0 else 0,
        'prefix':prefix
    }

def prepare_df(df, group_column, dept=None):
    try:
        df.loc[df['department'] == 'sk', 'department'] = 'rk'
        df = df[df['brutto_95_amount']>0]
        if dept and dept != 'all':
            df = df[df['department']==dept]
        df['is_bad_npl'] = df['npl_category'] > 2 
        df['brutto_bad'] = df['brutto_95_amount'].where(df['is_bad_npl'], 0)
        df['brutto_good'] = df['brutto_95_amount'].where(~df['is_bad_npl'], 0)
        
        # 3. Group by whatever dimension you need dynamically (e.g. department)
        grouped = df.groupby(group_column).agg(
            brutto_bad=('brutto_bad', 'sum'),
            brutto_good=('brutto_good', 'sum')
        ).reset_index().fillna(0)

        # 4. Calculate calculated totals & relative risk shares
        grouped['brutto_total'] = grouped['brutto_bad'] + grouped['brutto_good']
        grouped['bad_share'] = (grouped['brutto_bad'] / grouped['brutto_total'] * 100).fillna(0)
        grouped['good_share'] = (grouped['brutto_good'] / grouped['brutto_total'] * 100).fillna(0)
        grouped = grouped.sort_values('brutto_total', ascending = True)
        # 5. Format using your local layout number strings
        grouped['brutto_bad_formatted'] = grouped['brutto_bad'].apply(format_number)
        grouped['brutto_good_formatted'] = grouped['brutto_good'].apply(format_number)
        grouped['brutto_total_formatted'] = grouped['brutto_total'].apply(format_number)

        return grouped
    except Exception as e:
        print(f'{e} Error happened')
        return pd.DataFrame()

def generate_risk_chart(df, group_col, target_font="Arial", custom_color=None):
    if df is None or df.empty:
        
        fig = go.Figure()
        fig.update_layout(
            title="Нет данных для отображения",
            xaxis={"visible": False},
            yaxis={"visible": False}
        )
        chart_html = fig.to_html(
            full_html=False,
            include_plotlyjs=False,
            config={"displaylogo": False}
        )
        
        # --- HTML WRAPPER SYSTEM ---
        # Wraps the raw Plotly div in a scrollable CSS container 
        wrapper_html = f"""
        <div style="overflow-y: auto; overflow-x: hidden;">
            {chart_html}
        </div>
        """
        
        return wrapper_html
        # Assuming you want to return a components div string or figure object:
        # If your script expects a component string return: return fig.to_html() 
       

    COLOR_MAP = {
        'kk': '#5E4D21',
        'rk': '#1e3655',
        'mk': '#174d39',
    }
    active_dept = df['department'].iloc[0] if 'department' in df else 'All'
    good_color = COLOR_MAP.get(active_dept, custom_color or '#22e3a3')
    
    # --- SCROLL LOGIC SYSTEM ---
    ROW_LIMIT = 8            # Max bars to show without scrolling
    ROW_HEIGHT = 45          # Pixels allocated per bar
    BASE_PADDING = 100        # Pixels needed for margins and legend
    num_rows = len(df)
    #should set like > but I am finding this better
    if num_rows < ROW_LIMIT:
        # Calculate extended height if over the limit
        calculated_height = (num_rows * ROW_HEIGHT) + BASE_PADDING
    else:
        # Use your default static height if under the limit
        calculated_height = 450 
    
    hover_matrix = np.column_stack((
        df['brutto_good_formatted'], df['good_share'].round(1).astype(str) + '%',
        df['brutto_bad_formatted'], df['bad_share'].round(1).astype(str) + '%',
        df['brutto_total_formatted']
    ))
    
    hover_template = (
        '<b>%{y}</b><br>'
        'Стандарт: %{customdata[0]} (%{customdata[1]})<br>'
        'NPL (90+): %{customdata[2]} (%{customdata[3]})<br>'
        'Всего Портфел: %{customdata[4]}<extra></extra>'
    )
    
    hover_style = dict(bgcolor="white", font=dict(size=12), namelength=-1)
    traces_config = [
        {'x': df['brutto_bad'], 'name': 'NPL 90+', 'color': '#ef4444', 'text': None},
        {'x': df['brutto_good'], 'name': 'Стандарт', 'color': good_color, 'text': df['brutto_total_formatted']}
    ]

    fig = go.Figure()
    for t in traces_config:
        fig.add_trace(go.Bar(
            y=df[group_col],
            x=t['x'],
            orientation='h',
            name=t['name'],
            marker=dict(color=t['color'], cornerradius=3),
            opacity=0.9,
            text=t['text'],
            textposition='auto' if t['text'] is not None else 'none',
            hovertemplate=hover_template,
            hoverlabel=hover_style,
            customdata=hover_matrix,
            textfont=dict(size=16, color='#fff')
        ))

    fig.update_layout(
        barmode='stack',
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=5, r=5, t=5, b=5),
        height=calculated_height,  # Dynamic height injected here
        font=dict(size=16, family=target_font),
        legend=dict(
            orientation='h', yanchor='bottom', y=1.02, 
            xanchor='right', x=1, font=dict(size=14)
        )
    )
    fig.update_yaxes(tickfont=dict(size=12))
    
    buttons_to_kill = [
        'hoverClosestCartesian', 'pan2d', 'select2d', 'zoom2d', 
        'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'
    ]
    
    chart_html = fig.to_html(
        full_html=False,
        include_plotlyjs=False,
        config={"modeBarButtonsToRemove": buttons_to_kill, "displaylogo": False}
    )
    
    # --- HTML WRAPPER SYSTEM ---
    # Wraps the raw Plotly div in a scrollable CSS container 
    max_container_height = 450
    wrapper_html = f"""
    <div style="max-height: {max_container_height}px; overflow-y: auto; overflow-x: hidden;">
        {chart_html}
    </div>
    """
    
    return wrapper_html



import plotly.express as px
import pandas as pd

def generate_pie_chart(df, target_font='Arial', dept = None, group_col = None):
    # 1. Define the internal mappings for the 1-5 categories
    category_names = {
        1: 'Стандартный',
        2: 'Субстандартный',
        3: 'Неудовлетворительный',
        4: 'Сомнительный',
        5: 'Безнадежный'
    }
    
    color_map = {
        'Стандартный': '#00CC96',        # Green for Standard
        'Субстандартный': '#FFCC00',     # Yellow for Substandard
        'Неудовлетворительный': '#FF9900', # Orange for Unsatisfactory
        'Сомнительный': '#FF6666',       # Light Red for Doubtful
        'Безнадежный': '#CC0000'         # Dark Red for Hopeless
    }

    
    # 2. Aggregate the raw data (Replace column names if yours are different)
    # Filter out rows where amount is 0 or negative to avoid charting empty data
    
    df.loc[df['department'] == 'sk', 'department'] = 'rk'
    df = df[df['brutto_95_amount']>0]
    if dept and dept != 'all':
        df = df[df['department']==dept]
    df_filtered = df[df['brutto_95_amount'] > 0].copy()
    grouped = df_filtered.groupby(group_col)['brutto_95_amount'].sum().reset_index()
    grouped.columns = ['npl_category', 'total']
    
    # 3. Map numeric codes to text labels
    grouped['category_name'] = grouped['npl_category'].map(category_names)
    grouped = grouped.dropna(subset=['category_name'])
    
    # 4. Apply your exact custom number formatting
    grouped['total_formatted'] = grouped['total'].apply(format_number)
    
    # 5. Generate the Plotly pie chart with your exact design parameters
    fig_mk_category = px.pie(
        grouped,
        values='total',
        names='category_name',
        hole=0.4,
        color='category_name',
        color_discrete_map=color_map
    )
    
    fig_mk_category.update_traces(
        textinfo='percent',                    
        texttemplate='%{percent:.1%}',        
        hovertemplate=(
            '<b>%{label}</b><br>' +
            'Доля: %{percent:.1%}<br>' +
            'Сумма: %{customdata}<extra></extra>'
        ),
        customdata=grouped['total_formatted'],
        marker=dict(line=dict(color='#171717', width=2))
    )
               
    fig_mk_category.update_layout(
        showlegend=True,
        annotations=[dict(text="Категория", x=0.5, y=0.5, font_size=16, showarrow=False, font=dict(color='black', family=target_font))],
        margin=dict(t=50, b=50, l=50, r=50),    
        font=dict(family=target_font, size=14),    
        legend=dict(
            orientation='v',
            yanchor='middle',
            y=0.5,
            xanchor='right',
            x=1.1,
            font=dict(
                family=target_font,
                size=11,
                color="black"
            )
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # 6. Export to HTML string with your exact toolbar overrides
    fig_mk_cat = fig_mk_category.to_html(
        full_html=False,
        include_plotlyjs=False,
        config={
            "modeBarButtonsToRemove": ['hoverClosestCartesian', 'pan2d', 'select2d','zoom2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'],
            "displaylogo": False
        }
    )
    
    return fig_mk_cat    