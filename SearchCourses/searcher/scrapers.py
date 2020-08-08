import time#, requests
#from requests_html import HTMLSession
from selenium import webdriver
from bs4 import BeautifulSoup as bs

# CLASSE SCRAPER: objetos que retornam links de cursos
#
#   INICIALIZAÇÃO: chamar o construtor com os parãmetros de busca:
#       subject = assunto da pesquisa
#       language = linguagem desejada ("ingles" ou "portugues" ou "tudo_l")
#       duration = duração desejada ("curto", "medio", "longo" ou "tudo_d")
#       dificulty = nivel do curso ("iniciante", "intermediario", "avancado" ou "tudo_n")
#
#   MÉTODOS:
#       udemy(), coursera() e edx() = retornam os links de cada plataforma
#       all() = retorna os links de tudo
#
#   OUTPUT : lista com strings de URLs
#
#   EXEMPLO DE CHAMADA
#       teste = Scraper("python", "ingles", "tudo_d", "tudo_n")
#       print(teste.all())

class Scraper():
    def __init__(self, subject, language, duration, difficulty):
        self.subject = subject.strip()
        self.subject = self.subject.replace(' ', '%20')
        self.language = language
        self.duration = duration
        self.difficulty = difficulty

    def base(self, base_url, search_url, class_selector):
        links = []
        try:
            driver = webdriver.Firefox()
            driver.get(search_url)
            time.sleep(7)
            html = driver.page_source
            soup = bs(html, features="lxml")
            for tag in soup.find_all("a", class_= class_selector):
                link = tag['href']
                if link.startswith("https://"):
                    links.append(link)
                else:
                    links.append(base_url + link)
            driver. quit()
            return links
        except:
            return links


    def udemy(self):
        temp = self.subject
        self.subject = self.subject.replace('%20', '+')
        dict = {
            "Inglês": "en",
            "Português": "pt",
            "Qualquer Idioma": "en&duration=pt",
            "Básico": "beginner",
            "Intermediário": "intermediate",
            "Avançado": "expert",
            "Qualquer Dificuldade": "beginner&instructional_level=intermediate&instructional_level=expert",
            "Curto": "short",
            "Médio": "medium",
            "Longo": "long&duration=extraLong",
            "Qualquer Duração": "short&duration=medium&duration=long&duration=extraLong"
        }
        links = []
        try:
            url = "https://www.udemy.com/courses/search/?duration=" + dict[str(self.duration)]
            url = url + "&instructional_level=" + dict[str(self.dificulty)]
            url = url + "&lang=" + dict[str(self.language)] + "&price=price-free&q=" + str(self.subject) + "&sort=relevance"
            classe = "udlite-custom-focus-visible course-card--container--3w8Zm course-card--large--1BVxY"
            links = self.base("https://www.udemy.com", url, classe)
            self.subject = temp
            return links
        except:
            self.subject = temp
            return links

    def coursera(self):
        dict = {
            "Inglês": "English",
            "Português": "Portuguese",
            "Qualquer Idioma": "English&allLanguages=Portuguese",
            "Básico": "Beginner",
            "Intermediário": "Intermediate",
            "Avançado": "Advanced",
            "Qualquer Dificuldade": "Beginner&productDifficultyLevel=Intermediate&productDifficultyLevel=Advanced",
            "Curto": "Less%20Than%202%20Hours&productDurationEnum=1-4%20Weeks",
            "Médio": "1-3%20Months",
            "Longo": "3%2B%20Months",
            "Qualquer Duração": "Less%20Than%202%20Hours&productDurationEnum=1-4%20Weeks&productDurationEnum=1-3%20Months&productDurationEnum=3%2B%20Months"
        }
        links = []
        try:
            url = "https://www.coursera.org/search?query=" + str(self.subject)
            url = url + "&index=prod_all_products_term_optimization&productDifficultyLevel=" + dict[str(self.dificulty)]
            url = url + "&productDurationEnum=" + dict[str(self.duration)] + "&allLanguages=" + dict[str(self.language)]
            classe = "rc-DesktopSearchCard anchor-wrapper"
            links = self.base("https://www.coursera.org", url, classe)
            if links[0].startswith("https://www.coursera.org/degrees/global-mph-imperial"):
                return []
            else:
                return links
        except:
            return links

    def edx(self):
        dict = {
            "Inglês": "English",
            "Português": "Portuguese",
            "Qualquer Idioma": "English&language=Portuguese",
            "Básico": "Introductory",
            "Intermediário": "Intermediate",
            "Avançado": "Advanced",
            "Qualquer Dificuldade": "Introductory&level=Intermediate&level=Advanced",
            "Curto": "Less%20Than%202%20Hours&productDurationEnum=1-4%20Weeks",
            "Médio": "1-3%20Months",
            "Longo": "3%2B%20Months",
            "Qualquer Duração": "Less%20Than%202%20Hours&productDurationEnum=1-4%20Weeks&productDurationEnum=1-3%20Months&productDurationEnum=3%2B%20Months"
        }
        links = []
        try:
            url = "https://www.edx.org/search?availability=Available%20now&language=" + dict[str(self.language)]
            url = url + "&level=" + dict[str(self.dificulty)] + "&q=" + str(self.subject)
            classe = "discovery-card-link"
            links = self.base("https://www.edx.org", url, classe)
            if links[0].startswith("https://www.edx.org/professional-certificate/berkeleyx-science-of-happiness-at-work"):
                return []
            else:
                return links
        except:
            return links

    def all(self):
        links1 = self.udemy()
        links2 = self.coursera()
        links3 = self.edx()
        return links1 + links2 + links3
