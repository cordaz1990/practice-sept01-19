# The init Method 
# inside class Time:
  
  def _init_(self, hour = 0, minutes = 0, second = 0)
      self.hour = hour 
      self.minute = minute
      self.second = second
      
      self.hour = hour
 
time = Time()
time.print_time()
time = Time(9)
time.print_time()
time = Time(9, 45)
time.print_time()
09:45:00
