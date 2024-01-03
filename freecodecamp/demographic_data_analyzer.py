import pandas as pd

def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv("adult.data.csv")

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = (df[["race"]].value_counts())

  # What is the average age of men?
#   num_of_men=df[["sex"]].value_counts()["Male"]
#   df_of_men=df[df.sex.isin(['Male'])]
  col_of_men=df[df.sex.isin(['Male'])].age
#   print(col_of_men.mean())
  average_age_men = col_of_men.mean().round(1)

  # What is the percentage of people who have a Bachelor's degree?
  count_of_bach=df[df.education.isin(['Bachelors'])].education.count()
  total_size=df.shape[0]
  val = (count_of_bach/total_size)*100
  percentage_bachelors = val.round(1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  count_of_adv=df[df.education.isin(['Bachelors', 'Masters','Doctorate'])]
  sal_of_adv=count_of_adv[count_of_adv.salary.isin(['>50K'])].salary.count()
  size_of_adv=count_of_adv.shape[0]
  adv_value=(sal_of_adv/size_of_adv)*100
  # What percentage of people without advanced education make more than 50K?
  # with and without `Bachelors`, `Masters`, or `Doctorate`
  count_of_without=df[~df.education.isin(['Bachelors', 'Masters','Doctorate'])]
  sal_of_without=count_of_without[count_of_without.salary.isin(['>50K'])].salary.count()
  size_of_wo=count_of_without.shape[0]
  wo_value=(sal_of_without/size_of_wo)*100
  lower_education = None

  # percentage with salary >50K
  higher_education_rich = adv_value.round(1)
  lower_education_rich = wo_value.round(1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_hrs=df["hours-per-week"].min()
  min_work_hours = min_hrs

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  min_val=df[df["hours-per-week"].isin([min_hrs])]
  min_time=min_val[min_val.salary.isin(['>50K'])].salary.count()
  min_size=min_val.shape[0]
  min_ans=(min_time/min_size)*100
  num_min_workers = int(min_ans)

  rich_percentage = num_min_workers

  # What country has the highest percentage of people that earn >50K?
  high_salary_per_country= df[df['salary'] == ">50K"]['native-country'].value_counts()
  num_country = df['native-country'].value_counts()
  percentage = (high_salary_per_country/num_country)*100
  highest_earning_country = percentage.idxmax()
  highest_earning_country_percentage = percentage.max().round(1)

  # Identify the most popular occupation for those who earn >50K in India.
  india=df[df['native-country'].isin(['India'])]
  sal_india_total=india[india['salary'].isin(['>50K'])]['occupation'].shape[0]
  sal_india=india[india['salary'].isin(['>50K'])]['occupation'].value_counts()
  top_IN_occupation = sal_india.idxmax()

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }

print(calculate_demographic_data(False))
