filepath1 = r'D:\pylearn\File\sign.txt'
sign_dict = {}
with open(filepath1) as sign_fie:
    print(sign_fie.read().splitlines())
    sign_fie_info = sign_fie.read().splitlines()


for sign_info in sign_fie_info:
    print(sign_info)
#     sign_time = sign_info.split(',')[0].strip()
#     lesson_id = sign_info.split(',')[1].strip()
#     student_id = sign_info.split(',')[2].strip()
#     print(student_id)
#     # print(time, sign_id, student_id)
#     toAdd = {'lessonId': lesson_id, 'signTime': sign_time}
#     if student_id not in sign_dict:
#         sign_dict[student_id] = []
#     sign_dict[student_id].append(toAdd)
#
# print(sign_dict)
