from datetime import datetime, timedelta

def get_all_dates(start_year: int, end_year: int, start_month: int, end_month: int):
    all_dates = []

    for year in range(start_year, end_year + 1):
        # Define start and end months for each year to iterate
        if year == start_year:
            start_m = start_month
        else:
            start_m = 1
        
        if year == end_year:
            end_m = end_month
        else:
            end_m = 12
        
        for month in range(start_m, end_m + 1):
            if month == 12 and year != end_year:
                days_in_month = (datetime(year + 1, 1, 1) - datetime(year, month, 1)).days
            else:
                days_in_month = (datetime(year, month % 12 + 1, 1) - datetime(year, month, 1)).days
            
            for day in range(1, days_in_month + 1):
                all_dates.append(datetime(year, month, day).date())

    return all_dates

# Example usage
start_year = 2023
end_year = 2024
start_month = 11
end_month = 2

dates_between = get_all_dates(start_year, end_year, start_month, end_month)
print(dates_between)
