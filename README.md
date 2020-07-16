CENG 2034 Assignment (for Midterm Exam) 
 
Write python script that implementing the following: 
 
1. Print PID of itself. (10 points) 
2. If the running OS is linux; print loadavg. (15 points) 
3. Take and print “5 min loadavg” value and cpu core count. If the loadavg value is near (or close) to the cpu core count (hint: nproc - 5min loadavg < 1) then exit script. (15 points)
4. We have an array of urls [‘​https://api.github.com​’, ‘​http://bilgisayar.mu.edu.tr/​’, ‘​https://www.python.org/​’,  ‘​http://akrepnalan.com/ceng2034​’, ‘​https://github.com/caesarsalad/wow​’]  Check if the links in these urls are valid (working) or not. (Hint: You can use python requests lib. HTTP response status code 2xx is successful. 4xx or 5xx means failed.) *Implement this with threads. (40 points) 
