import win32evtlog # requires pywin32 pre-installed
import win32evtlogutil
import re
import json

def getEvents(server, eventtype, search):
    hand = win32evtlog.OpenEventLog(server,eventtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    ignorecase = re.compile(search, re.IGNORECASE)
    print ignorecase
    print total
    print search
    events = 1
    current = 0
    percentcount = 0
    while events:
        events = win32evtlog.ReadEventLog(hand, flags,0)
        if events:
            for event in events:
                current = current + 1
                category = str(event.EventCategory)
                time =  str(event.TimeGenerated)
                source = str(event.SourceName)
                eventID =  str(event.EventID)
                eventtype = str(event.EventType)
                data =  str(win32evtlogutil.SafeFormatMessage(event, eventtype))   
                if ignorecase.match(data) or ignorecase.match(source):
                    resultarray = [int(current/float(total) * 100),time, source, category, eventID, eventtype, data.replace("<","").replace(">","")]
                    yield 'data: %s\n\n' % str(json.dumps(resultarray))
                else:
                    if current == total:
                        yield 'data: %s\n\n' % str(json.dumps([100]))
                    if (current/float(total) > (percentcount + 1)*0.1):
                        yield 'data: %s\n\n' % str(json.dumps([int(current/float(total) * 100)]))
                        percentcount = percentcount + 1

    yield 'data: %s\n\n' %str(json.dumps([100]))
    print "Done"



