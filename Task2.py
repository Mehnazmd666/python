applicants = [    {"name": "Asha", "marks": [90, 85, 88], "attendance": 92, "income": 180000},
                  {"name": "Ravi", "marks": [82, 84, 80], "attendance": 88, "income": 220000},    
                  {"name": "Mina", "marks": [95, 58, 90], "attendance": 96, "income": 150000},    
                  {"name": "Kiran", "marks": [85, 85, 85], "attendance": 90, "income": 200000},
             ] 
eligible = [] 
for a in applicants:    
    total = sum(a["marks"])    
    aggregate = total / len(a["marks"])    
    ok = (aggregate >= 80 and min(a["marks"]) >= 60          
          and a["attendance"] >= 75 and a["income"] <= 250000)    
    if ok:        eligible.append((aggregate, a["attendance"], a["name"]))
    eligible.sort(key=lambda x: (x[0], x[1]), reverse=True) 
    if not eligible:    
        print("No eligible applicants") 
    else:    
        for rank, (marks, attendance, name) in enumerate(eligible, 1):        
            print(rank, name, "Aggregate:", round(marks, 2),              
                  "Attendance:", attendance)