import pandas as pd
import warnings
from datetime import datetime
warnings.simplefilter("ignore")
#将monthly文件标准化
def raw_monthly_to_standard(filename:str,col:list,skip_row=None,to=None):
    if skip_row:
        dataf = pd.read_csv(filename, skiprows=skip_row)
    else:
        dataf = pd.read_csv(filename)
    if to:
        dataf[col].to_csv(to, index=None)
        return to
    else:
        dataf[col].to_csv(filename[:-4]+"_standard"+filename[-4:], index=None)
        return filename[:-4]+"_standard"+filename[-4:]

#将daily文件标准化
def raw_daily_to_standard(filename:str,col:list,year,skip_row=None,to=None):
    """
    默认col的前3个元素为date,year,month
    """
    if skip_row:
        dataf = pd.read_csv(filename, skiprows=skip_row)
    else:
        dataf = pd.read_csv(filename)
    date_time = []
    years = []
    month = []
    mean_max_temp = []
    mean_min_temp = []
    mean_mean_temp = []
    total_rain = []
    total_snow = []
    total_preceip = []
    for i in range(1, 13):
        date_time.append(datetime.strftime(datetime.strptime("%d-%d" % (year, i),"%Y-%m"),"%Y-%m"))
        years.append(year)
        month.append(i)
        mean_max_temp.append(dataf[dataf["Month"] == i]["Max Temp (°C)"].dropna().values.mean())
        mean_min_temp.append(dataf[dataf["Month"] == i]["Min Temp (°C)"].dropna().values.mean())
        mean_mean_temp.append(dataf[dataf["Month"] == i]["Mean Temp (°C)"].dropna().values.mean())
        total_rain.append(dataf[dataf["Month"] == i]["Total Rain (mm)"].dropna().values.sum())
        total_snow.append(dataf[dataf["Month"] == i]["Total Snow (cm)"].dropna().values.sum())
        total_preceip.append(dataf[dataf["Month"] == i]["Total Precip (mm)"].dropna().values.sum())
    data = dict(zip(col, [date_time, years, month, mean_max_temp, mean_min_temp, mean_mean_temp, total_rain, total_snow,
                       total_preceip]))
    t = pd.DataFrame(data)
    if to:
        t.to_csv(to, index=None)
        return to
    else:
        t.to_csv(filename[:-4]+"_standard"+filename[-4:], index=None)
        return filename[:-4]+"_standard"+filename[-4:]
#将标准化daily文件合并到monthly文件中
def merge_daily_into_monthly(dailys,month_file,to=None):

    month_df = pd.read_csv(month_file)
    print(dailys)
    for daily in dailys:
        day_df = pd.read_csv(daily)
        # print(day_df)
        month_df = pd.concat([month_df.dropna(),day_df.dropna()],axis=0)

        print(daily)
        month_df = month_df.groupby("Date/Time").mean()
        month_df = month_df.reset_index()  #groupby把列变为索引了，要转换回来
        print(month_df)
        # break

    # print(month_df)
    month_df.sort_values(by="Date/Time", ascending=False)
    if to:
        month_df.to_csv(to,index=None)
    else:
        month_df.to_csv(month_file)
    # print(month_df)

def standardize(month_files,daily_files,daily_years,col,month_skip,day_skip,to):
    # if len(month_files)>1:
    #先标准化每个文件
    standard_month = []
    for file in month_files:
        standard_month.append(raw_monthly_to_standard(file,col,month_skip))
    standard_daily = []
    for file,year in zip(daily_files,daily_years):
        standard_daily.append(raw_daily_to_standard(file,col,year,day_skip))

    #把一个文件孤立出来，其他文件分别与之合并即可
    standard = standard_daily+standard_month
    tmp = standard[0]
    standard = standard[1:]
    print(standard)
    print(tmp)
    merge_daily_into_monthly(standard,tmp,to)



# if __name__ == "__main__":
#     files = ["Data/Canada/Alberta/alberta.csv",
#              "Data/Canada/British_Columbia/British_Columbia.csv",
#              "Data/Canada/Manitoba/Manitoba.csv",
#              "Data/Canada/New_Brunswick/New_Brunswick.csv",
#              "Data/Canada/Newfoundland_Labrador/Newfoundland_Labrador.csv",
#              "Data/Canada/Northwest_TERRITORIES/Northwest_TERRITORIES.csv",
#              "Data/Canada/Nova_Scotia/Nova_Scotia.csv",
#              "Data/Canada/Nunavut/Nunavut.csv",
#              "Data/Canada/Ontario/Ontario.csv",
#              "Data/Canada/Prince_Edward_Island/Prince_Edward_Island.csv",
#              "Data/Canada/Quebec/Quebec.csv",
#              "Data/Canada/Saskatchewan/Saskatchewan.csv",
#              ]
#     month_file = "Data/Canada/Yukon/Yukon.csv"
#     to = "Data/Canada/Canada.csv"
#     merge_daily_into_monthly(files,month_file,to)
#     tmp = ["Date/Time", "Year", "Month", "Mean Max Temp (°C)", "Mean Min Temp (°C)", "Mean Temp (°C)",
#            "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)"]
# #     # # raw_monthly_to_standard("Data/Canada/Alberta/CALGARY_1956_1979.csv",tmp,18)
# #     # # raw_daily_to_standard("Data/Canada/Alberta/CALGARY_daily_2012.csv",tmp,2012,24)
# #     # merge_daily_into_monthly(["Data/Canada/Alberta/CALGARY_daily_2012_standard.csv"],
# #     #                          "Data/Canada/Alberta/CALGARY_1881_2012_standard.csv")
#     month_files = [
# "Data/Canada/Nunavut/BAKER_1946_2013.csv",
# "Data/Canada/Nunavut/CAMBRIDGE_1929_2015.csv"
# ]
#     daily_files = [
# "Data/Canada/Nunavut/BAKER_daily_2013.csv",
# "Data/Canada/Nunavut/BAKER_daily_2014.csv",
# "Data/Canada/Nunavut/BAKER_daily_2015.csv",
# "Data/Canada/Nunavut/BAKER_daily_2016.csv",
# "Data/Canada/Nunavut/BAKER_daily_2017.csv",
# "Data/Canada/Nunavut/BAKER_daily_2018.csv",
# "Data/Canada/Nunavut/BAKER_daily_2019.csv",
# "Data/Canada/Nunavut/CAMBRIDGE_daily_2015.csv",
# "Data/Canada/Nunavut/CAMBRIDGE_daily_2016.csv",
# "Data/Canada/Nunavut/CAMBRIDGE_daily_2017.csv",
# "Data/Canada/Nunavut/CAMBRIDGE_daily_2018.csv",
# "Data/Canada/Nunavut/CAMBRIDGE_daily_2019.csv"
# ]
#     years = [2013,2014,2015,2016,2017,2018,2019,2015,2016,2017,2018,2019]
#     to = "Data/Canada/Nunavut/Nunavut.csv"
#     standardize(month_files,daily_files,years,tmp,18,24,to)


