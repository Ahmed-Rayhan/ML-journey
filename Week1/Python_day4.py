#task 1
my_data= [ 14, 25, 19, 24, 18  ]
my_data.append(100)
my_data.remove(my_data[1])
print(my_data)
print(sum(my_data))

#task 2
city=('Dhaka', 'Boston', 'Sydney', 'Tokyo', 'London')
print(city[2])
new_city=list(city)
new_city.append('Chittagong')
city=tuple(new_city)
print(city)

#task 3
subject_marks = {'Math': 80, 'Science': 85, 'History' : 82, 'English': 85, 'Physics': 80}
subject_marks['Biology'] = 88
subject_marks['Math'] = 86
average_mark = sum(subject_marks.values()) / len(subject_marks)
print(average_mark)
