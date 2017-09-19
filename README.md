# Test taks

project for test task and we can write another description.


POST -  api/v1/postfile/

keys:
'file': file.pdf

response:
200 ok
403 forbidden type of file


GET -  api/v1/generalinfo/

keys:
--

response:
200 :
    [
        {
            "count_urls": 2,
            "id": 1,
            "filename": "test.pdf"
        }
    ]


GET -  api/v1/postfile-info/[pk]

keys:
--

response:
200 :
    [
        {
            "model": "crawler.foundlinks",
            "pk": 1,
            "fields": {
                "url": "http://test.com.ua"
            }
        },
        {
            "model": "crawler.foundlinks",
            "pk": 2,
            "fields": {
                "url": "http://test2.com.ua"
            }
        }
    ]
