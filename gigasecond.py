from datetime import timedelta
def add_gigasecond(birthday):
    """ Calculate the moment when someone has lived for 10^9 seconds. """
    gigasecond = 10**9
    
    # transform gigaseconds to days, hours, minutes and seconds
    gigas_to_days = gigasecond // (24 * 60 * 60)
    gigas_to_hours = (gigasecond % (24* 60 * 60)) // (60 * 60)
    gigas_to_min = (gigasecond % (24 * 60 * 60) % (60 * 60)) // 60
    gigas_to_sec = gigasecond % (24 * 60 * 60) % (60 * 60) % 60
    
    return birthday + timedelta(days= gigas_to_days, seconds=gigas_to_sec, minutes=gigas_to_min, hours=gigas_to_hours) 