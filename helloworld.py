import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import bokeh

with st.echo(code_location='below'):
    """
    ## Hello, World!
    """


    def print_hello(name="world"):
        st.write(f"## Привет, {name}")


    name = st.text_input("Your name", key="name", value="Anonymous")

    print_hello(name)


    a = st.slider("a")
    x = np.linspace(-10, 10, 500)
    df = pd.DataFrame(dict(x=x, y=x*np.cos(a * x)))
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x="x", y="y", ax=ax)
    st.pyplot(fig)



    @st.cache
    first_df = pd.read_csv(r"C:\Users\Андрей Михайлович\Desktop\nordics_weather.csv").dropna()
    countries = pd.DataFrame({
    'first column': ['Finland', 'Norway', 'Sweden'],
    'second column': [1, 2, 3]
    })

    option = st.selectbox(
    'Выберите страну:',
     countries['first column'])
    df_selection = first_df[lambda x: x["country"] == option]
    df_selection

    chart = (
    alt.Chart(df_selection)
        .mark_circle()
        .encode(x=alt.X("date:T"), y="tavg", tooltip="tavg")
     )

     st.altair_chart(
    (
          chart
          + chart.transform_loess("date", "tavg").mark_line()
    ).interactive())
    
    happy_df = pd.read_csv(r"C:\Users\Андрей Михайлович\Desktop\happy.csv").dropna()
    from bokeh.plotting import figure, show
    from bokeh.models import ColumnDataSource
    from bokeh.transform import factor_cmap, factor_mark
    from bokeh.layouts import row
    new_data = ColumnDataSource(happy_df)
    regions = ['Western Europe', 'North America and ANZ', 'Middle East and North Africa', 'Latin America and Caribbean', 'East Asia', 'Central and Eastern Europe', 'Commonwealth of Independent States', 'Sub-Saharan Africa', 'Southeast Asia','South Asia']
    from bokeh.core.enums import MarkerType
    markers = list(MarkerType)
    ### FROM: https://docs.bokeh.org/en/latest/docs/user_guide/data.html
    graph_1 = figure(title = "Index of happiness",sizing_mode="scale_both")
    graph_1.xaxis.axis_label = "Logged GDP per capita"
    graph_1.yaxis.axis_label = "Ladder score"
    graph_1.scatter("Logged GDP per capita", "Ladder score", source=new_data, legend_field="Regional indicator", fill_alpha=0.1, size=15, marker=factor_mark('Regional indicator', markers, regions), color=factor_cmap('Regional indicator', 'Turbo256', regions))
    graph_2 = figure(title = "Index of happiness",sizing_mode="scale_both")
    graph_2.scatter("Freedom to make life choices", "Ladder score", source=new_data, legend_field="Regional indicator", fill_alpha=0.1, size=15, marker=factor_mark('Regional indicator', markers, regions), color=factor_cmap('Regional indicator', 'Turbo256', regions))
    graph_2.xaxis.axis_label = "Freedom to make life choices"
    graph_2.yaxis.axis_label = "Ladder score"
    ### END FROM
    show(row(graph_1,graph_2))
    
    AAPL = pd.read_csv(r"C:\Users\Андрей Михайлович\Downloads\AAPL (3).csv").dropna()
    TSLA = pd.read_csv(r"C:\Users\Андрей Михайлович\Downloads\TSLA.csv").dropna()
    FB = pd.read_csv(r"C:\Users\Андрей Михайлович\Downloads\FB.csv").dropna()
    from bokeh.plotting import figure, show
    from bokeh.models import HoverTool,ColumnDataSource
    ### FROM:https://docs.bokeh.org/en/latest/docs/gallery/stocks.html
    def datetime(x):
        return np.array(x, dtype=np.datetime64)
    ### END FROM
    s_graph=figure(x_axis_type="datetime", title="Stock Prices (hide each of them by pushing abbreviations at the top left corner)")
    s_graph.xaxis.axis_label = 'date'
    s_graph.xaxis.axis_label = 'stock closing price'
    s_graph.line(datetime(AAPL['Date']), AAPL['Adj Close'], color=(23, 94, 35), legend_label='AAPL')
    s_graph.line(datetime(TSLA['Date']), TSLA['Adj Close'], color=(234, 42, 90), legend_label='TSLA')
    s_graph.line(datetime(FB['Date']), FB['Adj Close'], color=(250, 126, 25), legend_label='FB')
    s_graph.legend.location = "top_left"
    s_graph.legend.click_policy="mute"
    apple=ColumnDataSource(AAPL)
    TOOLTIPS =[('Open Price',"@{Open}"),
            ('Closing Price', "@{Close}"),
            ('Volume',"@{Volume}")]
    a_graph= figure(title="Apple Stock Prices",tooltips=TOOLTIPS)
    a_graph.line('Date', 'Adj Close', source=apple)
    ag.add_tools(HoverTool(
    tooltips=[( 'closing price',  'Adj Close' ),('volume', 'Volume')]))
    show(row(s_graph,ag))
