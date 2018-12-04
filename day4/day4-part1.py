from datetime import datetime
import re



class GuardEntry:
    pattern = re.compile(r'\[(.*)\]\s(.*)')
    datetime_format = "%Y-%m-%d %H:%M"

    def __init__(self, line):
        (time_string, event) = self.parse(line)
        self.timestamp = datetime.strptime(time_string, GuardEntry.datetime_format)
        self.event = event

    def parse(self, line):
        match = re.search(GuardEntry.pattern, line)
        return (match.group(1), match.group(2))

class GuardShift:
    id_pattern = re.compile(r'#(\d+)')
    
    def __init__(self, entries):
        self.guard_id = re.search(GuardShift.id_pattern, entries[0].event).group(1)
        print("NEW SHIFT")
        
        for entry in entries[1:]:
            print(entry.event)
        
        self.shift_start_timestamp = entries[0].timestamp
        self.falls_asleep_timestamp = entries[1].timestamp
        self.wakes_up_timestamp = entries[2].timestamp

def main():
    entries = parse_input()
    entries.sort(key = lambda x: x.timestamp)
    grouped_entries = group_entries(entries)
    print(type(grouped_entries[0][0]))
    shifts = [GuardShift(group) for group in grouped_entries]
    print(shifts[0].guard_id)

def parse_input():
    return [GuardEntry(line) for line in open('input-day4.txt')]

def group_entries(entries):
    result = []
    shift = []
    for entry in entries:
        if "#" in entry.event: # start of new shift
            if len(shift) > 0:
                result.append(shift) # add shift to result
                shift = [] # clear shift
        shift.append(entry)
    return result
        
if __name__ == "__main__":
    main()