import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from datetime import datetime
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
def parse_date(x):
    return datetime.strptime(x, "%Y-%m-%d")

df= pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],date_parser=parse_date)
df=df.set_index('date')

# Clean data
bottom = df['value'].quantile(0.025)
top = df['value'].quantile(0.975)

outliers = df[(df.value<bottom) | (df.value>top)]
df=df.drop(outliers.index)
print(df.size)    


def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots(figsize=(10,5))
    sns.lineplot(df,palette=["red"]).set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    # plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    fig,ax=plt.subplots(figsize=(10,5))
    df_bar = df.groupby([df.index.year,df.index.month]).mean().unstack()
    df_bar.plot(kind='bar',ax=ax)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'])

    # Draw bar plot
    # plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,ax = plt.subplots(figsize=(10,5),ncols=2)
    ax2=sns.boxplot(x='year',y='value',data=df_box, ax=ax[0])
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Value')
    ax2.set_title('Year-wise Box Plot(Trend)')

    ax2=sns.boxplot(x='month',y='value',data=df_box, ax=ax[1])
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Value')
    ax2.set_title('Month-wise Box Plot(Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig