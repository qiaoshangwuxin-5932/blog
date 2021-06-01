# django的 url 导入时 如果使用include  必须  加/  例如  path('login/',include('Exam.urls')),
 *** 

# django 模板 导入的时候 例如 如果直接导入这种  render(xxxx,d)
‘’‘
d={
  1: {'room_id': 5501, 'type': 'common', 'room': '贾呗', 'status': '未入住'}, 
  2: {'room_id': 5502, 'type': 'common', 'room': '贾呗', 'status': '未入住'}, 
  3: {'room_id': 5503, 'type': 'common', 'room': 'null', 'status': '未入住'}, 
  4: {'room_id': 5504, 'type': 'two', 'room': 'null', 'status': '未入住'}, 
  5: {'room_id': 5505, 'type': 'two', 'room': 'null', 'status': '未入住'}, 
  6: {'room_id': 5506, 'type': 'two', 'room': 'null', 'status': '未入住'},
  7: {'room_id': 5507, 'type': 'two', 'room': '贾呗', 'status': '未入住'}
}
’‘’
>> 若想产出具体数据的话需要    <% for i in 1 %>这种，否则无法调用
>>若想正常返回后面字典的数据，   <% for key,values in d %>   且 render 输入时需要 （xxx，{‘d’：d}）
>>返回的values是{'room_id': 5501, 'type': 'common', 'room': '贾呗', 'status': '未入住'}     若想调用内部，values,type即可
