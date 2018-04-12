from datetime import datetime
from datetime import timedelta

def iso_to_gregorian(iso_year,iso_week,iso_day):
    fourth_jan_week=datetime(iso_year,1,4).isocalendar()[1]
    fourth_jan_day=datetime(iso_year,1,4).isocalendar()[2]
    return datetime(iso_year,1,4)+timedelta((iso_day-fourth_jan_day)+(iso_week-fourth_jan_week)*7)

def main():
    i=0
    code=0                      #used to check input(correct types of input or incorrect types of input)
    reset=0                     #used to check whether its new week or same week
    target_week=0               #used to check whether its new week or same week)
    day_summary=0               #working hours summary of one day
    week_summary=0              #working hours summary of one week
    statutory_overtime=0        #1.overtime within statutory working hours
    statutory_excess=0          #2.overtime in a excess of statutory working hours
    late_night=0                #3.Late-night overtime working hours
    holiday_prescribed=0        #4.Working hours on prescribed holiday
    holiday_statutory=0         #5.Working hours on statutory holiday
    if_input=True
    while code==0:
        input=raw_input().split()
        try:
            target_date=datetime.strptime(input[0],"%Y/%m/%d")
            code=0
        except:
            code=1                   #if incorrect input data is passed,the program returns 1
            pass
        if code==1:
            break
        #check whether its new week or same week
        #if its new week(reset=1),reset week working hours summary
        if target_date.isocalendar()[1]==target_week:
            reset=0
        else:
            reset=1
        if reset==1:
            week_summary=0
            reset=0

        # Daily aggregation is done in the unit of minutes.
        # calculating actual working hours excluding break time.
        tomorrow=0
        for i in range(len(input)-1):
            first=map(int,input[i+1].split("-")[0].split(":"))
            second=map(int,input[i+1].split("-")[1].split(":"))
            if target_date.isocalendar()[2]==7 or target_date.isocalendar()[2]==6:
                statutory_overtime+=0
            else:
                if second[0]>16:
                    if first[0]<=16:
                        if (work_minutes+(16-first[0])*60)<420:
                            statutory_overtime+=(second[0]-16)*60-(420-(work_minutes+(16-first[0])*60))
                        else:
                            statutory_overtime+=60
                elif first[0]<8:
                    if second[0]<=8:
                        statutory_overtime+=(second[0]-first[0])*60
                    else:
                        statutory_overtime+=(8-first[0])*60

            if second[0]>22:
                if first[0]<=22:
                    late_night+=(second[0]-22)*60
                else:
                    late_night+=(second[0]-first[0])*60

            if second[0]>24:
                if first[0]<24:
                    tomorrow=(second[0]-24)*60
                else:
                    tomorrow=(second[0]-first[0])*60
            work_minutes=(second[0]-first[0])*60+(second[1]-first[1])
            day_summary+=work_minutes

        #if the day is sunday or saturday or weekdays change the process
        week_summary+=day_summary

        if target_date.isocalendar()[2]==5:
            if day_summary>480:
                statutory_excess+=day_summary-480
            elif week_summary>2400:
                statutory_excess+=week_summary-2400
            if tomorrow>0:
                holiday_prescribed+=tomorrow
                statutory_excess-=tomorrow

        elif target_date.isocalendar()[2]==6:
            holiday_prescribed+=day_summary
            if tomorrow>0:
                holiday_statutory+=tomorrow
                holiday_prescribed-=tomorrow

        elif target_date.isocalendar()[2]==7:
            holiday_statutory+=day_summary

        elif target_date.isocalendar()[2]==1:
            if day_summary>480:
                statutory_excess+=day_summary-480
            elif week_summary>2400:
                statutory_excess+=week_summary-2400

        else:
            if day_summary>480:
                statutory_excess+=day_summary-480
            elif week_summary>2400:
                statutory_excess+=week_summary-2400
        day_summary=0

    #printing outputs
    #1.overtime within statutory working hours
    #2.overtime in a excess of statutory working hours
    #3.Late-night overtime working hours
    #4.Working hours on prescribed holiday
    #5.Working hours on statutory holiday
    if statutory_overtime%60<30:
        print statutory_overtime/60
    else:
        print statutory_overtime/60+1
    if statutory_excess%60<30:
        print statutory_excess/60
    else:
        print statutory_excess/60+1
    if late_night%60<30:
        print late_night/60
    else:
        print late_night/60+1
    if holiday_prescribed%60<30:
        print holiday_prescribed/60
    else:
        print holiday_prescribed+1
    if holiday_statutory%60<30:
        print holiday_statutory/60
    else:
        print holiday_statutory/60+1


if __name__=="__main__":
    code=0                           #exit code
    n=raw_input()
    try:
        agg_year,agg_month=map(int,n.split('/'))
        code=0
    except:
        code=1                   #if incorrect input data is passed,the program returns 1
        pass
    if code==0:
        agg_weeknumb=datetime(agg_year,agg_month,1).isocalendar()[1]
        agg_daynumb=datetime(agg_year,agg_month,1).isocalendar()[2]
        main()
