import requests
import time
import json
import xlwt
headers = {
        'Host': 'music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}
def get_comments(songId):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{0}?limit=100&offset=0'.format(songId) #字符串格式化
    response = requests.get(url=url, headers=headers)
    result = json.loads(response.text)
    temp = []
    for item in result['hotComments']:
        data = {}
        # 评论者id
        data['userId'] = item['user']['userId']
        # 评论者昵称
        data['nickname'] = item['user']['nickname']
        # 评论内容
        data['content'] = item['content'].replace("\n",",")
        # 评论发表时间
        timeArray = time.localtime(item['time'] / 1000)
        date = time.strftime("%H:%M:%S", timeArray)
        data['date'] = date
        # 点赞数
        data['likedCount'] = item['likedCount']
        temp.append(data)
    return temp
if __name__ == '__main__':
    list = ["评论者id","评论者昵称","评论内容","评论发表时间","点赞数"]
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("sheet1",cell_overwrite_ok=True)  # 创建工作表
    for index, item in enumerate(list):
        worksheet.write(0, index, item)
    for row_index,temp in enumerate(get_comments("1997438791")):
        for col_index, item in enumerate(temp.values()):
            worksheet.write(row_index+1, col_index, item)

    workbook.save('乌梅子酱.xls')
