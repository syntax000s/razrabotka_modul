import datetime
"""поступает в формате 19.06.2005"""
def form(t1):
    """
    input 22.12.2007
    output datatime
    """
    return datetime.datetime(t1[6::],t1[3:5],t1[0:2])

def output(t1):
    """
    return datatime
    output 09.02.2003
    """
    return f"{t1.day}.{t1.month}.{t1.year}"

def difference_in_days(t1,t2):
    """
    разница дат в днях
    """
    a=form(t1)
    b=form(t2)
    c=a-b
    return c.days

def minus_days(t1,day):
    """ 
    
    вычитание дней
    
    """
    t=form(t1)
    t= t - datetime.timedelta(days=day)

    


