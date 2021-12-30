from django.urls import reverse

class PageInfo:

    def __init__(self, current_page, all_count, per_page, show_page, page_url):
        """
        :param current_page: 第几页
        :param all_count: 总个数
        :param per_page: 每页显示多少条
        """
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.per_page = per_page
        a, b = divmod(all_count, per_page)
        if b:
            a = a + 1
        self.all_pager = a
        self.show_page = show_page
        self.page_url = page_url

    def start(self):
        start = (self.current_page - 1) * self.per_page
        return start

    def end(self):
        end = self.current_page * self.per_page
        return end

    def pager(self):
        """
        页码显示
        :return: str-><a>></a>
        """
        url = reverse(self.page_url)
        page_list = []
        half = int((self.show_page - 1) / 2)
        if self.all_pager < self.show_page:
            # 左侧边界：如果总页数小于需要显示的页数,则显示1到所有页
            begin = 1
            stop = self.all_pager + 1
        else:
            if self.current_page <= half:

                # 左侧边界：如果当前页小于中间值,则说明当前页之前没有half数量的页码
                begin = 1
                stop = self.show_page + 1
            else:
                # 右侧边界：如果当前页大于中间值
                if self.current_page + half > self.all_pager:
                    # 超出右侧页码范围
                    begin = self.all_pager - self.show_page + 1
                    stop = self.all_pager + 1
                else:
                    # 未超出左右侧页码范围
                    begin = self.current_page - half
                    stop = self.current_page + half + 1

        if self.current_page > 1:
            # 上一页
            perv = f"<li><a href={url}?page={self.current_page - 1}>上一页</a></li>"
            page_list.append(perv)
        for item in range(begin, stop):
            if item == self.current_page:
                temp = f"<li class='active'><a href={url}?page={item}>{item}</a></li>"
            else:
                temp = f"<li><a href={url}?page={item}>{item}</a></li>"
            page_list.append(temp)
        if self.current_page < self.all_pager:
            # 下一页
            next = f"<li><a href={url}?page={self.current_page + 1}>下一页</a></li>"
            page_list.append(next)
        return "".join(page_list)