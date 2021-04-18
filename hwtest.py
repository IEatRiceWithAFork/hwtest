import discord 
from dhooks import Webhook, Embed
import datetime
def error(x):
    while True:
        print('Error: '+x+'\nPlease close program to fix error')
        input()
def dcolour(l):
    return 65536*l[0]+256*l[1]+l[2]
months = {'Jan':1,
          'Feb':2,
          'Mar':3,
          'Apr':4,
          'May':5,
          'Jun':6,
          'Jul':7,
          'Aug':8,
          'Sep':9,
          'Oct':10,
          'Nov':11,
          'Dec':12,
          'jan':1,
          'feb':2,
          'mar':3,
          'apr':4,
          'may':5,
          'jun':6,
          'jul':7,
          'aug':8,
          'sep':9,
          'oct':10,
          'nov':11,
          'dec':12}
today = datetime.datetime.today()
todaystr = str(today)
year = int(todaystr[0:4])
zero = datetime.timedelta(0)
oneday = datetime.timedelta(1+(today.weekday()==4)+2*(today.weekday()==5))
sevendays = datetime.timedelta(7)
todaystr = ('Updated ' + todaystr[8:10] + '/' + int(todaystr[5])*todaystr[5] +
            todaystr[6]+ '/' + todaystr[0:4] + ' ' +
            str((int(todaystr[11:13])-1)%12+1) + todaystr[13:16] +
            'am'*(int(todaystr[11:13])<12) + 'pm'*(int(todaystr[11:13])>=12))
hook = Webhook('https://discord.com/api/webhooks/832588732901097482/JjrM_G6onGCEhOdMAT1tJlppTRkW90s8qy6GnX2se-N5THYI94SuoaxVFyctodVANc-J')
hwprofile = 'https://cdn.discordapp.com/attachments/805731894914318337/811544677655380024/Screenshot_2021-02-13_at_12.37.31_PM.png'
# HIDDEN CHAR 'ㅤ'
e = []
tests = False
message = 'Homework'
statechanged = False
questionmark = False
xcolour = [255,0,0]
while input() != 'Homework':
    pass
e.append(Embed(author = 'HWOTD', title = todaystr, thumbnail = hwprofile, colour = discord.Colour.blue()))
e.append(Embed(title = 'HOMEWORK', colour = dcolour(xcolour)))
xcolour[2] += 20
inp = input()
if inp[0] != '[':
    error('Line after "Homework" should be a subject, please check format:\n"'+inp+'"')
while True: # subject
    if inp[-1] != ']':
        error('Please close or delete square bracket:\n"'+inp+'"')
    if tests and not statechanged:
        xcolour = [0,255,0]
        e.append(Embed(title='TESTS',colour=dcolour(xcolour)))
        statechanged = True
        message = 'Tests'
    e.append(Embed(title=inp[1:-1],colour=dcolour(xcolour)))
    if statechanged:
        xcolour[0] += 20
    else:
        xcolour[2] += 20
    fieldname = message
    while True: # band
        fieldtext = ''
        while True: # homework
            inp = input()
            if inp == 'Tests':
                tests = True
            if inp == '':
                continue
            if inp[0] == '>' or inp[0] == '[' or inp == 'have a nice day :)':
                break
            if '[' in inp and ']' in inp:
                if (inp.count('[') != 1 or inp.count(']') != 1
                    or inp.index('[')>inp.index(']')):
                    error('Please close or delete square bracket:\n"'+inp+'"')
                rawdate = inp[inp.index('['):inp.index(']')+1]
                if rawdate[1] == '?':
                    inp = '**' + inp + '**'
                else:
                    monthprocessed = False
                    dayprocessed = False
                    num = False
                    numstr = ''
                    for i in rawdate:
                        if i.isdigit():
                            num = True
                            numstr += i
                        else:
                            if num:
                                if monthprocessed:
                                    error('More than two numbers detected in date:\n"'+inp+'"')
                                elif dayprocessed:
                                    monthprocessed = True
                                    month = int(numstr)
                                else:
                                    dayprocessed = True
                                    day = int(numstr)
                                num = False
                                numstr = ''
                    for i in range(len(rawdate)-2):
                        if rawdate[i:i+3] in months:
                            if monthprocessed:
                                error('More than two months detected in date:\n"'+inp+'"')
                            else:
                                monthprocessed = True
                                month = months[rawdate[i:i+3]]
                    if not monthprocessed:
                        error('Less than two numbers detected in date:\n"'+inp+'"')
                    howlong = datetime.datetime(year+('next year' in rawdate),
                                                month,day) - today
                    if howlong <= zero:
                        inp = '~~' + inp + '~~'
                    elif howlong <= oneday:
                        inp = '__**' + inp + '**__'
                    elif howlong <= sevendays:
                        inp = '**'+inp+'**'
            else:
                inp = '- ' + inp
            fieldtext += inp + '\n'
        if fieldtext == '':
            fieldtext = '-'
        if inp[0] == '[' or inp == 'have a nice day :)':
            e[-1].add_field(name=fieldname,value=fieldtext,inline=False)
            break
        if fieldname != message:
            e[-1].add_field(name=fieldname,value=fieldtext,inline=False)
            fieldname = inp[2:]
        else:
            fieldname = inp[2:]
    if inp == 'have a nice day :)':
        break
# part where i have to purge
for i in e:
    hook.send(embed=i)
                
                
                

        

























    
