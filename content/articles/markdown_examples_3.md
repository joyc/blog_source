Title: Markdown Examples Part 3
Author: Hython
Date: 2019-01-04 12:00
Category: blogging
Tags: markdown, pygments

Code blocks are preceeded by an indent, three : symbols and the name of the language.  
All of the following code will be highlighted while the text is indented.

    :::python3
    def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper_do_twice

    @do_twice
    def say_whee(some_text):
        print(some_text)

    x = 'Whee!'
    say_whee(x)

Code blocks 2:

    :::html
    <!DOCTYPE html>
    <html>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <meta name="viewport" content="initial-scale=1, maximum-scale=1,user-scalable=no"/>
      <title>FeatureTable Formatting</title>
      <link rel="stylesheet" href="https://js.arcgis.com/3.26/dijit/themes/claro/claro.css">
      <script src="https://js.arcgis.com/3.26/"></script>
      <style>
        html, body, #map {
          width: 100%;
          height: 100%;
          margin: 0;
          padding: 0;
        }
      </style>
    </head>
    <body class="claro esri">
      <div data-dojo-type="dijit/layout/BorderContainer" data-dojo-props="design:'headline'" style="width:100%; height:100%;">
        <div data-dojo-type="dijit/layout/ContentPane" data-dojo-props="region:'center', splitter:true" style="height:50%">
          <div id="map"></div>
        </div>
        <div id="bot" data-dojo-type="dijit/layout/ContentPane" data-dojo-props="region:'bottom', splitter:true" style="height:50%">
          <div id="myTableNode"></div>
        </div>
      </div>
    </body>
    </html>

Code blocks 3:

    :::bash
    $sudo yum install -y yum-utils device-mapper-persistent-data lvm2

    $sudo yum-config-manager \
         --add-repo \
         http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    
Code blocks 4:

    :::javascript
    const aaa = (a, b) => {
      return "OK"
    }
    
Code blocks 5:

    :::java
    public static List<Integer> getTopLogN(List<Integer> originalList) {
    int index = originalList.size() - (int) round(log(originalList.size()) / log(2);
    int left = 0;
    int right = originalList.size() - 1;
    
    while (true) {
        int pivot = (left + right) / 2;
        pivot = partition(originalList, left, right, pivot);
        
        if (index == pivot) break;
        
        else if (index < pivot) right = pivot - 1;
        else left = pivot + 1;
    }

    return originalList.subList(index, originalList.size());
    }

Code blocks 5:

    ＃!/usr/bin/python
    def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper_do_twice

    @do_twice
    def say_whee(some_text):
        print(some_text)

    x = 'Whee!'
    say_whee(x)