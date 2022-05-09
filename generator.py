from datetime import timedelta, datetime
from pytz import timezone

def water_schedule_generator(duration,day_number,water_coming_first_time):
  water_coming_first_day = water_coming_first_time
  # water_coming_first_day = datetime(2022, 4, 25, 4, 00, 23, 218739)
  
  
  water_schedule = []
  for day in range(day_number,20,3):
    alternate_water_coming_day = water_coming_first_day + timedelta(day)
    water_schedule.append(alternate_water_coming_day)
  # print(water_schedule)
  
  
                 
  # printing original list
  # print("The original list is : " + str(water_schedule))
    
  # initializing test date 
  # present_time = datetime(2022, 5, 7, 8, 11, 23, 218739) - timedelta(hours=duration)
  present_time = datetime.now() 
  
  present_time_kathmandu = present_time.astimezone(timezone('Asia/Kathmandu'))
  formated_present_time =present_time_kathmandu.strftime("%m/%d/%Y, %H:%M")
  print(f"Current Date and Time = {formated_present_time}")
  # get all differences with date as values 
  cloz_dict = { 
    abs(present_time.timestamp() - date.timestamp()) : date 
    for date in water_schedule
  }
    
  # extracting minimum key using min()
  res = cloz_dict[min(cloz_dict.keys())]
  
  
  # printing result
  # print("Nearest date from list : " + str(res))

  #manupulate present time, to show routine during water is available 
  present_time -= timedelta(hours=duration) 
  
  if present_time>res:
    #time passed
    res_index = water_schedule.index(res)
    time_to_display = water_schedule[res_index+1]
  else:
    #time yet to come
    time_to_display = res

  
  #display final result to User
  final_result_showing_user_start =time_to_display.strftime("%m/%d/%Y, %H:%M")
  final_result_showing_user_end =time_to_display + timedelta(hours=duration)
  final_result_showing_user_end = final_result_showing_user_end.strftime("%H:%M")
  return final_result_showing_user_start,final_result_showing_user_end
#   print(f"Water-Coming Date & Time = {final_result_showing_user_start} to {final_result_showing_user_end}")