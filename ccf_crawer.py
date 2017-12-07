import urllib.request
import re
from html.parser import HTMLParser

title_dict = ('试题编号：', '试题名称：', '时间限制：', '内存限制：', '问题描述', '输入格式', '输出格式', '评测用例规模与约定', '样例输入', '样例输出', '样例说明')


class Sample:
    def __init__(self, sample_input: str = None, sample_output: str = None, sample_description: str = None):
        self.sample_input = sample_input
        self.sample_output = sample_output
        self.sample_description = sample_description


class Question:
    id_text = '## ' + title_dict[0] + '\n\n'
    name_text = '\n\n## ' + title_dict[1] + '\n\n'
    time_limit_text = '\n\n## ' + title_dict[2] + '\n\n'
    memory_limit_text = '\n\n## ' + title_dict[3] + '\n\n'
    description_text = '\n\n## ' + title_dict[4] + '\n\n'
    input_format_text = '\n\n## ' + title_dict[5] + '\n\n'
    output_format_text = '\n\n## ' + title_dict[6] + '\n\n'
    sample_input_text = '\n\n## ' + title_dict[8] + '\n\n'
    sample_output_text = '\n\n## ' + title_dict[9] + '\n\n'
    sample_description_text = '\n\n## ' + title_dict[10] + '\n\n'
    sample_detail_text = '\n\n## ' + title_dict[7] + '\n\n'
    pictures = []

    def __init__(self,
                 id: str,
                 name: str,
                 time_limit: str,
                 memory_limit: str,
                 description: str,
                 input_format: str,
                 output_format: str,
                 sample_detail: str,
                 samples: list,
                 pictures=None):
        self.id = id
        self.name = name
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.description = description
        self.input_format = input_format
        self.output_format = output_format
        self.sample_detail = sample_detail
        self.samples = samples
        if pictures is None:
            pictures = []
        self.pictures = pictures

    def to_md(self):
        description = self.description
        for picture in self.pictures:
            description = description.replace(picture, '\n\n![](' + picture + '.png)\n\n')
        result = self.id_text
        result += self.id
        result += self.name_text
        result += self.name
        result += self.time_limit_text
        result += self.time_limit
        result += self.memory_limit_text
        result += self.memory_limit
        result += self.description_text
        result += description
        result += self.input_format_text
        result += self.input_format
        result += self.output_format_text
        result += self.output_format
        for sample in self.samples:
            result += self.sample_input_text
            result += '```\n' + sample.sample_input + '\n```'
            result += self.sample_output_text
            result += '```\n' + sample.sample_output + '\n```'
            if sample.sample_description:
                result += self.sample_description_text
                result += sample.sample_description
        if self.sample_detail:
            result += self.sample_detail_text
            result += self.sample_detail
        return result

    def __str__(self):
        return self.to_md()


def parse_question_from_dict(question_dict):
    return Question(question_dict[0],
                    question_dict[1],
                    question_dict[2],
                    question_dict[3],
                    question_dict[4],
                    question_dict[5],
                    question_dict[6],
                    question_dict[7],
                    question_dict[8],
                    question_dict[9])


class QuestionParser(HTMLParser):
    def error(self, message):
        print(message)

    def __init__(self):
        super().__init__()
        self.next_is_title = False
        self.next_is_content = False
        self.next_title = 0
        self.question_dict = ['', '', '', '', '', '', '', '', [], []]
        self.current_sample: Sample = Sample()

    def feed(self, data):
        self.__init__() # TODO There are still bugs with `sup` and `sub` tags.
        data = data.replace('　', '').replace('<br />', '\n').replace('<i>', ' `').replace('</i>', '` ').replace('</sup>', ' `/sup` ').replace('<sup>', ' `sup` ').replace('</sub>', ' ` /sub` ').replace('<sub>', ' `sub` ')
        HTMLParser.feed(self, data)

    def handle_starttag(self, tag, attrs):
        if not len(attrs):
            return
        if (tag == 'div' and 'pdsec' in attrs[0]) or (tag == 'td' and 'probref' in attrs[0]):
            self.next_is_title = True
            return
        if tag == 'img' and '/RequireFile.do?fid=' in attrs:
            self.question_dict[-1].append(attrs['src'].replace('/RequireFile.do?fid=', ''))

    def handle_endtag(self, tag):
        if tag == "div" or tag == "td":
            self.next_is_title = False
            return

    def handle_data(self, data):
        if self.next_is_title:
            try:
                data = re.compile('\d').sub('', data)
                self.next_title = title_dict.index(data) + 1
            except ValueError:
                self.next_title = 0
            return
        if self.next_title:
            if self.next_title < title_dict.__len__() - 2:  # sample
                if not self.question_dict[self.next_title - 1]:
                    self.question_dict[self.next_title - 1] = data
            elif self.next_title == title_dict.__len__() - 2:
                if self.current_sample.sample_input:
                    self.question_dict[- 2].append(self.current_sample)
                    self.current_sample = Sample()
                self.current_sample.sample_input = data
            elif self.next_title == title_dict.__len__() - 1:
                self.current_sample.sample_output = data
            elif self.next_title == title_dict.__len__():
                self.current_sample.sample_description = data
            self.next_title = 0
            return

    def get_question(self):
        self.question_dict[-2].append(self.current_sample)
        self.question_dict[title_dict.index('问题描述')] = self.question_dict[title_dict.index('问题描述')].replace(' `/sup` ', '</sup>').replace(' `sup` ', '<sup>').replace('` /sub` ', '</sub>').replace(' `sub` ', '<sub>')
        return parse_question_from_dict(self.question_dict)


def save_question(question: Question):
    with open('ccf/' + question.name + '.md', 'w', encoding='utf-8') as f:
        f.write(question.to_md())
        print(question.name + '.md written')


opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
login_url = 'http://118.190.20.162/UserEnter.do?USERKEY=test&NAME=test&CODE=CPP'
question_url = 'http://118.190.20.162/view.page?gpid='
request = urllib.request.Request(login_url)
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
response = opener.open(request)
result = response.read().decode()

times = re.findall('<tr><td class="idn">[0-9].*?-[0-9]</td>', result)
titles = re.findall('<td style="text-align:left; padding-left:20px;">.*?</td>', result)
urls = re.findall('<a href="/submitlist.page\?gpid=T[0-9]{1,2}" class="bluebtn">查看我的提交</a>', result)

for i in range(0, times.__len__()):
    times[i] = times[i].replace('<tr><td class="idn">', '').replace('</td>', '')
    titles[i] = titles[i].replace('<td style="text-align:left; padding-left:20px;">', '').replace('</td>', '')
    urls[i] = urls[i].replace('<a href="/submitlist.page?gpid=', '').replace('" class="bluebtn">查看我的提交</a>', '')
    print(times[i], titles[i], urls[i])

parser = QuestionParser()

for url in urls:
    content = opener.open(question_url + url).read().decode().encode('utf-8').decode('utf-8')
    parser.feed(content)
    question = parser.get_question()
    save_question(question)
    parser.close()
