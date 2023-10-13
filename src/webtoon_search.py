import re
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By

def kakao_webtoon_search():
    # 웹 페이지로 이동합니다.
    tag_names = tag_search_entry.get().split()
    result_text.delete(1.0, END)  # 이전 검색 결과를 지우기 위해 텍스트 상자를 초기화합니다.
    webtoon_include_tags = {}
    webtoon_include_tags_number = {}
    webtoon_dic = {}
    for tag_name in tag_names:
        driver = webdriver.Chrome()
        webtoon_name_list = []
        driver.get("https://page.kakao.com/search/themekeyword?filterList=" + tag_name)
        # 데이터를 추출합니다.
        webtoon_name_elements = driver.find_elements(By.CSS_SELECTOR, 'div.w-full.overflow-hidden.my-5pxr [data-t-obj*="name"]')

        for webtoon_name_element in webtoon_name_elements:
            match = re.search(r'"name":"(.*?)"', webtoon_name_element.get_attribute("data-t-obj"))
            if match:
                webtoon_name = match.group(1)
                webtoon_name_list.append(webtoon_name)

        webtoon_id_elements = driver.find_elements(By.CSS_SELECTOR, 'div.w-full.overflow-hidden.my-5pxr [data-t-obj*="series_id"]')
        webtoon_id_list = []

        for webtoon_id_element in webtoon_id_elements:
            match = re.search(r'"series_id":"(.*?)"', webtoon_id_element.get_attribute("data-t-obj"))
            if match:
                webtoon_id = match.group(1)
                webtoon_id_list.append(webtoon_id)

        for webtoon_name, webtoon_id in zip(webtoon_name_list, webtoon_id_list):
            webtoon_dic[webtoon_name] = webtoon_id
        driver.quit()

        for webtoon_name in webtoon_name_list:
            if webtoon_name in webtoon_include_tags_number:
                webtoon_include_tags_number[webtoon_name] += 1
            else:
                webtoon_include_tags_number[webtoon_name] = 1
            if webtoon_name in webtoon_include_tags:
                webtoon_include_tags[webtoon_name].append(tag_name)
            else:
                webtoon_include_tags[webtoon_name] = [tag_name]

    webtoon_include_tags_number = dict(sorted(webtoon_include_tags_number.items(), key=lambda x: x[1], reverse=True))

    for webtoon_name in webtoon_include_tags_number:
        # 검색 결과를 텍스트 상자에 추가합니다.
        result_text.insert(END, f"{webtoon_name} (해당하는 태그: {', '.join(webtoon_include_tags[webtoon_name])})\n")
        button = Button(result_text, text="전체 태그 보기", bd=0, fg="blue", cursor="hand2")
        button.bind("<Button-1>", lambda event, name = webtoon_name : show_webtoon_tags(name, webtoon_dic))
        result_text.window_create(END, window=button)
        result_text.insert(END, "\n")

 
def show_webtoon_tags(webtoon_name, webtoon_dic):
    # 태그를 보여줄 새로운 창을 생성합니다.
    tag_window = Toplevel(window)
    tag_window.title(f"{webtoon_name} 태그")

    # 태그를 보여줄 텍스트 상자를 생성합니다.
    tag_text = Text(tag_window, width=40, height=10)
    tag_text.pack()

    # 웹 페이지로 이동하여 태그를 추출합니다.
    tag_url = "https://page.kakao.com/content/" + webtoon_dic[webtoon_name]
    driver = webdriver.Chrome()
    driver.get(tag_url)

    find_webtoon_tags_elements = driver.find_elements(By.CSS_SELECTOR, 'div.flex.flex-wrap.px-32pxr button[data-t-obj*="copy"]')
    for find_webtoon_tag_element in find_webtoon_tags_elements:
        match = re.search(r'"copy":"(.*?)"', find_webtoon_tag_element.get_attribute("data-t-obj"))
        if match:
            find_webtoon_tag = match.group(1)
            tag_text.insert(END, find_webtoon_tag + "\n")

    driver.quit()


window = Tk()
window.title("Webtoon Search")
tag_search_entry = Entry(window)
tag_search_entry.grid(row=0, column=0)

Button(window, text="검색", command=kakao_webtoon_search).grid(row=0, column=1)

result_text = Text(window, width=60, height=30)
result_text.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(window, command=result_text.yview)
scrollbar.grid(row=1, column=2, sticky=N+S)
result_text.config(yscrollcommand=scrollbar.set)

mainloop()