def time(time_str):
    if 'AM' in time_str or 'PM' in time_str:
        period = time_str[-2:] 
        time_parts = time_str[:-2].strip().split(':')  
        hours = int(time_parts[0])
        if len(time_parts) > 1:
            minutes = int(time_parts[1])
        else: 
            minutes = 0
        if period == 'AM':
            if hours == 12:
                hours = 0
        else:
            if hours != 12:
                hours += 12
        result = str(hours)+':'+str(minutes)
        return result
    else:
        time_parts = time_str.strip().split(':')
        hours = int(time_parts[0])
        if  len(time_parts)>1:
            minutes = int(time_parts[1])
        else:
            minutes = 0
        if hours == 0:
            return('12'+':'+str(minutes)+'AM')
        elif hours <12:
            return(str(hours)+':'+str(minutes)+'AM')
        elif hours == 12:
            return(str(hours)+':'+str(minutes)+'PM')
        else:
            return(str(hours-12)+':'+str(minutes)+'PM')
        


