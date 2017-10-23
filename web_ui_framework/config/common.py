#coding:utf-8

# html元素定位方式
G_LOCAL = {
    "id":"By.ID",
    "name":"By.NAME",
    "xpath":"By.XPATH",
    "tag":"By.TAG",
    "link":"By.LINK_TEXT",
    "class":"By.CLASS",
    "css":"By.ID",
    "partiallink":"find_element_by_partial_link_text"
}

# assertion
G_LOCAL_ASSERT = {
    "assert_text":"By.ID",
    "name":"By.NAME",
    "xpath":"By.XPATH",
    "tag":"By.TAG",
    "link":"By.LINK_TEXT",
    "class":"By.CLASS",
    "css":"By.ID",
    "partiallink":"find_element_by_partial_link_text"
}

# 关键字定义
G_LOCAL_KEY = {
    'input':'send', # 键盘输入
    'input_Text':'send', # 键盘输入
    'get_text':'getText', # 获取文本
    'get_attr':'getAttr', # 获取熟悉
    'click':'click', # 鼠标单击
    'startbrowser':'startBrowser',# 启动浏览器
    'openurl':'get', # 打开网页
    'get':'get',     # 打开网页
    'set_page_timeout':'setPageTimeout', # 设置网页加载timeout
    'snapshot':'snapshot', # 截图
    'switch_to_frame':'switchToFrame', # 切换至特定frame
    'select_by_value':'selectByValue', # 通过选择框value选择下拉选项
    'select_by_text':'selectByText', # 通过选择框可视文本选择下拉选项
    'contain':'contain', # 包含验证
    'equal':'equal', # 相等验证
    'sleep':'waiting', # 延时，以秒为单位，参数可以传入整数、浮点数
    'close':'close', # 关闭窗口
    'quit':'quit',   # 退出浏览器
    'max':'maxWindow', # 最大化浏览器
    'switch_to_active_element':'switchToActiveEle', # 切换至活动的html 元素
    'alert_dismiss':'alertDismiss', # 取消alert窗口
    'alert_confirm':'alertConfirm', # 确定alert窗口
    'switch_to_alert':'switchToAlert',# 切换至alert窗口
    'max_window':'maxWindow', # 最大化浏览器
    'switch_to_default_frame':'switchToDefaultFrame', # 切换至默认的frame
    'clear':'clearCookies' # 清除所有cookies
}