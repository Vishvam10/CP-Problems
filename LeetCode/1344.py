class Solution:
    # Degree covered by hour hand (hour area + minutes area)
    # Degree covered by minute hand (Each minute = 6 degree)
    
    # Absolute angle between them
    # req = angle(hour_hand) - angle(minute_hand)
    
    # If req is obtuse, convert to acute 
    
    def angleClock(self, hour: int, minutes: int) -> float:
        ha = (hour%12 * 30) + (minutes/60 * 30)
        ma = minutes * 6
        ang = abs(ma - ha)
        if ang > 180:
            ang = 360.0 - ang
        return ang
